import argparse
import os
import sys
import subprocess
from typing import Optional


def find_ffmpeg() -> Optional[str]:
	"""Return path to ffmpeg if available, else None. Tries PATH first, then imageio-ffmpeg."""
	# Try system ffmpeg
	try:
		subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
		return "ffmpeg"
	except Exception:
		pass

	# Try bundled via imageio-ffmpeg
	try:
		import imageio_ffmpeg

		ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()
		if ffmpeg_path and os.path.exists(ffmpeg_path):
			return ffmpeg_path
	except Exception:
		pass

	return None


def ensure_dependencies() -> str:
	"""Ensure ffmpeg is available. Returns path or 'ffmpeg' if on PATH.
	Raises RuntimeError with guidance if not found.
	"""
	ffmpeg_path = find_ffmpeg()
	if not ffmpeg_path:
		raise RuntimeError(
			"ffmpeg is required but not found.\n"
			"Install ffmpeg (https://ffmpeg.org/download.html) OR install the Python package 'imageio-ffmpeg' to bundle one."
		)
	return ffmpeg_path


def build_ydl_options(output_dir: str, ffmpeg_location: Optional[str]) -> dict:
	# Prefer mp4-compatible 720p video + m4a audio; fallback to best <=720p mp4
	format_selector = (
		"bv*[height<=720][height>=720][ext=mp4]+ba[ext=m4a]/b[height<=720][ext=mp4]/b[height<=720]"
	)
	outtmpl = os.path.join(output_dir, "%(playlist_title)s", "%(playlist_index)02d - %(title)s.%(ext)s")

	opts = {
		"format": format_selector,
		"outtmpl": outtmpl,
		"noplaylist": False,
		"ignoreerrors": True,
		"merge_output_format": "mp4",
		"restrictfilenames": True,
		"writethumbnail": False,
		"quiet": False,
		"continuedl": True,
		"consoletitle": True,
		# Ensure only the final merged file remains
		"keepvideo": False,
		"postprocessor_args": {
			"FFmpegVideoRemuxer": ["-c:v", "copy", "-c:a", "copy"],
		},
		# Clean re-run behavior
		"overwrites": True,
		"no_keep_fragments": True,
		"retries": 10,
		"fragment_retries": 10,
	}

	if ffmpeg_location:
		opts["ffmpeg_location"] = ffmpeg_location

	return opts


def download_playlist(playlist_url: str, output_dir: str) -> int:
	from yt_dlp import YoutubeDL

	ffmpeg_path = ensure_dependencies()
	os.makedirs(output_dir, exist_ok=True)
	opts = build_ydl_options(output_dir, ffmpeg_path)

	with YoutubeDL(opts) as ydl:
		result = ydl.download([playlist_url])
	return int(result) if isinstance(result, int) else 0


def parse_args(argv=None):
	parser = argparse.ArgumentParser(
		description="Download all videos from a YouTube playlist in 720p using yt-dlp.",
	)
	parser.add_argument(
		"playlist_url",
		help="URL of the YouTube playlist",
	)
	parser.add_argument(
		"-o",
		"--output",
		default="downloads",
		help="Output directory (default: downloads)",
	)
	return parser.parse_args(argv)


def main(argv=None) -> int:
	args = parse_args(argv)
	try:
		return download_playlist(args.playlist_url, args.output)
	except RuntimeError as e:
		print(str(e), file=sys.stderr)
		return 1


if __name__ == "__main__":
	raise SystemExit(main())

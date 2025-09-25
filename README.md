# Free Palestine 

# YouTube Playlist Downloader

A simple Python tool to download all videos from a YouTube playlist in 720p quality with merged audio and video.

## Features

- Downloads entire YouTube playlists automatically
- Prefers 720p quality (falls back to best available ≤720p)
- Merges video and audio into single MP4 files
- Organizes videos by playlist name and index
- Cross-platform support (Windows, macOS, Linux)
- Automatic FFmpeg detection and fallback

## Requirements

- Python 3.9 or higher
- FFmpeg (will be auto-detected or bundled)

## Installation

### Step 1: Clone or Download
```bash
git clone https://github.com/yourusername/youtube-playlist-downloader.git
cd youtube-playlist-downloader
```

### Step 2: Set up Python Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Verify Installation
```bash
python playlist_downloader/cli.py --help
```

## Usage

### Basic Usage
```bash
python playlist_downloader/cli.py "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID" -o "downloads"
```

### With Custom Output Directory
```bash
python cli.py "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID" -o "C:\Users\YourName\Videos\Playlists"
```

### Using PowerShell Wrapper (Windows)
```powershell
.\download_playlist.ps1 "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID" "C:\Users\YourName\Videos\Playlists"
```

## Examples

### Download a Course Playlist
```bash
python cli.py "https://www.youtube.com/playlist?list=PLoyB9yetHDhCQfXY-AYyApaDooHHlPbR1" -o "courses"
```

### Download Music Playlist
```bash
python cli.py "https://www.youtube.com/playlist?list=YOUR_MUSIC_PLAYLIST_ID" -o "music"
```

## Output Structure

Videos are organized as follows:
```
output_folder/
└── Playlist_Name/
    ├── 01 - First_Video_Title.mp4
    ├── 02 - Second_Video_Title.mp4
    └── 03 - Third_Video_Title.mp4
```

## Command Line Options

- `playlist_url`: YouTube playlist URL (required)
- `-o, --output`: Output directory (default: "downloads")

## Troubleshooting

### Python Not Found
If you get "python is not recognized":
- Use `py` instead of `python` on Windows
- Or use the full path: `.venv\Scripts\python.exe`

### FFmpeg Not Found
The tool will automatically:
1. Try to find FFmpeg in your system PATH
2. Use bundled FFmpeg via imageio-ffmpeg
3. Show installation instructions if neither is found

### Permission Errors
- Run PowerShell as Administrator if needed
- Ensure you have write permissions to the output directory

## Technical Details

- Uses `yt-dlp` for YouTube downloading
- Prefers MP4-compatible formats for better compatibility
- Automatically merges separate video/audio streams
- Cleans up temporary files after merging
- Supports resume functionality for interrupted downloads

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Feel free to use, modify, and distribute.

## Disclaimer

This tool is for educational purposes only. Please respect YouTube's Terms of Service and copyright laws. Only download content you have permission to download.

---


# Free Palestine


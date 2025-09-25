param(
    [Parameter(Mandatory=$true)][string]$PlaylistUrl,
    [Parameter(Mandatory=$false)][string]$OutputDir = "downloads"
)

$ErrorActionPreference = "Stop"

# Activate venv if found
$venvActivate = Join-Path -Path ".venv" -ChildPath "Scripts\Activate.ps1"
if (Test-Path $venvActivate) {
    . $venvActivate
}

# Ensure dependencies (yt-dlp) are available
try {
    python -c "import yt_dlp" | Out-Null
} catch {
    Write-Host "Installing dependencies..."
    pip install -r requirements.txt | Out-Null
}

python playlist_downloader/cli.py $PlaylistUrl -o $OutputDir

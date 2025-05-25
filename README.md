ytdl-download-cli

Advanced YouTube Video & Playlist Downloader CLI

---

## Features

- Download videos with selectable quality (e.g., 720p, 1080p, best)  
- Download audio only (mp3)  
- Download entire playlists  
- Automatic merging of video and audio streams  
- Progress display in terminal  
- Custom output directory  

---

## Installation

```bash
git clone https://github.com/T6ARB/ytdl-download-cli.git
cd ytdl-download-cli
pip install -r requirements.txt
```

Make sure you have `ffmpeg` installed on your system (required for audio extraction and merging).

---

## Usage

### Download a single video (best quality)

```bash
python ytdl.py download <youtube_url>
```

### Download a video with specific quality (e.g., 720p)

```bash
python ytdl.py download <youtube_url> --quality 720
```

### Download audio only (mp3)

```bash
python ytdl.py download <youtube_url> --audio-only
```

### Download a playlist

```bash
python ytdl.py playlist <playlist_url>
```

### Specify output directory

```bash
python ytdl.py download <youtube_url> --output /path/to/folder
```

---

## Notes

- Supports all YouTube URL formats  
- Progress bar updates in terminal  
- Uses `yt-dlp` under the hood (a powerful youtube-dl fork)  
- Requires `ffmpeg` installed and available in PATH  

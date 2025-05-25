import os
import sys
import click
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError

@click.group()
def cli():
    """Advanced YouTube Video Downloader CLI"""
    pass

@cli.command()
@click.argument('url')
@click.option('--audio-only', is_flag=True, help='Download audio only (mp3)')
@click.option('--quality', default='best', help='Video quality e.g. 720, 1080, best')
@click.option('--output', default='downloads', help='Output directory')
def download(url, audio_only, quality, output):
    """Download video or audio from YouTube URL"""
    os.makedirs(output, exist_ok=True)

    ydl_opts = {
        'outtmpl': os.path.join(output, '%(title)s.%(ext)s'),
        'progress_hooks': [progress_hook],
    }

    if audio_only:
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        # Select video+audio format by quality preference
        # yt-dlp format selection syntax to prioritize given quality height:
        # Try to get the requested height, fallback to best
        fmt = f'bestvideo[height<={quality}]+bestaudio/best[height<={quality}]/best'
        ydl_opts['format'] = fmt

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except DownloadError as e:
        click.echo(f'Error: {e}', err=True)
        sys.exit(1)

def progress_hook(d):
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
        if total_bytes:
            percent = d['downloaded_bytes'] / total_bytes * 100
            click.echo(f"\rDownloading... {percent:.1f}%", nl=False)
    elif d['status'] == 'finished':
        click.echo('\nDownload finished, processing...')

@cli.command()
@click.argument('url')
@click.option('--audio-only', is_flag=True, help='Download audio only (mp3)')
@click.option('--quality', default='best', help='Video quality e.g. 720, 1080, best')
@click.option('--output', default='downloads', help='Output directory')
def playlist(url, audio_only, quality, output):
    """Download all videos from a playlist URL"""
    os.makedirs(output, exist_ok=True)

    ydl_opts = {
        'outtmpl': os.path.join(output, '%(playlist_index)03d - %(title)s.%(ext)s'),
        'progress_hooks': [progress_hook],
        'ignoreerrors': True,
    }

    if audio_only:
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        fmt = f'bestvideo[height<={quality}]+bestaudio/best[height<={quality}]/best'
        ydl_opts['format'] = fmt

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except DownloadError as e:
        click.echo(f'Error: {e}', err=True)
        sys.exit(1)

if __name__ == '__main__':
    cli()

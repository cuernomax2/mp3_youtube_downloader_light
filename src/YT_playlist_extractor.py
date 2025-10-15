import yt_dlp
playlist_url = 'https://music.youtube.com/playlist?list=PLEDShO75npvoLEwS5aLcrShvS6fZ3Ygpu'

def extract_links_from_playlist(url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(url, download=False)

        if 'entries' in result:
            for entry in result['entries']:
                print(entry['url'])

if __name__ == '__main__':
    extract_links_from_playlist(playlist_url)

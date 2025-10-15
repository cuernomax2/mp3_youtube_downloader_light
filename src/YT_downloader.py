import yt_dlp

video_urls = [
    # 'https://music.youtube.com/watch?v=D83PDsxA-3A',
    # 'https://music.youtube.com/watch?v=PSRJFwpaY9Q',
    # 'https://music.youtube.com/watch?v=uFaC-L1_DEk',
    # 'https://music.youtube.com/watch?v=0hbdrqiUmbc',
    # 'https://music.youtube.com/watch?v=lIpfJrcLTCA',
    # 'https://music.youtube.com/watch?v=b19R5pITN0s',
    # 'https://music.youtube.com/watch?v=pIJdAEdJmcc',
    # 'https://music.youtube.com/watch?v=W4g0fRlkzrM',
    # 'https://music.youtube.com/watch?v=7_-shcIVE0w',
    # 'https://music.youtube.com/watch?v=R5O_neFRYwI',
    # 'https://music.youtube.com/watch?v=RbvMQLRcza0',
    # 'https://music.youtube.com/watch?v=AYfxqb8n74o',
    # 'https://music.youtube.com/watch?v=uIDzmw0SsmI',
    # 'https://music.youtube.com/watch?v=2gWxGlPYils',
    # 'https://music.youtube.com/watch?v=gCloRAaMje4',
    # 'https://music.youtube.com/watch?v=HjdIvAiLPIM',
    # 'https://music.youtube.com/watch?v=WDpccSrDtkQ',
    # 'https://music.youtube.com/watch?v=muFsahYaq3Y',
    # 'https://music.youtube.com/watch?v=E9XDix2jLN8',
    # 'https://music.youtube.com/watch?v=ecpitgeoh80',
    # 'https://music.youtube.com/watch?v=1mq7lHcE5po',
    # 'https://music.youtube.com/watch?v=fivG7FT0LYE',
    # 'https://music.youtube.com/watch?v=Htq9jtiBNkc',
    # 'https://music.youtube.com/watch?v=lOlsNirDi08',
    # 'https://music.youtube.com/watch?v=rsJLHVNfEP0',
    # 'https://music.youtube.com/watch?v=ipIItONK98M',
    # 'https://music.youtube.com/watch?v=Dz73u3-mtbo',
    # 'https://music.youtube.com/watch?v=Gm5v9l2rQoE',
    # 'https://music.youtube.com/watch?v=9-zsJUoIfjk',
    # 'https://music.youtube.com/watch?v=3eBeKpeufI0',
    # 'https://music.youtube.com/watch?v=fivG7FT0LYE',
    # 'https://music.youtube.com/watch?v=6cDBQb1kXQ0',
    # 'https://music.youtube.com/watch?v=WNworBfljKk',
    # 'https://music.youtube.com/watch?v=8cjq0x8ajfU',
    # 'https://music.youtube.com/watch?v=GrFWXMw2Y0c',
    # 'https://music.youtube.com/watch?v=6-fqpVj044c',
    # 'https://music.youtube.com/watch?v=wqdxhrr4pqQ',
    # 'https://music.youtube.com/watch?v=v0NzDq6wq78',
    'https://www.youtube.com/watch?v=wOv5574-EPU',
    'https://www.youtube.com/watch?v=DVUyJ02wQxs'
]

def download_videos_as_lossless(urls, format_type="flac"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,        
        'audioquality': 0,           
        'outtmpl': '%(title)s.%(ext)s', 
        'postprocessors': [{
            'key': 'FFmpegExtractAudio', 
            'preferredcodec': format_type,
            'preferredquality': '0',   
        }],
        'quiet': False, 
        'ffmpeg_location': r"C:\ffmpeg\bin", 
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            print(f"Downloading: {url}")
            ydl.download([url])

if __name__ == '__main__':
    download_videos_as_lossless(video_urls, format_type="flac")
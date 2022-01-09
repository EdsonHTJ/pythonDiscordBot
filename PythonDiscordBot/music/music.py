import youtube_dl
import discord

FFMPMEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

async def getVideoInfo(url):
    YDL_OPTIONS = {'format': "bestaudio"}        
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        try:
            info = ydl.extract_info(url, download= False)
        except:
            info = ydl.extract_info(f"ytsearch:{url}", download=False)['entries'][0]


    url2 = info['formats'][0]['url']
    
    source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPMEG_OPTIONS)

    return info, source
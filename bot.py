import discord
from discord.ext import commands
from discord.ext.commands.core import command
import youtube_dl
from pycoingecko import CoinGeckoAPI
import asyncio
from threading import Thread

from random import randint

class music(commands.Cog):


    def __init__(self, client):
        self.client = client
        self.urlQueue = []
        self.FFMPMEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}


    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("no one in voice channel")
        
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def queue(self, ctx, *inputs):
        url = ''.join(inputs)
        await self.addItemToQueue(ctx, url)

    @commands.command()
    async def frita(self, ctx, *inputs):

        url = ''.join(inputs)
        await self.join(ctx)

        if url == '':
            self.playNextVideo(ctx)
            return

        await self.addItemToQueue(ctx, url)

        if  ctx.voice_client.is_playing() == 0:
            self.playNextVideo(ctx= ctx)

    async def addItemToQueue(self, ctx, url):
        info, source = await self.getVideoInfo(url)
        self.urlQueue.append( (info, source) )

        await ctx.send(f"Added -> {info.get('title', None)}")

    def playNextVideo(self, ctx):
        if len(self.urlQueue) == 0:
            return
        
        info, source = self.urlQueue[0]
        self.urlQueue = self.urlQueue[1:]
        self.playVideo(ctx, info, source)

    def playVideo(self, ctx, info , source):
        
        vc = ctx.voice_client
        vc.stop()        

        video_title = info.get('title', None)
        video_id = info.get("id", None)

        print(f"playing: {video_title} \nhttps://www.youtube.com/watch?v={video_id}")

        #await ctx.send(f"playing: {video_title} \nhttps://www.youtube.com/watch?v={video_id}")

        vc.play(source, after = lambda _: self.playNextVideo(ctx) )
        
 

    def send(self, ctx, message):
        print("teste2")
        td =  Thread(target=asyncio.run, args=(send(ctx,"some text"),))
        td.start()


    @commands.command()
    async def skip(self, ctx):
        await self.playNextVideo(ctx)

    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("Paused")

    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send("resumed")

    @commands.command()
    async def alyson(self, ctx):
        await ctx.send("CLUBISTA MASTER")

    @commands.command()
    async def corno(self, ctx):
        channel = self.client.get_channel(ctx.author.voice.channel.id)
        vm = channel.members
        await ctx.send(f"Existem {len(vm)} possiveis cornos")
        for member in vm:
            await ctx.send(member.mention)

        ri = randint(0, len(vm) - 1)
        await ctx.send(f"mas {vm[ri].mention} sem duvida é o maior deles")

    @commands.command()
    async def coin(self, ctx, *kwargs):
        coin = kwargs[0]
        if(len(kwargs) < 2):
            vsc = 'usd'
        else:
            vsc = kwargs[1]

        cg = CoinGeckoAPI()
        price = cg.get_price(ids = coin, vs_currencies = vsc)
        await ctx.send(price)

    async def getVideoInfo(self, url):
        YDL_OPTIONS = {'format': "bestaudio"}        
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info(url, download= False)
            except:
                info = ydl.extract_info(f"ytsearch:{url}", download=False)['entries'][0]


        url2 = info['formats'][0]['url']
        
        source = await discord.FFmpegOpusAudio.from_probe(url2, **self.FFMPMEG_OPTIONS)

        return info, source


def setup(client):
    client.add_cog(music(client))


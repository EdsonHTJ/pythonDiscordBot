import discord
from discord import message
from discord.ext import commands
from discord.ext.commands.core import command
from music.music import getVideoInfo
from pycoingecko import CoinGeckoAPI
from battleRoyale.battle import BattleRoyale
import asyncio
from threading import Thread
import time


from random import randint

class bot(commands.Cog):


    def __init__(self, client):
        self.client = client
        self.urlQueue = []
        self.br = BattleRoyale()
        self.hidePlay = False

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
    async def play(self, ctx, *inputs):

        url = ''.join(inputs)
        await self.join(ctx)

        if url == '':
            self.playNextVideo(ctx)
            return

        await self.addItemToQueue(ctx, url)

        if  ctx.voice_client.is_playing() == 0:
            self.playNextVideo(ctx= ctx)

    async def addItemToQueue(self, ctx, url):
        info, source = await getVideoInfo(url)
        self.urlQueue.append( (info, source) )

        if not self.hidePlay:
            await ctx.send(f"Added -> {info.get('title', None)}")

    def playNextVideo(self, ctx):

        if len(self.urlQueue) == 0:
            ctx.voice_client.stop()
            return

        info, source = self.urlQueue[0]
        self.urlQueue = self.urlQueue[1:]
        self.playVideo(ctx, info, source)

    def playVideo(self, ctx, info , source):
        
        vc = ctx.voice_client
        vc.stop()        

        video_title = info.get('title', None)
        video_id = info.get("id", None)

        if not self.hidePlay:
            self.send(ctx, f"playing: {video_title} \nhttps://www.youtube.com/watch?v={video_id}")

        print(f"playing: {video_title} \nhttps://www.youtube.com/watch?v={video_id}")

        #await ctx.send(f"playing: {video_title} \nhttps://www.youtube.com/watch?v={video_id}")

        vc.play(source, after = lambda _: self.playNextVideo(ctx) )

    def send(self, ctx, message):
        try:
            loop = asyncio.get_event_loop()
            loop.create_task(ctx.send(message))
        except:
            pass

    @commands.command()
    async def skip(self, ctx):
        ctx.send("Skipping Video")
        self.playNextVideo(ctx)

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
        await ctx.send(f"{coin.title()}: {price[coin][vsc]} {vsc.upper()}")

    @commands.command()
    async def br(self, ctx, *args):
        arg = args[0]

        if arg == "new":
            await ctx.send("New beto Real Game")
            self.br = BattleRoyale()
        elif arg == "add":

            if len(args) < 2:
                await ctx.send("inform player")
                return

            names = args[1:]
            for name in names:
                self.br.addPlayer(name)
        
        elif arg == "run":
            lines = self.br.run()
            for line in lines:
                time.sleep(3)
                if("colour" in line):
                    embed = discord.Embed(colour = line["colour"], description = line["message"])
                else:
                    embed = discord.Embed(description = line)
                if("img_url" in line):
                    embed.set_image(url = line["img_url"])
                if("footer" in line):
                    embed.set_footer(text = line["footer"]["text"], icon_url = line["footer"]["icon_url"])
                if("music" in line):
                    self.hidePlay = True
                    await self.join(ctx)
                    if  ctx.voice_client.is_playing():
                        ctx.voice_client.stop()
                    await self.play(ctx, line["music"])
                    self.hidePlay = False
                
                await ctx.send(embed = embed) 




def setup(client):
    client.add_cog(bot(client))


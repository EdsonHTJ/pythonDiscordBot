import discord
from discord.ext import commands
from discord.ext.commands.core import command
import youtube_dl
from random import randint

class music(commands.Cog):
    def __init__(self, client):
        self.client = client

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
    async def frita(self, ctx, *inputs):

        url = ''.join(inputs)

        await self.join(ctx)
        ctx.voice_client.stop()
        FFMPMEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format': "bestaudio"}
        vc = ctx.voice_client
        
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info(url, download= False)
            except:
                info = ydl.extract_info(f"ytsearch:{url}", download=False)['entries'][0]

            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPMEG_OPTIONS)
            vc.play(source)

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

        ri = randint(0, len(vm))
        await ctx.send(f"mas {vm[ri].mention} sem duvida é o maior deles")

        





def setup(client):
    client.add_cog(music(client))
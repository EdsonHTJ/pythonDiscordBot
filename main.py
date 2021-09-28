import discord
from discord.ext import commands
from discord.ext.commands import cog
from discord.flags import Intents
import bot

cogs = [bot]

apikey = open("./APIKEY.txt","r").read()
     
client = commands.Bot(command_prefix='?', Intents= discord.Intents.all)

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run(apikey)
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import os

Client = discord.Client()
Client = commands.bot(command_prefix = "lmao!")


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Prefix is lmao!'))
        print('launched')

@client.command 
async def count(ctx):
    print('Counting to 1 trillion idk why lol')
    if ctx.message.author.server_permissions.administrator:
        a = 0
        for i in range(0, 1000000000000):
        a = a + 1
        print(a)
        await client.say(a)
        else:
        a = 0
        for i in range(0, 1000000000000):
        a = a + 1
        print(a)
        await client.say(a)

client.run(os.getenv("TOKEN"))

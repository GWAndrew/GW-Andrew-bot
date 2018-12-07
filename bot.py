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

@client.event
async def on_message(message):
	if "Trillion List Count LMAO xD 123456789" in message.content.upper():
		a = 0
		while a != 123456789:
			await client.send_message(message.channel, a)
			a = a + 1
            
client.run(os.getenv("TOKEN"))

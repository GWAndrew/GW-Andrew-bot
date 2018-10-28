import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "a!")
@client.event
async def on_ready():
	print ("Connected")
	await client.change_presence(game = discord.Game(name="Prefix : a!"))

@client.event
async def on_message(message):
	if message.content.upper() == ('OOF'):
		msg = 'ARE YOU A DOG'
		await client.send_message(message.channel, msg)
				
client.run(os.getenv('TOKEN'))

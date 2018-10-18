import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk
import random
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "a!")
@client.event
async def on_ready():
	print ("Connected")
	await client.change_presence(game = discord.Game(name="Testing"))

@client.event
async def on_message(message):
	if message.content.starswith('oof')
	msg = 'ARE YOU A DOG'
	await client.send_message(message.channel, msg)

client.run(os.getenv('NDk1Mjk1NDIxODIwODI5Njk2.DqpVTg.yhX5_SDVtSgt3NZsT9XQM6TjUJk'))

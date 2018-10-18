import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk
import random
import time
import os


bot = commands.Bot(command_prefix='a!')

@bot.event
async def on_ready():
    print ("Connected")

@bot.event
async def on_message(message):
    if message.content == "a!random":
        random_number = random.randint(0,1000)
        await bot.send_message(message.channel,random_number)

















bot.run(os.getenv('TOKEN'))

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import random
import time
import json


os.system('color 0A')


bot = commands.Bot(command_prefix = "s!")
@bot.event
async def on_ready():
	print ("Connected")


@bot.event
async def on_member_join(member):

	channel = bot.get_channel("531157558828990504")
	await bot.send_message(channel, "Welcome on my server, I hope you will have a nice day here, Not forget to read the rules :wink: {} :joy:". format(member.mention))
	print ("Nouveau membre : {}".format(member))

	role = discord.utils.get(member.server.roles, name="™️Members™️")
	await bot.add_roles(member, role)
	print ("Role Members a été ajouté à : {}".format(member))



@bot.event
async def on_message(message):
	await bot.process_commands(message)
       
bot.run(os.getenv("TOKEN"))

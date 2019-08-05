import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import random
import time
import json

bot = commands.Bot(command_prefix = "a!")

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
	print ("Role Members as been added to : {}".format(member))

@bot.event
async def on_member_remove(member):
	channel = bot.get_channel("531157558828990504")
	await bot.send_message(channel, "{} Just leave the server, good bye :confused:". format(member))

@bot.event
async def on_message(message):
	await bot.process_commands(message)
		
@bot.command(pass_context = True)
async def ping(ctx):
    resp = await bot.say('Ping :')
    diff = resp.timestamp - ctx.message.timestamp
    await bot.say(f"{1000*diff.total_seconds():.1f}ms")
    print ("Ping")

	
	
@bot.command(pass_context=True)
async def gay(ctx, arg1):
	#sadly the bot detector doesnt work yet I have to fix this code lol
	user=arg1
	if user is not bot.user:
		random_number=random.randint(0,100)
		random_color=random.choice(color_list)
		embed=discord.Embed(title=":gay_pride_flag: GAY RATE :gay_pride_flag:",description="{} IS {}% GAY".format(arg1, random_number), color=random_color)
		msg = await ctx.bot.say(embed=embed)
		print("{}% GAY".format(random_number))
		loop = 0
		while loop < 50:
			random_color=random.choice(color_list)
			embed=discord.Embed(title=":gay_pride_flag: GAY RATE :gay_pride_flag:",description="{} IS {}% GAY".format(arg1, random_number), color=random_color)
			await ctx.bot.edit_message(msg,embed=embed)
			loop=loop+1
			await asyncio.sleep(1)
	else:
		embed=discord.Embed(title=":gay_pride_flag: GAY RATE :gay_pride_flag:",description="ARE BOTS GAY TOO ? :thinking:", color=0x62cee5)



@gay.error
async def gay_on_error(error,ctx):
	random_number=random.randint(0,100)
	random_color=random.choice(color_list)
	embed=discord.Embed(title=":gay_pride_flag: GAY RATE :gay_pride_flag:",description="{}, YOU ARE {}% GAY".format(ctx.message.author,random_number), color=random_color)
	msg = await bot.say(embed=embed)
	print("{}% GAY".format(random_number))
	loop = 0
	while loop < 10:
		random_color=random.choice(color_list)
		embed=discord.Embed(title=":gay_pride_flag: GAY RATE :gay_pride_flag:",description="{}, YOU ARE {}% GAY".format(ctx.message.author,random_number), color=random_color)
		await bot.edit_message(msg,embed=embed)
		loop=loop+1
		await asyncio.sleep(2)


       
bot.run(os.getenv("TOKEN"))


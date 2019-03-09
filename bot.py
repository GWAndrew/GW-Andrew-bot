import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import random
import time
import json
from time import sleep

bot = commands.Bot(command_prefix = "s!")

@bot.event
async def on_ready():
	print ("Le bot est online")

@bot.event
async def on_member_join(member):

	channel = bot.get_channel("535522119401078784")
	await bot.send_message(channel, "Bienvenu(e) sur le serveur de Spar_Trike :smile: Mais je te conseil de d'abord lire les regles {} :joy:". format(member.mention))
	print ("Nouveau membre : {}".format(member))

	role = discord.utils.get(member.server.roles, name="GirlZ and BoyZ")
	await bot.add_roles(member, role)
	print ("Role GirlZ and BoyZ a été ajouté à : {}".format(member))

	with open("users.json", "r") as f:
		users = json.load(f)

	await update_data(users, member)

	with open("users.json", "w") as f:
		json.dump(users, f)

async def update_data(users, user):
	if not user.id in users:
		users[user.id]= {}
		users[user.id]["experience"] = 0
		users[user.id]["level"] = 1

async def add_experience(users, user, exp):
	users[user.id]["experience"] += exp

async def level_up(users, user, channel):
	experience = users[user.id]["experience"]
	lvl_start = users[user.id]["level"]
	level = users[user.id]["level"]
	lvl_end_first = 250
	lvl_end = int(lvl_end_first * ((level+level)*1.5))

	if experience >= lvl_end:
		level = level + 1
		await bot.send_message(channel, "{} a augmenter au level {}".format(user.mention, level))
		print ("{} a augmenter au level {}".format(user.mention, level))
		users[user.id]["level"] = level

async def say_rank(users, user, channel):
	experience = users[user.id]["experience"]
	level = users[user.id]["level"]
	await bot.send_message(channel, "XP : {} ; LEVEL : {}".format(experience, level))

async def got_role_xp(users, user, member):
	level = users[user.id]["level"]
	int(level)
	if level >= 5:
		role = discord.utils.get(member.server.roles, name="Les ptits bros")
		await bot.add_roles(member, role)

	if level >= 15:
		role = discord.utils.get(member.server.roles, name="Les Maîtres")
		await bot.add_roles(member, role)

	if level >= 30:
		role = discord.utils.get(member.server.roles, name="Les seigneurs youtubes")
		await bot.add_roles(member, role)

@bot.event
async def on_message(message):
	if message.content.upper() == ('SPARTRIKE'):
		await bot.send_message(message.channel, "Spartrike c'est le sang :100: :fire:")
		print ("Spartrike c'est le sang :100: :fire:")

	with open("users.json", "r") as f:
		users = json.load(f)

	if message.author != bot.user:
		await update_data(users, message.author)
		await add_experience(users, message.author, random.randint(15,25))
		await level_up(users, message.author,message.channel)
	else :
		pass

	with open("users.json", "w") as f:
		json.dump(users, f)

	if message.content.upper() == ("S!RANK"):
		await say_rank(users, message.author,message.channel)

	if message.content == message.content:
		await got_role_xp(users, message.author, message.author)

	await bot.process_commands(message)

@bot.command(pass_context = True)
async def ping(ctx):
    resp = await bot.say('Ping du bot :')
    diff = resp.timestamp - ctx.message.timestamp
    await bot.say(f"{1000*diff.total_seconds():.1f}ms")
    print ("Ping :", f"{1000*diff.total_seconds():.1f}ms")

@bot.command(pass_context = True)
async def effacer(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount)):
    	messages.append(message)
    await bot.delete_messages(messages)

bot.run(os.getenv("TOKEN"))

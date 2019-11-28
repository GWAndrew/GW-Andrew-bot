import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import random
import time
import json

#colors
color_list = [0xff0000,0x00ff00,0xffff00,0x0000ff,0xff00ff,0x00ffff,0xffffff]

#poop pics
poop_pics=["https://miro.medium.com/max/1050/1*p_f8-fZS6VBeVzLWK-RXqw.png",
"http://cdn.shopify.com/s/files/1/1061/1924/products/Poop_Emoji_7b204f05-eec6-4496-91b1-351acc03d2c7_grande.png?v=1480481059",
"https://static.fnac-static.com/multimedia/Images/69/69/BA/9F/10467945-1505-1540-1/tsp20181206124851/Horloge-Emoji-Caca-Poop.jpg",
"https://s7.orientaltrading.com/is/image/OrientalTrading/13798019?$PDP_VIEWER_IMAGE$",
"https://cdn.shopify.com/s/files/1/1102/7446/products/NKX12948-Gold-The-Poop-Emoji-Necklace_1100x.jpg?v=1540190890",
"https://www.petpooskiddoo.com/wp-content/uploads/2015/09/perfect_poop.png"]


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
		if user.id=="504973571211132930":
			random_number==100
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

@bot.command()
async def poop():
	e = discord.Embed(color=0x663300)
	print ("poop sent")
	e.set_image(url=random.choice(poop_pics))
	await bot.say(embed=e)

		
		
#COLOR ROLES
#Black
@bot.command(pass_context=True)
async def black(ctx):
	user = ctx.message.author
	role = discord.utils.get(user.server.roles, name="Black")
	if "black" in [y.name.lower() for y in ctx.message.author.roles]:
		await bot.remove_roles(user,role)
		embed=discord.Embed(title="{}, COLOR REMOVED : BLACK".format(ctx.message.author), color=0x000001)
		await bot.say(embed=embed)
	else :
		await bot.add_roles(user, role)
		embed=discord.Embed(title="{}, COLOR ADDED : BLACK".format(ctx.message.author), color=0x000001)
		await bot.say(embed=embed)





#White
@bot.command(pass_context=True)
async def white(ctx):
	user = ctx.message.author
	role = discord.utils.get(user.server.roles, name="White")
	if "white" in [y.name.lower() for y in ctx.message.author.roles]:
		await bot.remove_roles(user,role)
		embed=discord.Embed(title="{}, COLOR REMOVED : WHITE".format(ctx.message.author), color=0xffffff)
		await bot.say(embed=embed)
	else :
		await bot.add_roles(user, role)
		embed=discord.Embed(title="{}, COLOR ADDED : WHITE".format(ctx.message.author), color=0xffffff)
		await bot.say(embed=embed)






#Blue
@bot.command(pass_context=True)
async def blue(ctx):
	user = ctx.message.author
	role = discord.utils.get(user.server.roles, name="blue")
	if "blue" in [y.name.lower() for y in ctx.message.author.roles]:
		await bot.remove_roles(user,role)
		embed=discord.Embed(title="{}, COLOR REMOVED : BLUE".format(ctx.message.author), color=0x0000ff)
		await bot.say(embed=embed)
	else :
		await bot.add_roles(user, role)
		embed=discord.Embed(title="{}, COLOR ADDED : BLUE".format(ctx.message.author), color=0x0000ff)
		await bot.say(embed=embed)





#Cyan
@bot.command(pass_context=True)
async def cyan(ctx):
	user = ctx.message.author
	role = discord.utils.get(user.server.roles, name="Cyan")
	if "cyan" in [y.name.lower() for y in ctx.message.author.roles]:
		await bot.remove_roles(user,role)
		embed=discord.Embed(title="{}, COLOR REMOVED : CYAN".format(ctx.message.author), color=0x00ffff)
		await bot.say(embed=embed)
	else :
		await bot.add_roles(user, role)
		embed=discord.Embed(title="{}, COLOR ADDED : CYAN".format(ctx.message.author), color=0x00ffff)
		await bot.say(embed=embed)






#Green
@bot.command(pass_context=True)
async def green(ctx):
	user = ctx.message.author
	role = discord.utils.get(user.server.roles, name="Green")
	if "green" in [y.name.lower() for y in ctx.message.author.roles]:
		await bot.remove_roles(user,role)
		embed=discord.Embed(title="{}, COLOR REMOVED : GREEN".format(ctx.message.author), color=0x00ff00)
		await bot.say(embed=embed)
	else :
		await bot.add_roles(user, role)
		embed=discord.Embed(title="{}, COLOR ADDED : GREEN".format(ctx.message.author), color=0x00ff00)
		await bot.say(embed=embed)








#Yellow
@bot.command(pass_context=True)
async def yellow(ctx):
	user = ctx.message.author
	role = discord.utils.get(user.server.roles, name="Yellow")
	if "yellow" in [y.name.lower() for y in ctx.message.author.roles]:
		await bot.remove_roles(user,role)
		embed=discord.Embed(title="{}, COLOR REMOVED : YELLOW".format(ctx.message.author), color=0xffff00)
		await bot.say(embed=embed)
	else :
		await bot.add_roles(user, role)
		embed=discord.Embed(title="{}, COLOR ADDED : YELLOW".format(ctx.message.author), color=0xffff00)
		await bot.say(embed=embed)






#Orange
@bot.command(pass_context=True)
async def orange(ctx):
	user = ctx.message.author
	role = discord.utils.get(user.server.roles, name="Orange")
	if "orange" in [y.name.lower() for y in ctx.message.author.roles]:
		await bot.remove_roles(user,role)
		embed=discord.Embed(title="{}, COLOR REMOVED : ORANGE".format(ctx.message.author), color=0xff6600)
		await bot.say(embed=embed)
	else :
		await bot.add_roles(user, role)
		embed=discord.Embed(title="{}, COLOR ADDED : ORANGE".format(ctx.message.author), color=0xff6600)
		await bot.say(embed=embed)





#Red
@bot.command(pass_context=True)
async def red(ctx):
	user = ctx.message.author
	role = discord.utils.get(user.server.roles, name="Red")
	if "red" in [y.name.lower() for y in ctx.message.author.roles]:
		await bot.remove_roles(user,role)
		embed=discord.Embed(title="{}, COLOR REMOVED : RED".format(ctx.message.author), color=0xff0000)
		await bot.say(embed=embed)
	else :
		await bot.add_roles(user, role)
		embed=discord.Embed(title="{}, COLOR ADDED : RED".format(ctx.message.author), color=0xff0000)
		await bot.say(embed=embed)





#pink
@bot.command(pass_context=True)
async def pink(ctx):
	user = ctx.message.author
	role = discord.utils.get(user.server.roles, name="Pink")
	if "pink" in [y.name.lower() for y in ctx.message.author.roles]:
		await bot.remove_roles(user,role)
		embed=discord.Embed(title="{}, COLOR REMOVED : PINK".format(ctx.message.author), color=0xfc2670)
		await bot.say(embed=embed)
	else :
		await bot.add_roles(user, role)
		embed=discord.Embed(title="{}, COLOR ADDED : PINK".format(ctx.message.author), color=0xfc2670)
		await bot.say(embed=embed)




		
@bot.command(pass_context=True)
async def dm(ctx):
	user=await bot.get_user_info("428516895919046667")
	await bot.send_message(user, "SUKA BLYAT")
	print("spam")
	await asyncio.sleep(1)
	
    # This works ^


		

       
bot.run(os.getenv("TOKEN"))


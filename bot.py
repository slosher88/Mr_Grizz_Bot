#bot.py

import os
import discord

from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client)) 

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startswith('!mr_grizz'):
		if message.content[10:].upper() == 'ARE YOU HOT?' or  message.content[10:].upper() == 'ARE YOU HOT':
			
			await message.channel.send('I am decidedly not hot.')
		else:
			await message.channel.send('Mr_Grizz_Bot smiles and nods')


client.run(TOKEN)

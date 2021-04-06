import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix = ';')

client = discord.Client()

@client.event
async def on_ready():
  print('Logged into {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == discord.user:
    return


  if message.content == ';credits':
    await message.channel.send('Credits to RiverChannel#0001')

    if message.author == discord.user:
      return

  if message.content == ';source':
    await message.channel.send('Source Code is not available.')

  if message.author == discord.user:
    return

  if message.content == ';version':
    await message.channel.send('Bot is in version 0.0.1')

  if message.content == ';help':

    myEmbed = discord.Embed(title="Commands", description="All commands for RiverBot", color=0x00ff00)
    myEmbed.add_field(name=";version", value="Shows the version the bot is in", inline=False)
    myEmbed.add_field(name=";source", value="Source Code for RiverBot", inline=False)
    myEmbed.add_field(name=";credits", value="Credits for RiverBot", inline=False)
  
    await message.channel.send(embed=myEmbed)



keep_alive()
client.run(os.getenv('TOKEN'))

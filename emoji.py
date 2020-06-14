import discord
from discord.ext import commands
import requests
import asyncio
import env
import config
import json

#Variables
client = commands.Client(command_prefix='Bot Prefix (Example: b;)')

  
@client.event
async def on_message(message):
  await message.add_reaction("😆")

  
 
client.run(env.TOKEN)

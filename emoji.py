import discord
from discord.ext import commands
import requests
import asyncio
import env
import json

#Variables
client = commands.Client(command_prefix='-')

  
@client.event
async def on_message(message):
  await message.add_reaction("😆")

  
 
client.run(env.TOKEN)

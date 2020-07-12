import random
import copy
import datetime
import random
import asyncio
from collections import Counter, defaultdict
import ast
import psutil
import platform
import cpuinfo
import time

import secrets
import sys, traceback

import sys, traceback
import random
import asyncio

import os
import asyncio
import inspect
import copy
import datetime
import random
import asyncio
from collections import Counter, defaultdict
import ast
import psutil

import time

import secrets
import sys, traceback

import sys, traceback
import random
import asyncio

import os
import asyncio
import inspect
from textwrap import dedent
from secrets import *
import re
import requests
import time
import html
import random
import ast
import env
import sys
import time
from collections import Counter, OrderedDict
from itertools import cycle
import json
import logging
import asyncio
import time
import datetime
import asyncio
import os
from discord import Game
import discord
from discord.ext import commands
import praw
import platform
from discord.ext.commands import CommandNotFound
import subprocess

messages = joined = 0





def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
        
    e = prefixes[str(message.guild.id)]
   
    return prefixes[str(message.guild.id)]

client=discord.AutoShardedClient()

client = commands.Bot(command_prefix=get_prefix, case_insensitive=True)
client.remove_command('help')




@client.event
async def on_member_join(member):
    global joined
    joined += 1


@client.event
async def on_message(message):
    global messages
    messages += 1

    await client.process_commands(message)

    
    
@client.command()
async def ping(ctx):
    try:
      t = time.time()
      await ctx.trigger_typing()
      t2 = round((time.time() - t) * 1000)
      start = time.perf_counter()
      embed = discord.Embed(title=f'Pinging...', description=f'', colour=0x2f3136)



      message = await ctx.send(embed=embed)
      await message.delete()
      end = time.perf_counter()
      duration = (end - start) * 100



      embed = discord.Embed(
            title=f'', description='' , colour=0x2f3136)

      embed.add_field(name="Client Ping:", value=f"{round(client.latency * 1000)}ms", inline=False)
      embed.add_field(name="API Latency:", value=f"{round(duration)}ms", inline=False)
      embed.add_field(name="Typing Delay:", value=f"{t2}ms", inline=False)

      msg = await ctx.send(embed = embed)
    except:
        embed = discord.Embed(
            title=f'The ping command had a error! Uh oh.', description="", colour=0x2f3136)

  
        msg = await ctx.send(embed = embed)

@commands.has_permissions(manage_messages=True)
@client.command(pass_context=True)
async def warn(ctx, member: discord.Member, *, note : str = None):
  try:
    if not member:
            embed=discord.Embed(title=f"Specify a member inside the server to warn", color=0x2f3136)
            await ctx.send(embed=embed)
    else:
      embed=discord.Embed(title="You have recieved a warning.", description="You were warned in **{0}** by **{1}**. Moderator note is `{2}`.".format(ctx.message.guild.name, ctx.message.author, note), color=0x2f3136)
      embed.set_thumbnail(url="https://images.emojiterra.com/twitter/512px/26a0.png")
      await member.send(embed=embed)
      embed=discord.Embed(title="Warning issued", color=0x2f3136)
      await ctx.send(embed=embed)
  except:
      embed=discord.Embed(title=f"There was a error with the `warn` command.", color=0x2f3136)
      await ctx.send(embed=embed)

@warn.error
async def warn_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
        title='Sorry.', description='You need the `manage_messages` permission to use this command.' , colour=discord.Colour.red())


        msg = await ctx.send(embed = embed)
        await msg.add_reaction("❌")

	
	
def get_uuid(username):
    try:
        r = requests.get(f'https://api.minetools.eu/uuid/{username}')
        j = r.json()
        return j['id']
    except Exception as e:
        return None




@client.command()
async def server(ctx: commands.Context, ip):
      try:
        url = f'https://api.mcsrvstat.us/2/{ip}'
        r = requests.get(url)
        j = r.json()
        embed: discord.Embed = discord.Embed(title=f'{ip}', color=0x2f3136)
        jkeys = j.keys()
        if 'version' in jkeys and len(j["version"]) > 1:
            embed.title += f' ({j["version"]})'

        embed.set_thumbnail(url=f'https://api.mcsrvstat.us/icon/{ip}')

        if 'motd' in jkeys and 'clean' in j['motd'].keys():
            embed.add_field(name='MOTD', value='\n'.join(j['motd']['clean']), inline=False)

        embed.add_field(name='Online: ', value=j['online'], inline=True)

        if 'players' in jkeys:
            players = j['players']
            print(players)
            embed.add_field(name='Slots', value=f'{players["online"]}/{players["max"]}', inline=True)
            if 'list' in players.keys():
                embed.add_field(name='Players', value=f'{", ".join(players["list"])}', inline=True)
        await ctx.send(embed=embed)
      except:
        await ctx.send("There was a error with the command.")




@client.command(helpinfo='Shows MC account info, skin and username history')
async def mcinfo(ctx, username='G3V'):
  try:	
    '''
    Shows MC account info, skin and username history
    '''
    uuid = requests.get('https://api.mojang.com/users/profiles/minecraft/{}'
                        .format(username)).json()['id']

    url = json.loads(base64.b64decode(requests.get(
        'https://sessionserver.mojang.com/session/minecraft/profile/{}'
        .format(uuid)).json()['properties'][0]['value'])
                     .decode('utf-8'))['textures']['SKIN']['url']
    
    names = requests.get('https://api.mojang.com/user/profiles/{}/names'
                        .format(uuid)).json()
    history = "\n"
    for name in reversed(names):
        history += name['name']+"\n"



    
    embed = discord.Embed(
            title=f"Username: `{username}`", description=f'UUID: {uuid}', colour=discord.Colour.blue())

    
    embed.add_field(name="**Name History**:", value=f"```{history}```", inline=False)
    embed.set_thumbnail(url=f'https://crafatar.com/renders/body/{get_uuid(username)}?overlay')
        


    await ctx.send(embed=embed)
  except:
    await ctx.send("There was a error.")
		
		


@client.command()
async def place(ctx: commands.Context, *, place):
      try:
        r = requests.get(f'https://www.metaweather.com//api/location/search/?query={place}')
        j = r.json()
        embed = discord.Embed(title="")
        embed.add_field(name="Name", value=f"`{j[0]['title']}`", inline=False)
        embed.add_field(name="Location Type", value=f"`{j[0]['location_type']}`", inline=False)
        embed.add_field(name="Latitude and Longitude", value=f"`{j[0]['latt_long']}`".replace(", ", "` `"), inline=False)
        await ctx.send(embed=embed)
      except:
        embed = discord.Embed(title="There was a error. Are you sure thats a city?")
        await ctx.send(embed=embed)




@client.command()
async def echo(ctx, *, text="Please include text."):
        await ctx.send(text.replace("@", "@ "))

	
	
import base64
import json
from typing import Union
from uuid import UUID
	


@client.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)


    prefixes[str(guild.id)] = "-"

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)


    prefixes.pop(str(guild.id))

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)


	
	
	

@client.command(aliases=["setprefix"])
async def changeprefix(ctx, prefix):
  if ctx.author.id == 229016449593769984 or ctx.author.id == 286591003794604034 or commands.has_permissions(manage_messages=True):
    try:
        embed = discord.Embed(
        title=f'Prefix was changed to `{prefix}` successfully.', description='' , colour=0x2f3136)

        msg = await ctx.send(embed = embed)
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)


        prefixes[str(ctx.guild.id)] = prefix

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)
    except:
        embed = discord.Embed(
        title=f'There was a error changing the prefix. ', description='' , colour=0x2f3136)

        msg = await ctx.send(embed = embed)
@changeprefix.error
async def changeprefix_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
        title='Sorry.', description='You need the `manage_messages` permission to use this command.' , colour=discord.Colour.red())


        msg = await ctx.send(embed = embed)
        await msg.add_reaction("❌")
    

import psutil
import time
import discord
import psutil
import time
import os
import copy
import aiohttp

def seconds_elapsed():
    return time.time() - psutil.boot_time()




@commands.has_permissions(manage_messages=True)
@client.command()
async def purge(ctx, amount=1000):
    m = await ctx.channel.purge(limit=amount+1)
    time.sleep(3)
    embed = discord.Embed(
        title=f":wastebasket: Successfully purged `{amount}` messages from the channel `{ctx.channel.name}`", description='' , colour=0x2f3136)

    m = await ctx.send(embed = embed)
    time.sleep(5)
    await m.delete()
@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
        title='Sorry.', description='You need the `manage_messages` permission to use this command.' , colour=discord.Colour.red())


        msg = await ctx.send(embed = embed)
        await msg.add_reaction("❌")

@commands.has_permissions(manage_messages=True)
@client.command()
async def mutebroken(ctx):
    embed = discord.Embed(
        title='', description=f'1 | **Are you sure there is a role called `Muted`.**\n2 | **{client.user.name} might not have permission to add roles to members.**\n3 | **The mute role might be higher than the bots roles, causing the bot to not be able to add the role.**' , colour=discord.Colour.red())

    embed.set_footer(text="If this didn't work you can type '-bug [text]' to report a bug")
    msg = await ctx.send(embed = embed)

			

			
			



@client.command()
async def ghstatus(ctx):
      embed = discord.Embed(title="Please wait..")
      m = await ctx.send(embed=embed)
      time.sleep(0)
      await m.delete()
      try:

        r = requests.get(f'https://kctbh9vrtdwd.statuspage.io/api/v2/status.json')
        j = r.json()
  
        b = requests.get(f'https://kctbh9vrtdwd.statuspage.io/api/v2/components.json')
        k = b.json()
  
        n = requests.get(f'https://kctbh9vrtdwd.statuspage.io/api/v2/incidents/unresolved.json')
        m = n.json()
  
    




        embed = discord.Embed(title=f"")
        embed.add_field(name="Github Status", value=f"`{j['status']['description']}`", inline=False)
        embed.add_field(name="API Status", value=f"`{k['components'][0]['status']}`".replace("operational", "Operational"), inline=False) 
        embed.add_field(name="Incidents", value=f"`{m['incidents']}`".replace("[]", "None"), inline=False) 

        await ctx.send(embed=embed)










        


        
      except Exception as e:
        embed = discord.Embed(title=f"Error: `{e}`")
        await m.edit(embed=embed)





@client.command()
async def dstatus(ctx):
      embed = discord.Embed(title="Please wait..")
      m = await ctx.send(embed=embed)
      time.sleep(0)
      await m.delete()
      try:

        r = requests.get(f'https://srhpyqt94yxb.statuspage.io/api/v2/status.json')
        j = r.json()
  
        b = requests.get(f'https://srhpyqt94yxb.statuspage.io/api/v2/components.json')
        k = b.json()
  
        n = requests.get(f'https://srhpyqt94yxb.statuspage.io/api/v2/incidents/unresolved.json')
        m = n.json()
  
    




        embed = discord.Embed(title=f"")
        embed.add_field(name="Discord Status", value=f"`{j['status']['description']}`", inline=False)
        embed.add_field(name="API Status", value=f"`{k['components'][0]['status']}`".replace("operational", "Operational"), inline=False) 
        embed.add_field(name="Incidents", value=f"`{m['incidents']}`".replace("[]", "None"), inline=False) 

        await ctx.send(embed=embed)










        


        
      except Exception as e:
        embed = discord.Embed(title=f"Error: `{e}`")
        await m.edit(embed=embed)
    
    
import wikipedia
import os
from chatbot import Chat, register_call	
			
			



@register_call("whoIs")
def who_is(query, session_id="general"):
    try:
        return wikipedia.summary(query)
    except Exception:
        for new_query in wikipedia.search(query):
            try:
                return wikipedia.summary(new_query)
            except Exception:
                pass
    return "I don't know about "+query
template_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"chatbotTemplate","chatbottemplate.template")
chat=Chat(template_file_path)
@client.command(pass_context = True, aliases=["chat", "ai"])
async def chatbot(ctx,*,message):
    embed = discord.Embed(
        title=f'Processing..', description='' , colour=0x2f3136)
    embed.set_footer(text="If this is still showing run the command again.")


    m = await ctx.send(embed = embed)
    result = chat.respond(message)
    if(len(result)<=2048):
        embed=discord.Embed(title="ChatBot", description = result, color = (0x2f3136))
        await m.edit(embed=embed)
    else:
        embedList = []
        n=2048
        embedList = [result[i:i+n] for i in range(0, len(result), n)]
        for num, item in enumerate(embedList, start = 1):
            if(num == 1):
                embed = discord.Embed(title="ChatBot", description = item, color = (0x2f3136))
                embed.set_footer(text="Page {}".format(num))
                await m.edit(embed = embed)
            else:
                embed = discord.Embed(description = item, color = (0x2f3136))
                embed.set_footer(text = "Page {}".format(num))
                await m.edit(embed = embed)
			
			
    
@client.event
async def on_message(message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
        
    e = prefixes[str(message.guild.id)]
    if message.author.bot:
        return
    if client.user in message.mentions: 
        embed = discord.Embed(
        title='', description=f'Prefix: `{e}`' , colour=discord.Colour.blurple())

        
   
        await message.channel.send(embed = embed)
    await client.process_commands(message)
   
@client.command()
async def bug(ctx, *, something):
  try:
    channel = client.get_channel(718531451876016209)
    embed = discord.Embed(
    title='Bug Report', description=f'Sent by `{ctx.author.name}#{ctx.author.discriminator}` on the server `{ctx.guild.name}`' , colour=discord.Colour.blue())

    
    embed.add_field(name='Message', value=f'`{something}`', inline=False)


    await channel.send(embed = embed)
    embed = discord.Embed(
    title='Bug Report Sent', description=f'' , colour=discord.Colour.blue())

    
    embed.add_field(name='Message', value=f'`{something}`', inline=False)


    await ctx.send(embed = embed)
  except: 
      embed = discord.Embed(
        title='', description=f'There was a error with the bug command. Did you include text?' , colour=discord.Colour.red())


      msg = await ctx.send(embed = embed)
        

@commands.has_permissions(manage_roles=True)
@client.command()
async def roles(ctx: commands.Context):
    try:
        roles = [f'{role.name}: {len(role.members)}' for role in sorted(await ctx.guild.fetch_roles(), reverse=True) if
                 role.name != '@everyone']
        embed=discord.Embed(description='\n'.join(roles), color=0x2f3136)
        embed.set_footer(text=f"{len(ctx.guild.roles)} in total")
        await ctx.send(embed=embed)
    except:
        embed=discord.Embed(description='The roles command had a error.', color=0x2f3136)
        await ctx.send(embed=embed)
@roles.error
async def roles_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
        title='Sorry.', description='You need the `manage_messages` permission to use this command.' , colour=discord.Colour.red())


        msg = await ctx.send(embed = embed)
        await msg.add_reaction("❌")

        
        


@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member=None):
  try:  
    if not member:
        embed = discord.Embed(
        title='', description='Please specify a member to mute.' , colour=discord.Colour.red())


        msg = await ctx.send(embed = embed)
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    embed = discord.Embed(
    title='', description=f'{member.mention} has been muted.' , colour=discord.Colour.green())


    msg = await ctx.send(embed = embed)
  except:
      embed = discord.Embed(
        title='', description=f'There was a error with the `mute` command. Please type `{ctx.prefix}muterole` to create a role.' , colour=discord.Colour.green())


      msg = await ctx.send(embed = embed)
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
        title='Sorry.', description='You need the `manage_messages` permission to use this command.' , colour=discord.Colour.red())


        msg = await ctx.send(embed = embed)
        await msg.add_reaction("❌")

        
        
@commands.has_permissions(manage_messages=True)
@client.command()
async def muterole(ctx):
  try: # creates muted role 
            embed = discord.Embed(
               title='', description=f'Creating role..' , colour=discord.Colour.green())


            msg = await ctx.send(embed = embed)  
            muted = await ctx.guild.create_role(name="Muted", reason="Used for muting members.")
            for channel in ctx.guild.channels: # removes permission to view and send in the channels 
                await channel.set_permissions(muted, send_messages=False,
                                              read_message_history=False,
                                              read_messages=False) 
            time.sleep(0)
            await msg.delete()
  except discord.Forbidden:
    embed = discord.Embed(
        title='', description=f'I have no permissions to make a `Muted` role.' , colour=discord.Colour.red())


    return await ctx.send(embed = embed)

    
  embed = discord.Embed(
        title='', description=f'The role `Muted` has been created. You can now mute members.' , colour=discord.Colour.green())


  await ctx.send(embed = embed)
@muterole.error
async def muterole_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
        title='Sorry.', description='You need the `manage_messages` permission to use this command.' , colour=discord.Colour.red())


        msg = await ctx.send(embed = embed)
        await msg.add_reaction("❌")


@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member=None):
  try:  
    if not member:
        embed = discord.Embed(
          title='', description='Please specify a member to mute.' , colour=discord.Colour.red())


        msg = await ctx.send(embed = embed)
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role)
    embed = discord.Embed(
        title='', description=f'{member.mention} has been unmuted.' , colour=discord.Colour.green())


    msg = await ctx.send(embed = embed)
  except:
      embed = discord.Embed(
        title='', description=f'Maybe the member was already muted. But the `unmute` command had a error.' , colour=discord.Colour.red())


      msg = await ctx.send(embed = embed)

	
                
@client.command(aliases=["nlradio", "nextlr","nlevelr"])
async def nlr(ctx: commands.Context):	

      
      embed = discord.Embed(title="Please wait..")
      m = await ctx.send(embed=embed)
      time.sleep(0)
			
		

      try:	
						
  					
        r = requests.get(f'http://nlradio.xyz/api/nowplaying/2')
        j = r.json()	
	
        dj = f'{str(datetime.timedelta(seconds=j["now_playing"]["duration"]))}'.replace("0:00:00", f"{j['live']['streamer_name']}")
        img = f'{j["now_playing"]["song"]["art"]}'


        embed = discord.Embed(title=f"Next Level Radio Information")
        embed.set_thumbnail(url=f"{img}")
        embed.add_field(name="> Listeners", value=f"Total: `{j['listeners']['total']}`\nUnique: `{j['listeners']['unique']}`\n", inline=False)
        embed.add_field(name="> Now Playing", value=f'{j["now_playing"]["song"]["text"]} `[{str(datetime.timedelta(seconds=j["now_playing"]["duration"]))}]`'.replace("0:00:00", f"{j['live']['streamer_name']} is Live"), inline=False)
        embed.add_field(name="> Up Next", value=f'{j["playing_next"]["song"]["text"]} `[{str(datetime.timedelta(seconds=j["playing_next"]["duration"]))}]`', inline=False)	
							   


        await m.edit(embed=embed)
      except Exception as e:
        embed = discord.Embed(title=f"Error: `{e}`")
        await m.edit(embed=embed)	
				
				




			
						
	

					      
@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
        title='Sorry.', description='You need the `manage_messages` permission to use this command.' , colour=discord.Colour.red())


        msg = await ctx.send(embed = embed)
        await msg.add_reaction("❌")



        await channel.send(embed=embed)



import googletrans
from googletrans import Translator



translator = Translator()

@commands.guild_only()
@client.command()
async def translate(ctx, *, translation):
  try:
    translator = Translator()
    result = translator.translate(translation)

    embed = discord.Embed(title=f"", description=f"")
    embed.add_field(name=f"Translation | :flag_{result.src}:".replace(":flag_en:", ":england:"), value=f"```{result.text}```", inline=False)

    await ctx.send(embed=embed)
  except Exception as e:
    embed = discord.Embed(title=f"Error: `{e}`")
    await ctx.send(embed=embed)


import subprocess
import logzero
from logzero import logger


@client.command()
async def pingip(ctx, *, ping="google.com"):
  if ctx.author.id == 286591003794604034 or ctx.author.id == 229016449593769984:
    try: 
      embed = discord.Embed(
        title='', description=f"Pinging..", colour=discord.Colour.blurple())


      m = await ctx.send(embed = embed)
  
      logzero.logfile("logfile.log", maxBytes=1e6, backupCount=3, disableStderrLogger=False)
 
      out = subprocess.run(['ping', f'{ping}'], capture_output=True)
      output = out.stdout.decode()
      await m.delete()
      embed = discord.Embed(
        title='', description=f"```h\n{output}```", colour=discord.Colour.blurple())


      msg = await ctx.send(embed = embed)
    except:
      embed = discord.Embed(
        title='', description=f"Error!", colour=discord.Colour.red())


      msg = await ctx.send(embed = embed)
  else:
    await ctx.send("Your not the owner!")

  

import subprocess
import logzero
from logzero import logger


@client.command()
async def pull(ctx):
  if ctx.author.id == 286591003794604034 or ctx.author.id == 229016449593769984:
    try: 
      embed = discord.Embed(
        title='', description=f"Pulling..", colour=discord.Colour.blurple())


      m = await ctx.send(embed = embed)
  
      logzero.logfile("logfile2.log", maxBytes=1e6, backupCount=3, disableStderrLogger=False)
 
      out = subprocess.run(['git', f'pull'], capture_output=True)
      output = out.stdout.decode()
      await m.delete()
      embed = discord.Embed(
        title='', description=f"```h\n{output}```", colour=discord.Colour.blurple())


      msg = await ctx.send(embed = embed)
    except:
      embed = discord.Embed(
        title='', description=f"Error!", colour=discord.Colour.red())


      msg = await ctx.send(embed = embed)
  else:
    await ctx.send("Your not the owner.")

@client.command()
async def console(ctx, *, hi):
  if ctx.author.id == 229016449593769984 or ctx.author.id == 286591003794604034:
    try:
      text = f"{hi}".replace(" ", "', '").replace("ipconfig", "no")
      embed = discord.Embed(
        title='', description=f"Processing..", colour=discord.Colour.blurple())


      m = await ctx.send(embed = embed)
  
      logzero.logfile("logfile3.log", maxBytes=1e6, backupCount=3, disableStderrLogger=False)
 
      out = subprocess.run([f'{text}'], capture_output=True, shell=True)
      output = out.stdout.decode()
      await m.delete()
      embed = discord.Embed(
        title='', description=f"```h\n{output}```", colour=discord.Colour.blurple())

      msg = await ctx.send(embed = embed)
    except Exception as e:
      embed = discord.Embed(
        title='Error!', description=f"{e}", colour=discord.Colour.red())


      msg = await ctx.send(embed = embed)
  else:
    embed = discord.Embed(
        title='Forbidden', description=f"Your not the owner.", colour=discord.Colour.red())


    msg = await ctx.send(embed = embed)

    
    
   


@client.event
async def on_ready():
    
    url = "https://wumpusbots.com/api/bot/718205517054476320/stats"
    payload = {"serverCount": f"{len(client.guilds)}", "shardCount": "1"}
    headers = {"authorization": 'XA-gTypCy2SoQfGOcb4LJo5pN5q'}
    r = requests.post(url, data=payload, headers=headers)
    print("[+] Wumpusbots.com")
    
    url = "https://discordbots.org/api/bots/718205517054476320/stats"
    payload = {"server_count": f"{len(client.guilds)}", "shard_count": "1"}
    headers = {"Authorization": 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjcxODIwNTUxNzA1NDQ3NjMyMCIsImJvdCI6dHJ1ZSwiaWF0IjoxNTkyODIyOTg5fQ.okYwlEcS3ZIqnCVayf-RQWOe0e1vnxVmE8mTHLJ4f_k'}
    r = requests.post(url, data=payload, headers=headers)
    print("[+] Top.gg\n")
    
    url = "https://listmybots.com/api/bot/718205517054476320"
    payload = {"server_count": f"{len(client.guilds)}", "shardCount": "1"}
    headers = {"Authorization": 'b3d3763ba5e0cda10471fd5c3c04a001e68ca627423ad664e25c4775b648fec267d1f0152d5bcbb5c941ae46cd131d35c082f1a1318b4fd28130e8b2c30ab367'}
    r = requests.post(url, data=payload, headers=headers)
    print("[+] Listmybots.com\n")
    
    print("Bot is online! Cool!")
    print(f"Logged in as {client.user.name} ({client.user.id})")
    await client.change_presence(activity=discord.Game(name=f"with moderation stuff"), status=discord.Status.idle)


@commands.is_owner()
@client.command()
async def banner(ctx):
    embed = discord.Embed(
       title='', description='', colour=0x2f3136)
    embed.set_image(url="https://cdn.discordapp.com/attachments/718213349615337521/718245744338796553/SetsudoBANNER.png")
    m = await ctx.send(embed=embed)


@client.command(aliases=["pass"])
async def password(ctx, nbytes: int = 18):
    try:
        if nbytes not in range(3, 1401):
            embed = discord.Embed(title="Error!", description="I only accept any numbers between `3-1400`", color=0x2f3136)
            return await ctx.send(embed=embed)
        if hasattr(ctx, 'guild') and ctx.guild is not None:
            embed = discord.Embed(title="", description=f"I've randomly generated a password and sent it to your private messages, {ctx.author.mention}", color=0x2f3136)
            await ctx.send(embed=embed)
            embed = discord.Embed(title="Here is your password:", description=f"{secrets.token_urlsafe(nbytes)}", color=0x2f3136)
            await ctx.author.send(embed=embed)
        else:
            embed = discord.Embed(title="Error!", description="Thats not a number?", color=0x2f3136)
            await ctx.send(embed=embed)
    except:
        embed = discord.Embed(title="Error!", description="It seems your private messages are disabled.", color=0x2f3136)
        await ctx.send(embed=embed)


@commands.is_owner()
@client.command()
async def prefixes(ctx):
        file = open('prefixes.json', 'r')
        await ctx.send(file=discord. File('prefixes.json'))



@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member = None):
    try:
        if not member:
            embed=discord.Embed(title=f"Specify a member inside the server to kick", color=0x2f3136)
            await ctx.send(embed=embed)
            return
        await member.kick()
        embed=discord.Embed(title=f"`{member.name}` has been kicked from `{ctx.guild.name}`", color=0x2f3136)
        await ctx.send(embed=embed)
    except:
        embed=discord.Embed(title=f"That member has equal or higher permissions to me.", color=0x2f3136)
        await ctx.send(embed=embed)
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
        title='Sorry.', description='You need the `kick_members` permission to use this command.' , colour=discord.Colour.red())


        msg = await ctx.send(embed = embed)
        await msg.add_reaction("❌")

@commands.has_permissions(ban_members=True)
@client.command()
async def unban(ctx, *, member="f"):
  try:
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
      user = ban_entry.user

      if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        embed = discord.Embed(
          title=f"Unbanned the user `{user.name}#{user.discriminator}`", description="", colour=0x2f3136)


        msg = await ctx.send(embed = embed)

  except:
    embed = discord.Embed(
          title="You didn't do the name right. ", description="`Usage: unban [name]#[discriminator]`", colour=discord.Colour.red())


    msg = await ctx.send(embed = embed)
@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
        title='Sorry.', description='You need the `ban_members` permission to use this command.' , colour=discord.Colour.red())


        msg = await ctx.send(embed = embed)
        await msg.add_reaction("❌")



@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member = None):
    try:
        if not member:
            embed=discord.Embed(title=f"Specify a member inside the server to ban", color=0x2f3136)
            await ctx.send(embed=embed)
            return
        await member.ban()
        embed=discord.Embed(title=f"`{member.name}` has been banned from `{ctx.guild.name}`", color=0x2f3136)
        await ctx.send(embed=embed)
    except:
        embed=discord.Embed(title=f"That member has equal or higher permissions to me.", color=0x2f3136)
        await ctx.send(embed=embed)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
        title='Sorry.', description='You need the `ban_members` permission to use this command.' , colour=discord.Colour.red())


        msg = await ctx.send(embed = embed)
        await msg.add_reaction("❌")@client.command()
        
@commands.has_permissions(ban_members=True)
@client.command()
async def softban(ctx, member:discord.Member = None):
    try:
        if not member:
            embed=discord.Embed(title=f"Specify a member inside the server to ban", color=0x2f3136)
            await ctx.send(embed=embed)
            return
        await member.ban()
        await member.unban()
        embed=discord.Embed(title=f"`{member.name}` has been softbanned from `{ctx.guild.name}`", color=0x2f3136)
        await ctx.send(embed=embed)
    except:
        embed=discord.Embed(title=f"That member has equal or higher permissions to me.", color=0x2f3136)
        await ctx.send(embed=embed)

@softban.error
async def softban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
        title='Sorry.', description='You need the `ban_members` permission to use this command.' , colour=discord.Colour.red())


        msg = await ctx.send(embed = embed)
        await msg.add_reaction("❌")


@client.command()
async def test(ctx):
  if ctx.author.id == 286591003794604034 or ctx.author.id == 229016449593769984:
    embed = discord.Embed(
       title='Pulling..', description='', colour=random.randint(0, 0xFFFFFF))

    m = await ctx.send(embed=embed)
    os.system("git pull")
    time.sleep(0)
    embed = discord.Embed(
       title='Pulled from github', description='', colour=random.randint(0, 0xFFFFFF))

    await m.edit(embed=embed)
@pull.error
async def pull_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
          title='Forbidden', description='This command is owner only.' , colour=discord.Colour.red())



        msg = await ctx.send(embed = embed)
        await msg.add_reaction("❌")
      
    
    






@client.command(pass_context=True, aliases=["r"])
async def reload(ctx):
    if ctx.author.id == 286591003794604034 or ctx.author.id == 229016449593769984:
        embed = discord.Embed(
           title='Reloading commands', description='This can take 6 seconds or more', colour=random.randint(0, 0xFFFFFF))
  
        m = await ctx.send(embed=embed)
        os.system("python run.py")
    
        time.sleep(0.2) # 200ms to CTR+C twice
@reload.error
async def reload_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
        title='Forbidden', description='This command is owner only.' , colour=discord.Colour.red())


        msg = await ctx.send(embed = embed)
        await msg.add_reaction("❌")  






@client.command()
async def fix(ctx):
  if ctx.author.id == 286591003794604034 or ctx.author.id == 229016449593769984:
    embed = discord.Embed(
       title='Fixing `Pull` command.', description='', colour=random.randint(0, 0xFFFFFF))

    m = await ctx.send(embed=embed)
    os.system("git fetch --all")
    os.system("git reset --hard origin/master")
    time.sleep(0)
    embed = discord.Embed(
       title='`Pull` command is fixed', description='', colour=random.randint(0, 0xFFFFFF))

    await m.edit(embed=embed)
@fix.error
async def fix_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
          title='Forbidden.', description='This command is owner only.' , colour=discord.Colour.red())

        msg = await ctx.send(embed = embed)
        await msg.add_reaction("❌")

        
        
        
@client.command(aliases=["si"])
async def serverinfo(ctx):
		"""Show various information about the server."""

		guild = ctx.guild

		desc = dict(
			ID=guild.id,
		)

		e = discord.Embed(
			title=guild.name,
			description='\n'.join('**{}**: {}'.format(key, value) for key, value in desc.items()),
			timestamp=guild.created_at
		)

		e.add_field(
			name='Owner',
			value=guild.owner
		)

		e.add_field(
			name='Region',
			value=str(guild.region)
		)

		# CHANNELS

		channels = {
			discord.TextChannel: 0,
			discord.VoiceChannel: 0,
		}

		for channel in guild.channels:
			for channel_type in channels:
				if isinstance(channel, channel_type):
					channels[channel_type] += 1

		channel_desc = '{} {}\n{} {}'.format(
			'📨',
			channels[discord.TextChannel],
			'🔊',
			channels[discord.VoiceChannel]
		)

		e.add_field(
			name='Channels',
			value=channel_desc
		)
    


		# FEATURES

		if guild.features:
			e.add_field(
				name='Features',
				value='\n'.join('• ' + feature.replace('_', ' ').title() for feature in guild.features)
			)

    

 
    

		# MEMBERS

		statuses = dict(
			online=0,
			idle=0,
			dnd=0,
			offline=0
		)

		total_online = 0

		for member in guild.members:
			status_str = str(member.status)
			if status_str != "offline":
				total_online += 1
			statuses[status_str] += 1

		member_desc = '{} {} {} {} {} {} {} {}'.format(
			'<:online:714584789880930366>',
			statuses['online'],
			'<:idle:714584789880930426>',
			statuses['idle'],
			'<:offline:714584790019604541>',
			statuses['dnd'],
			'◾',
			statuses['offline']
		)

		e.add_field(
			name='Members ({}/{})'.format(total_online, len(guild.members)),
			value=f"{member_desc}", inline=False
		)

		# SERVER BOOST

		boost_desc = '<:booster:717514418514034828> Level {} - {} Boosts'.format(guild.premium_tier, guild.premium_subscription_count)




		e.add_field(
			name='Server boost',
			value=boost_desc
		)
   

		e.set_thumbnail(url=guild.icon_url)
		e.set_footer(text='Created')

		await ctx.send(embed=e)  
        
        
        
        
        
        
        
      
@client.command(aliases=["ui"])
async def userinfo(ctx, member: discord.Member = None):
  if not member:
    embed = discord.Embed(
        title='Information', description='')
    embed.add_field(name="> User Information", value=f"**❯**  Profile: {ctx.author.mention} `[{ctx.author.name}#{ctx.author.discriminator}]`\n**❯**  ID: `{ctx.author.id}`\n**❯**  Status: `{ctx.author.status}`\n**❯**  Bot?: {ctx.author.bot}\n**❯**  Joined Discord: `{ctx.author.created_at.strftime('%A, %B %d %Y @ %H:%M:%S %p')}`\n**❯**  Joined Guild: `{ctx.author.joined_at.strftime('%A, %B %d %Y @ %H:%M:%S %p')}`".replace('False', ':x:').replace('True', ':white_check_mark:'), inline=False)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.send(embed=embed) 
  else:
    embed = discord.Embed(
        title='Information', description='')
    embed.add_field(name="> User Information", value=f"**❯**  Profile: {member.mention} `[{member.name}#{member.discriminator}]`\n**❯**  ID: `{member.id}`\n**❯**  Status: `{member.status}`\n**❯**  Bot?: {member.bot}\n**❯**  Joined Discord: `{member.created_at.strftime('%A, %B %d %Y @ %H:%M:%S %p')}`\n**❯**  Joined Guild: `{member.joined_at.strftime('%A, %B %d %Y @ %H:%M:%S %p')}`".replace('False', ':x:').replace('True', ':white_check_mark:'), inline=False)
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed) 

@client.command(aliases=["ci"])
async def channelinfo(ctx, channel: discord.TextChannel = None):
  if not channel:
    embed = discord.Embed(
      title='Channel Information', description='')
    
    embed.add_field(name="> Main Information", value=f"**❯**  Channel Name: `{ctx.channel.name}`\n**❯**  ID: `{ctx.channel.id}`\n**❯**  Created at: `{ctx.channel.created_at.strftime('%A, %B %d %Y @ %H:%M:%S %p')}`\n**❯** Category: `{ctx.channel.category}`\n**❯** NSFW?: `{ctx.channel.is_nsfw()}`\n**❯** Position: `{ctx.channel.position}` out of `{len(ctx.guild.channels)}`", inline=False)


    await ctx.send(embed=embed)
  else:
    embed = discord.Embed(
      title='Channel Information', description='')
    
    embed.add_field(name="> Main Information", value=f"**❯**  Channel Name: `{channel.name}`\n**❯**  ID: `{channel.id}`\n**❯**  Created at: `{channel.created_at.strftime('%A, %B %d %Y @ %H:%M:%S %p')}`\n**❯** Category: `{channel.category}`\n**❯** NSFW?: `{channel.is_nsfw()}`\n**❯** Position: `{channel.position}` out of `{len(ctx.guild.channels)}`", inline=False)


    await ctx.send(embed=embed)

                    
                    
@client.command()
async def info(ctx):
  """Shows this message."""
  embed = discord.Embed(
    title=f'Information Commands', description=f'', colour=0xcccccc)

  embed.add_field(name="channelinfo", value=f"Gives info about a channel.", inline=False)                
  embed.add_field(name="userinfo", value=f"Gives info about a user.", inline=False)
  embed.add_field(name="serverinfo", value=f"Gives info about the server.", inline=False)

  await ctx.send(embed=embed)               


@client.command()
async def dev(ctx):
  """Shows this message."""
  embed = discord.Embed(
    title=f'Developer Commands', description=f'', colour=0xcccccc)

  embed.add_field(name="Fix", value=f"Fixes the `Pull` command.", inline=False)
  embed.add_field(name="Pull", value=f"Pulls changes from github.", inline=False)
  embed.add_field(name="Reload", value=f"Reloads all commands.", inline=False)
  embed.add_field(name="Eval", value=f"Evaluates code.", inline=False)
  embed.add_field(name="Pingip", value=f"Pings a ip address.", inline=False)
  embed.add_field(name="Console", value=f"Runs a command in console.", inline=False)
  await ctx.send(embed=embed)




@client.command(pass_context=True, aliases=["stats", "botinfo"])
async def botstatus(ctx):

    start = time.perf_counter()
    message = await ctx.send('Pinging...')
    await message.delete()
    end = time.perf_counter()
    duration = (end - start) * 100
    embed=discord.Embed(title="**Setsudo** Stats ", color=0x2f3136)
    embed.add_field(name="<:python:717405551637561587> Python", value=(f"{platform.python_version()}"), inline=True)
    embed.add_field(name='<:discordpy:717404880632938536> Discord.py', value=f"{discord.__version__}", inline=True)
    embed.add_field(name="Bot latency", value=("{} ms (ws: {} ms)".format(round(duration), round(client.latency * 1000))), inline=False)
    embed.add_field(name="Users", value=(f"{len(client.users)}"), inline=True)
    embed.add_field(name="Guilds", value=(f"{len(client.guilds)}"), inline=True)
    embed.add_field(name="Shards", value=(f"{client.shard_count}"), inline=True)
    embed.add_field(name="CPU", value="{}%".format(round(psutil.cpu_percent())), inline=False)
    embed.add_field(name="RAM usage", value="{}% | {} / {}mb".format(round(psutil.virtual_memory().percent), round(psutil.virtual_memory().used/1048576), round(psutil.virtual_memory().total/1048576)), inline=True)

    
    await ctx.send(embed=embed)



@client.command()
async def useful(ctx):
    embed = discord.Embed(
    title=f'Useful Commands', description=f'', colour=0xcccccc)

    embed.add_field(name="Ping", value=f"Shows the bot latency.", inline=False)
    embed.add_field(name="Stats", value=f"Show information about the bot.", inline=False)
    embed.add_field(name="Setprefix", value=f"Changes the bots prefix.", inline=False)
    embed.add_field(name="Password", value=f"Generates a random password.", inline=False)
    embed.add_field(name="Dstatus", value=f"Shows the status of discord.", inline=False)
    embed.add_field(name="Ghstatus", value=f"Shows the status of github.", inline=False)
    embed.add_field(name="Place", value=f"Information about a place.", inline=False)
    embed.add_field(name="Translate", value=f"Translates text using google translate.", inline=False)
    embed.add_field(name="covid", value=f"Stats about covid-19.", inline=False)
    await ctx.send(embed=embed)
		 
		    
@client.command(aliases=["coronavirus", "corona","covid"])
async def cov(ctx: commands.Context):	

      
      embed = discord.Embed(title="Please wait..")
      m = await ctx.send(embed=embed)
      time.sleep(0)
			
		

      try:	
						
  					
        r = requests.get(f'https://api.covid19api.com/summary')
        j = r.json()	
	
        total = "{:,}".format(j['Global']['TotalConfirmed'])
        TotalD = "{:,}".format(j['Global']['TotalDeaths'])
        TotalR = "{:,}".format(j['Global']['TotalRecovered'])
        
        new = "{:,}".format(j['Global']['NewConfirmed'])
        newD = "{:,}".format(j['Global']['NewDeaths'])
        NewR = "{:,}".format(j['Global']['NewRecovered'])


        embed = discord.Embed(title=f"Covid-19 Stats")
        embed.add_field(name="Total", value=f"Total Confirmed: `{total}`\nTotal Deaths: `{TotalD}`\nTotal Recovered: `{TotalR}`", inline=False)
        embed.add_field(name="New", value=f"New Confirmed: `{new}`\nNew Deaths: `{newD}`\nNew Recovered: `{NewR}`", inline=False)
							   


        await m.edit(embed=embed)
      except Exception as e:
        embed = discord.Embed(title=f"Error: `{e}`")
        await m.edit(embed=embed)
		    
@client.command()
async def minecraft(ctx):
    embed = discord.Embed(
    title=f'Minecraft Commands', description=f'', colour=0xcccccc)
     
 
    embed.add_field(name="Server", value=f"Shows info about a server ip.", inline=False)
    embed.add_field(name="Mcinfo", value=f"Shows info about a user", inline=False)
   
    await ctx.send(embed=embed)
		    
		    
@client.command()
async def moderation(ctx):
    embed = discord.Embed(
    title=f'Moderation Commands', description=f'', colour=0xcccccc)
     
 
    embed.add_field(name="Ban", value=f"Bans a specified member.", inline=False)
    embed.add_field(name="Kick", value=f"Kicks a specified member.", inline=False)
    embed.add_field(name="Softban", value=f"Bans and Unbans a specified user.", inline=False)
    embed.add_field(name="Unban", value=f"Unbans a specified user.", inline=False)
    embed.add_field(name="Purge", value=f"Purges the chat.", inline=False)
    embed.add_field(name="Warn", value=f"Warns a specified member.", inline=False)
    embed.add_field(name="Mute", value=f"Mutes a specified member.", inline=False)
    embed.add_field(name="Unmute", value=f"Unmutes a specified member.", inline=False)
    embed.add_field(name="Muterole", value=f"Creates a muted role.", inline=False)
    embed.add_field(name="Roles", value=f"Lists all roles in the server.", inline=False)
    await ctx.send(embed=embed)

		    

		    
async def background_task():
    await client.wait_until_ready()
    url = "https://discordbots.org/api/bots/718205517054476320/stats"
    while not client.is_closed():
              try:
                payload = {"server_count": f"{len(client.guilds)}", "shard_count": "1"}
                headers = {"Authorization": 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjcxODIwNTUxNzA1NDQ3NjMyMCIsImJvdCI6dHJ1ZSwiaWF0IjoxNTkyODIyOTg5fQ.okYwlEcS3ZIqnCVayf-RQWOe0e1vnxVmE8mTHLJ4f_k'}
                r = requests.post(url, data=payload, headers=headers)
                print("Guild Count Posted")
                await asyncio.sleep(300) # task runs every 60 seconds
              except:
                print("Error! Retrying in 60 seconds.")
                await asyncio.sleep(60)
		    
		    
		    

@client.command()
async def help(ctx):
  embed = discord.Embed(
    title=f'Help command', description=f'', colour=0xcccccc)

  embed.add_field(name=f"{ctx.prefix}`moderation`".replace("<@!718205517054476320> ", "-"), value=f"Shows moderation commands.", inline=False)
  embed.add_field(name=f"{ctx.prefix}`useful`".replace("<@!718205517054476320> ", "-"), value=f"Shows useful commands", inline=False)
  embed.add_field(name=f"{ctx.prefix}`info`".replace("<@!718205517054476320> ", "-"), value=f"Shows info commands.", inline=False)
  embed.add_field(name=f"{ctx.prefix}`dev`".replace("<@!718205517054476320> ", "-"), value=f"Shows developer commands.", inline=False)
  embed.add_field(name=f"{ctx.prefix}`minecraft`".replace("<@!718205517054476320> ", "-"), value=f"Shows minecraft commands.", inline=False)

  await ctx.send(embed=embed)






@client.command(pass_context=True, name='eval')
async def _eval(ctx, *, code="You need to input code."):
  if ctx.author.id == 286591003794604034 or ctx.author.id == 229016449593769984:
    global_vars = globals().copy()
    global_vars['bot'] = client
    global_vars['ctx'] = ctx
    global_vars['message'] = ctx.message
    global_vars['author'] = ctx.message.author
    global_vars['channel'] = ctx.message.channel
    global_vars['server'] = ctx.message.guild

    try:
        result = eval(code, global_vars, locals())
        if asyncio.iscoroutine(result):
            result = await result
        result = str(result) # the eval output was modified by me but originally submitted by DJ electro
        embed=discord.Embed(title="Evaluated successfully.", color=0x80ff80)
        embed.add_field(name="**Input** :inbox_tray:", value="```py\n" + code + "```", inline=False)
        embed.add_field(name="**Output** :outbox_tray:", value=f"```diff\n+ {result}```".replace(f"{env.TOKEN}", "no ur not getting my token die"))
        await ctx.send(embed=embed)
    except Exception as error:
        embed=discord.Embed(title="Evaluation failed.", color=0xf7665f)
        embed.add_field(name="Input :inbox_tray:", value="```py\n" + code + "```", inline=False)
        embed.add_field(name="Error :interrobang: ", value='```diff\n- {}: {}```'.format(type(error).__name__, str(error)))
        await ctx.send(embed=embed)
        return
@_eval.error
async def _eval_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
          title='Forbidden', description='This command is owner only.' , colour=discord.Colour.red())


        msg = await ctx.send(embed = embed)
        await msg.add_reaction("❌")
	    
		    
client.loop.create_task(background_task())
client.run(env.TOKEN)

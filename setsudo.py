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
from datetime import datetime
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

async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")

            messages = 0
            joined = 0
 
            await asyncio.sleep(600)

        except Exception as e:
            print(e)
            await asyncio.sleep(600)




def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    
    
   
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
      embed = discord.Embed(title=f'', description=f'Pinging...', colour=0x2f3136)



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
            title=f'The ping command had a error!', description="", colour=0x2f3136)

  
        msg = await ctx.send(embed = embed)

@commands.has_permissions(manage_messages=True)
@client.command(pass_context=True)
async def warn(ctx, member: discord.Member, *, note : str = None):
  try:
    if not member:
            embed=discord.Embed(title=f"Specify a member inside the server to warn", color=0x2f3136)
            await ctx.send(embed=embed)
    else:
      embed=discord.Embed(title="You have recieved a warning.", description="You were warned in **{0}** by **{1}**. Moderator note is `{2}`.".format(ctx.message.guild.name, ctx.message.author, note), color=0x176cd5)
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



@client.command()
async def echo(ctx, *, text="Please include text."):
        await ctx.send(text.replace("@", "@ "))



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
async def changeprefix(ctx, *, prefix):
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


@client.command()
async def mutebroken(ctx):
    embed = discord.Embed(
        title='', description=f'1 | **Are you sure there is a role called `Muted`.**\n2 | **{client.user.name} might not have permission to add roles to members.**\n3 | **The mute role might be higher than the bots roles, causing the bot to not be able to add the role.**' , colour=discord.Colour.red())

    embed.set_footer(text="If this didn't work you can type '-bug [text]' to report a bug.")
    msg = await ctx.send(embed = embed)




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
        title='', description=f'There was a error with the `mute` command. Please type `{ctx.prefix}mutebroken` on ways to fix this.' , colour=discord.Colour.red())


      msg = await ctx.send(embed = embed)
@mute.error
async def mute_error(ctx, error):
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

@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
        title='Sorry.', description='You need the `manage_messages` permission to use this command.' , colour=discord.Colour.red())


        msg = await ctx.send(embed = embed)
        await msg.add_reaction("❌")



        await channel.send(embed=embed)
















@client.event
async def on_ready():
    url = "https://www.cloudlist.xyz/api/stats/718205517054476320"
    payload = {"count": f"{len(client.guilds)}"}
    headers = {"Authorization": '91d1ef2c1403da93000b23187'}
    r = requests.post(url, data=payload, headers=headers)
    print("[+] Posted count to: \n[+] Cloudlist.xyz")
    url = "https://wumpusbots.com/api/bot/718205517054476320/stats"
    payload = {"serverCount": f"{len(client.guilds)}", "shardCount": "1"}
    headers = {"authorization": 'XA-gTypCy2SoQfGOcb4LJo5pN5q'}
    r = requests.post(url, data=payload, headers=headers)
    print("[+] wumpusbots.com")
    url = "https://listmybots.com/api/bot/718205517054476320"
    payload = {"server_count": f"{len(client.guilds)}", "shardCount": "1"}
    headers = {"Authorization": 'b3d3763ba5e0cda10471fd5c3c04a001e68ca627423ad664e25c4775b648fec267d1f0152d5bcbb5c941ae46cd131d35c082f1a1318b4fd28130e8b2c30ab367'}
    r = requests.post(url, data=payload, headers=headers)
    print("[+] listmybots.com\n")
    print("Bot is online!")
    print(f"Logged in as {client.user.name} ({client.user.id})")
    await client.change_presence(activity=discord.Game(name=f"with my prefix '-' | -help"), status=discord.Status.idle)


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
        await msg.add_reaction("❌")



    
@commands.is_owner()
@client.command()
async def pull(ctx):
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
      
    
    
    
import subprocess
import logging

@commands.is_owner()
@client.command()
async def tt(ctx, *, tt):
  try:
    a  = os.popen("git pull").readlines()
    time.sleep(0)
    await ctx.send(a)
  except:
    await ctx.send("Error!")



@commands.is_owner()
@client.command(pass_context=True, aliases=["r"])
async def reload(ctx):
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






@commands.is_owner()
@client.command()
async def fix(ctx):
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
          title='Forbidden', description='This command is owner only.' , colour=discord.Colour.red())

        msg = await ctx.send(embed = embed)
        await msg.add_reaction("❌")







@client.command()
async def dev(ctx):
  """Shows this message."""
  embed = discord.Embed(
    title=f'Developer Commands', description=f'', colour=0xcccccc)

  embed.add_field(name="Fix", value=f"Fixes the `Pull` command.", inline=False)
  embed.add_field(name="Pull", value=f"Pulls changes from github.", inline=False)
  embed.add_field(name="Reload", value=f"Reloads all commands.", inline=False)
  embed.add_field(name="Eval", value=f"Evaluates code.", inline=False)
  await ctx.send(embed=embed)




@client.command(pass_context=True, aliases=["stats", "botinfo"])
async def botstatus(ctx):

    start = time.perf_counter()
    message = await ctx.send('Pinging...')
    await message.delete()
    end = time.perf_counter()
    duration = (end - start) * 100
    embed=discord.Embed(title="**Image Creator** Stats ", color=0x2f3136)
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
    embed.add_field(name="System", value=f"Setsudo's system status.", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def moderation(ctx):
    embed = discord.Embed(
    title=f'Moderation Commands', description=f'', colour=0xcccccc)

    embed.add_field(name="Ban", value=f"Bans a specified member.", inline=False)
    embed.add_field(name="Kick", value=f"Kicks a specified member.", inline=False)
    embed.add_field(name="Purge", value=f"Purges the chat.", inline=False)
    embed.add_field(name="Warn", value=f"Warns a specified member.", inline=False)
    embed.add_field(name="Mute", value=f"Mutes a specified member.", inline=False)
    embed.add_field(name="Unmute", value=f"Unmutes a specified member.", inline=False)
    embed.add_field(name="Roles", value=f"Lists all roles in the server.", inline=False)
    await ctx.send(embed=embed)


@client.command()
async def help(ctx):
  embed = discord.Embed(
    title=f'Help command', description=f'', colour=0xcccccc)

  embed.add_field(name=f"{ctx.prefix}`moderation`", value=f"Shows moderation commands.", inline=False)
  embed.add_field(name=f"{ctx.prefix}`useful`", value=f"Shows useful commands", inline=False)
  embed.add_field(name=f"{ctx.prefix}`dev`", value=f"Shows developer commands.", inline=False)

  await ctx.send(embed=embed)





@commands.is_owner()
@client.command(pass_context=True, name='eval')
async def _eval(ctx, *, code="You need to input code."):
  if ctx.author.id == 286591003794604034:
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

        
        
import psutil
import platform
from datetime import datetime
import cpuinfo



@client.command()
async def system(ctx):
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        content = discord.Embed(
            title="",
            colour=int("5dadec", 16),
            description="Grabbing System Info..",
        )
        m = await ctx.send(embed=content)
        time.sleep(0)
        system_uptime = time.time() - psutil.boot_time()
        mem = psutil.virtual_memory()
        pid = os.getpid()
        memory_use = psutil.Process(pid).memory_info()[0]

        data = [
            ("CPU Usage:", f"{psutil.cpu_percent()}%"),
            ("RAM Usage:", f"{mem.percent}%"),
            ("System Uptime:", f"{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"),
            ("CPU:", f"{cpuinfo.get_cpu_info()['brand']}")
        ]

        content = discord.Embed(
            title=":computer: System status",
            colour=int("5dadec", 16),
            description="\n".join(f"**{x[0]}** {x[1]}" for x in data),
        )
        await m.edit(embed=content)

client.loop.create_task(update_stats())
client.run(env.TOKEN)

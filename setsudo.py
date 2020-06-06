import random
import copy
import datetime
import random
import asyncio
from collections import Counter, defaultdict
import ast
import psutil

import time

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
import logging
import praw
import platform

def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)


    return prefixes[str(message.guild.id)]

client=discord.AutoShardedClient()

client = commands.Bot(command_prefix= get_prefix)
client.remove_command('help')


@client.command()
async def logs(ctx):
    test = logging.basicConfig(level=logging.INFO)#
    await ctx.send(test)





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
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)


    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)
    try:
        embed = discord.Embed(
        title=f'Prefix was changed to `{prefix}` successfully.', description='' , colour=0x2f3136)

        msg = await ctx.send(embed = embed)
    except:
        embed = discord.Embed(
        title=f'There was a error changing the prefix. ', description='' , colour=0x2f3136)

        msg = await ctx.send(embed = embed)

























































@client.event
async def on_ready():
    print("Bot is online!")
    print(f"Logged in as {client.user.name} ({client.user.id})")

start_time = datetime.datetime.utcnow() # Timestamp of when it came online

@client.command()
async def uptime(ctx):
    """Shows the bots uptime"""
    now = datetime.datetime.utcnow() # Timestamp of when uptime function is run
    delta = now - start_time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    if days:
        time_format = "{d} days, {h} hours, {m} minutes, and {s} seconds."
    else:
        time_format = "{h} hours, {m} minutes, and {s} seconds."
    uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
    embed = discord.Embed(
        title=f'', description='' , colour=0x2f3136)


  
    embed.set_author(name=f"{format(uptime_stamp)}", icon_url=ctx.author.avatar_url)


    msg = await ctx.send(embed = embed)

@commands.is_owner()
@client.command()
async def banner(ctx):
    embed = discord.Embed(
       title='', description='', colour=0x2f3136)
    embed.set_image(url="https://cdn.discordapp.com/attachments/718213349615337521/718245744338796553/SetsudoBANNER.png")
    m = await ctx.send(embed=embed)



@client.command()
@commands.has_permissions(administrator=True)
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
async def push(ctx):
    embed = discord.Embed(
       title='Pushing changes to github..', description='', colour=random.randint(0, 0xFFFFFF))

    m = await ctx.send(embed=embed)
    os.system("git push")
    time.sleep(0)
    embed = discord.Embed(
       title='Pushed changes to github', description='', colour=random.randint(0, 0xFFFFFF))

    await m.edit(embed=embed)

    
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


@commands.is_owner()
@client.command(pass_context=True)
async def reload(ctx):
        embed = discord.Embed(
           title='Reloading commands', description='', colour=random.randint(0, 0xFFFFFF))
  
        m = await ctx.send(embed=embed)
        embed = discord.Embed(
            title='Reloaded commands', description='', colour=random.randint(0, 0xFFFFFF))

        await m.edit(embed=embed)
        os.system("python run.py")
    
        time.sleep(0.2) # 200ms to CTR+C twice
  





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






@commands.is_owner()
@client.command()
async def dev(ctx):
  """Shows this message."""
  embed = discord.Embed(
    title=f'Developer Commands', description=f'', colour=0xcccccc)

  embed.add_field(name="Fix", value=f"Fixes the `Pull` command.", inline=False)
  embed.add_field(name="Pull", value=f"Pulls changes from github.", inline=False)
  embed.add_field(name="Push", value=f"Pushes changes to github.", inline=False)
  embed.add_field(name="Reload", value=f"Reloads all commands.", inline=False)
  embed.add_field(name="Eval", value=f"Evaluates code.", inline=False)
  await ctx.send(embed=embed)
@dev.error
async def dev_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
        title='No go away', description='Owner only' , colour=discord.Colour.red())


        msg = await ctx.send(embed = embed)
        await msg.add_reaction("❌")



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
    title=f'Moderation Commands', description=f'', colour=0xcccccc)

    embed.add_field(name="Ping", value=f"Shows the bot latency.", inline=False)
    embed.add_field(name="Uptime", value=f"Shows the bot uptime.", inline=False)
    embed.add_field(name="Stats", value=f"Show information about the bot.", inline=False)
    embed.add_field(name="Setprefix", value=f"Changes the bots prefix", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def moderation(ctx):
    embed = discord.Embed(
    title=f'Moderation Commands', description=f'', colour=0xcccccc)

    embed.add_field(name="Ban", value=f"Bans a specified member", inline=False)
    embed.add_field(name="Kick", value=f"Kicks a specified member", inline=False)
    await ctx.send(embed=embed)


@client.command()
async def help(ctx):
  embed = discord.Embed(
    title=f'Help command', description=f'', colour=0xcccccc)

  embed.add_field(name=f"{ctx.prefix}`moderation`", value=f"Shows moderation commands.", inline=False)
  embed.add_field(name=f"{ctx.prefix}`useful`", value=f"Shows useful commands", inline=False)
  embed.add_field(name=f"{ctx.prefix}`dev`", value=f"Shows developer commands.", inline=False)

  await ctx.send(embed=embed)



@client.command()
async def ping(ctx):
    """Sends the clients latency"""
    await ctx.send(f"Ping! ( `{round(client.latency * 1000)}ms` )")


@commands.is_owner()
@client.command(pass_context=True, name='eval')
async def _eval(ctx, *, code):
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



client.run(env.TOKEN)

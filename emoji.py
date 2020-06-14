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



client = commands.Bot(command_prefix = "img ")
client.remove_command('help')

  
@client.event
async def on_message(message):
  await message.add_reaction("😆")

  
 
client.run(env.TOKEN)

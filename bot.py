# bot.py
from asyncio import events
import os

import discord
from dotenv import load_dotenv

from discord.ext import commands, tasks
from datetime import timedelta, datetime

import json

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@tasks.loop(hours=12)
async def check_birthday():
    with open("/data/birthday.json", "r") as infile:
      data = json.load(infile)
    for key, value in data.items():
      dt = datetime.strptime(value, '%m/%d/%Y')
      new_dt = dt.replace(year=2021, hour=0, second=0, microsecond=0)
      today = datetime.today()
      new_today = today.replace(year=2021, hour=0, second=0, microsecond=0)
      if new_dt.date() == new_today.date():
        await bot.wait_until_ready()
        channel = bot.get_channel(198326359573921792)
        await channel.send(f"{key}'s birthday is today. Say happy birthday NOW!")

check_birthday.start()

@bot.command(name='birthday', help='Format should be: !birthday MM/DD/YYYY')
async def birthday(ctx, *, date):
    with open("/data/birthday.json", "r") as infile:
      data = json.load(infile)

    name=str(ctx.author)
    birthday=date

    try:
      dt = datetime.strptime(birthday, '%m/%d/%Y')
    except:
      await ctx.send("Enter a valid date dumby; do !help birthday")
      return

    if name in data:
      await ctx.send("You already have an entry iDioT!")
    else:
        data[name] = birthday
        await ctx.send(f"{name}'s birthday is: {birthday}")

    with open("/data/birthday.json", "w") as outfile:
      json.dump(data, outfile)

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.channel.send("50% SEA 50% WEED")    
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    await bot.wait_until_ready()
    channel = bot.get_channel(198326359573921792)
    await channel.send(f'{member.name} is HERE.')
    await member.send('Welcome to blinnigob nerd.')
    await bot.process_commands(member)


bot.run(TOKEN)

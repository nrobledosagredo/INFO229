import os

import discord
from dotenv import load_dotenv
from discord.ext import commands
from random import randrange

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "?" in message.content:
        n = randrange(7)
        if n == 0: response = "Tal vez algún día."
        if n == 1: response = "Nada."
        if n == 2: response = "Tampoco."
        if n == 3: response = "No lo creo."
        if n == 4: response  = "No."
        if n == 5: response = "Si."
        if n == 6: response = "Intenta preguntar de nuevo."
        await message.channel.send(response)

    await bot.process_commands(message)

bot.run(TOKEN)
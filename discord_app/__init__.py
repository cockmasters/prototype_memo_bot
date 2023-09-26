import logging

import discord
from discord.ext import commands
from discord.ext.commands import Context

from settings import bot_settings

config = {
    'token': bot_settings.TOKEN_DIS,
    'prefix': '/',
}

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=config['prefix'], intents=intents)


@bot.event
async def on_ready():
    logging.info("Бот дискорд готов!")


@bot.command()
async def hello(ctx: Context):
    await ctx.send('Привет')


@bot.command()
async def hello_a(ctx):
    await ctx.author.send(f'Привет, бро!')


bot.run(config['token'])

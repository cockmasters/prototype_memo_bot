import logging

import discord
from discord.ext import commands
from discord.ext.commands import Context

open('log.log', 'w').close()
logging.basicConfig(handlers=(logging.FileHandler('log.log'), logging.StreamHandler()),
                    level=logging.INFO
                    )
config = {
    'token': 'MTE1NTgxMDY2MjMyMTI0MjEzMg.GKD0UR.Ka-L5zFrUSVPcREY_BWUz_M9mIUiE_bvTdSiig',
    'prefix': '/',
}

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=config['prefix'], intents=intents)


@bot.event
async def on_ready():
    logging.info("Бот готов!")


@bot.command()
async def hello(ctx: Context):
    await ctx.send('Привет')


@bot.command()
async def hello_a(ctx):
    await ctx.author.send(f'Привет, бро!')


bot.run(config['token'])

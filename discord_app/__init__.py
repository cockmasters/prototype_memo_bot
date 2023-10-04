import logging

import discord
from discord import ButtonStyle
from discord.ext import commands
from discord.ext.commands import Context
from discord.ui import Button

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


@bot.command()
async def send_message_with_button(ctx):
    # Создание объекта сообщения
    message = await ctx.send("Нажмите на кнопку:", components=[
        discord.ui.Button(style=discord.ButtonStyle.primary, label="Нажми меня")
    ])

    # Ожидание нажатия кнопки
    interaction = await bot.wait_for("button_click", check=lambda i: i.component.label == "Нажми меня")

    # Отправка сообщения вместо кнопки
    await interaction.edit_origin(content="Кнопка была нажата!", components=[])


bot.run(config['token'])

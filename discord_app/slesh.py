import disnake
from disnake.ext import commands
from disnake.ext.commands import Context

from settings import bot_settings

intents = disnake.Intents.all()  # Подключаем все разрешения
bot = commands.Bot(command_prefix="!", intents=intents)  # Вместо 1234567890 указать id сервера


@bot.event
async def on_ready():
    print("Бот готов!")


@bot.command()
async def hello(ctx: Context):
    await ctx.send(f"Ваш текст: {ctx.message.content[6:]}")


bot.run(bot_settings.TOKEN_DIS)


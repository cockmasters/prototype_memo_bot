#  Данный код является расширенной версией предыдущего кода.

#  Импортируются необходимые модули
import os

import disnake
from disnake.ext import commands

from settings import bot_settings

#  Создается объект intents, который включает все разрешения для бота.
#  Создается экземпляр класса Bot с префиксом команд "!" и указанными разрешениями.
intents = disnake.Intents.all()  # Подключаем все разрешения
bot = commands.Bot(command_prefix="!", intents=intents, test_guilds=[123456789])  # Вместо 1234567890 указать id сервера


# Определяется функция on_ready, которая будет вызываться, когда бот будет готов к использованию.
# В данном случае, она просто выводит сообщение "Bot is ready!" в консоль.
@bot.event
async def on_ready():
    print("Bot is ready!")


@commands.command(name='verify')
async def verify(self, ctx):
    view = Verify_button()
    verify_embed = disnake.Embed(
        title='Верификация',
        description='Пройдите верификацию чтобы продолжить общение!'
    )
    await ctx.send(embed=verify_embed, view=view)


@disnake.ui.button(style=disnake.ButtonStyle.grey, label='Черный', row=1)
async def Black(self, button: disnake.Button, interaction: disnake.Interaction):
    Black = interaction.guild.get_role(1072561365438451743)
    if Black in interaction.user.roles:
        await interaction.user.remove_roles(Black)
        await interaction.response.send_message(f'{Black.mention} Успешно забрана', ephemeral=True)

    else:
        await interaction.user.add_roles(Black)
        await interaction.response.send_message(f'{Black.mention} Успешно присвоено', ephemeral=True)

# При готовности бота, загружает расширения из папки "cogs"
for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

# Запускается бот с помощью метода run, передавая ему токен для авторизации.
bot.run(bot_settings.TOKEN_DIS)

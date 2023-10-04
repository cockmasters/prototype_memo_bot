# Импортируем необходимые модули из библиотеки disnake.
import logging

import disnake
from disnake.ext import commands


# Определяем класс "ButtonView", который наследуется от disnake.ui.View.
class ButtonView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    # Создаем кнопку "button1" с соответствующей функцией-обработчиком.
    @disnake.ui.button(label="Кнопка", style=disnake.ButtonStyle.red, custom_id="button1")
    async def button1(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        # Получаем роль по ее ID (необходимо указать конкретный ID вместо ...).
        button.persistent_views_added = True
        print("Кнопка нажата!")
        # Отправляем ответ для показа, что бот обработал нажатие кнопки.
        await interaction.response.send_message('Проверка')
        await interaction.response.defer()


# Определяем класс "ButtonsRole", который является расширением (Cog) для бота.
class ButtonsRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.persistent_views_added = False

    # Создаем команду "buttons", которая будет выводить сообщение с кнопкой.
    @commands.command()
    async def buttons(self, ctx):
        view = ButtonView()

        # Получаем роль по ее ID (необходимо указать конкретный ID вместо ...).
        role = ctx.guild.get_role(...)

        embed = disnake.Embed(color=0x2F3136)
        embed.set_author(name="Мероприятия:")
        embed.description = f"\n\nПроверяем нажатие кнопки"
        embed.set_image(url="https://i.imgur.com/QzB7q9J.png")
        await ctx.send(embed=embed, view=view)

    # Создаем слушателя события "on_ready", который добавляет персистентную кнопку.
    @commands.Cog.listener()
    async def on_ready(self):
        if self.persistent_views_added:
            return

        # Message ID сообщения, где будет кнопка, добавляется после отправки команды.
        # Нужно будет скопировать ID сообщения и вставить вместо "...", после выполнения данных действий
        # необходимо перезапустить бота.
        self.bot.add_view(ButtonView(), message_id=...)


# Функция setup, которая добавляет класс ButtonsRole как Cog (команду-расширение) в бота.
def setup(bot):
    bot.add_cog(ButtonsRole(bot))

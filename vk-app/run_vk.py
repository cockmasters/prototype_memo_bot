from vkbottle import Keyboard, Text, KeyboardButtonColor
from vkbottle.bot import Bot, Message



bot = Bot(token="vk1.a.7_klp1JfZWkzyBFTk4-HxodzjhMwCW56DmiuRa0LeCky9V-yvB8nU8_2wcFzpeqedkmLMPc9tjluNMuWFJIv8zF8rtEEICtjSqrk4bS2vNoe4mKn32ZZy4AuNVTtF0ZBCMeB5nPheJUg36pCGUq6ucdL05AcespY1a47VdcH66yQwop7GgPJ5vFzCzehinpDevslQP8xt0ug9PweZwpRMg")


@bot.on.message(text="Привет")
async def hi_handler(message: Message):
    keyboard = (
        Keyboard(one_time=True, inline=False)
        .add(Text("Кнопка 1"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Кнопка 2"))
        .add(Text("Кнопка 3", payload={"command": 3}))
    ).get_json()

    await message.answer(
        message="Смотри сколько кнопок!!",
        keyboard=keyboard
    )
    users_info = await bot.api.users.get(message.from_id)
    await message.answer("Привет, {}".format(users_info[0].first_name))


bot.run_forever()

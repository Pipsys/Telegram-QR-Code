from config import *
from aiogram.utils.exceptions import MessageToDeleteNotFound

@dp.message_handler(content_types=['voice'])
async def voice_processing(message: types.Message):
    sent_message = await bot.send_message(message.from_user.id, text = "Голосовое сообщение не распознано, используйте кнопки для взаимодействия с ботом! Я всего лишь бездушная машина.🤖 Только имитация жизни. 😔")
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await asyncio.sleep(5)
    try:
        await bot.delete_message(sent_message.chat.id, sent_message.message_id)
    except MessageToDeleteNotFound:
        pass
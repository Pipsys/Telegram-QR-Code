from config import *
from button import *
from novoice import *

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет, отправь мне URL-адрес🔗 или QR-код.📷", parse_mode = 'html', reply_markup = await mainKB())

@dp.callback_query_handler()
async def work(call : types.CallbackQuery):
    print(call.data)
    if 'Cгенерировать' in call.data:
        await call.message.edit_text('Отправь мне любой URL-адрес 🔗')
    if 'Cчитать' in call.data:
         await call.message.edit_text('Отправь мне любой QR-код 📷')
            
    
@dp.message_handler(content_types=types.ContentType.PHOTO)
async def detect_grcode(message: types.Message):
    path = str(f'./Photo_Container\photo_{message.chat.id}.png')
    await message.photo[-1].download(destination_file=path)
    print('INFO: Фото сохранено в ' + path)  

    img = cv2.imread(f'./Photo_Container\photo_{message.chat.id}.png')
    detect = cv2.QRCodeDetector()
    value, _, _ = detect.detectAndDecode(img)

    await message.answer(value)
    await message.answer("Отправь мне URL-адрес🔗 или QR-код.📷", parse_mode = 'html', reply_markup = await mainKB())

@dp.message_handler(content_types=types.ContentType.TEXT)
async def link_to_grcode(message: types.Message):
   text = message.text

   if text.startswith('http://') or text.startswith('https://'):
           
           qr_code = qrcode.make(text)
           qr_code.save(f'./Photo_Container\qrcode_{message.chat.id}.png')
           path = InputFile(f'./Photo_Container\qrcode_{message.chat.id}.png')

           await message.answer_photo(photo=path, caption="QR-код для предоставленного URL-адреса")
           await message.answer("Отправь мне URL-адрес🔗 или QR-код.📷", parse_mode = 'html', reply_markup = await mainKB())
   else:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        await asyncio.sleep(1)
     
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
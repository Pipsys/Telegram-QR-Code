from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def mainKB():
    buttons = ['Cчитать QR код','Cгенерировать QR код']
    btn = [InlineKeyboardButton(button, callback_data=f'@qrcode_{button}')
            for button in buttons]
    inl_menu = InlineKeyboardMarkup(row_width=2).add(*btn)
    return inl_menu

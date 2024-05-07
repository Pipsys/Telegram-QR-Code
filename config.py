# pip install aiogram==2.15
# pip install opencv-python qrcode Pillow

import cv2
import qrcode
import logging
import asyncio

from aiogram.utils import executor
from aiogram import Bot, Dispatcher, types
from aiogram.types import InputFile 

from aiogram.contrib.middlewares.logging import LoggingMiddleware


TOKEN = 'token'
bot = Bot (token = TOKEN)
dp = Dispatcher (bot)

logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())
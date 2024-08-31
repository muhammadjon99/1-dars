from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from knopkalar import *
bottoken = '7351676892:AAHEz_FhqYMaokh0ROBc40p-OsCuwj3KuQs'
bot = Bot(bottoken)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='Botimizga Xush kelibsiz', reply_markup=asosiymenyu())

@dp.message_handler(text="Rasm jo'natish")

async def rasm(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='rasmni tanlang', reply_markup=rasmlar())

@dp.message_handler(text='1-rasm')
async def rasm(message: Message):
    chatid = message.chat.id
    rasm = open('1.png', 'rb')
    await bot.send_photo(chat_id=chatid, photo=rasm)

@dp.message_handler(text='2-rasm')
async def rasm(message: Message):
    chatid = message.chat.id
    rasm = open('images4.jpg', 'rb')
    await bot.send_photo(chat_id=chatid, photo=rasm)

@dp.message_handler(text='3-rasm')
async def rasm(message: Message):
    chatid = message.chat.id
    rasm = open('images5.jpg', 'rb')
    await bot.send_photo(chat_id=chatid, photo=rasm)

@dp.message_handler(text='4-rasm')
async def rasm(message: Message):
    chatid = message.chat.id
    rasm = open('python2.png', 'rb')
    await bot.send_photo(chat_id=chatid, photo=rasm)

@dp.message_handler(text='5-rasm')
async def rasm(message: Message):
    chatid = message.chat.id
    rasm = open('10011.jpg', 'rb')
    await bot.send_photo(chat_id=chatid, photo=rasm)

@dp.message_handler(text='⬅️ orqaga')
async def orqaga(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='asosiymenyu', reply_markup=asosiymenyu())

@dp.message_handler(text="Video jo'natish")
async def video(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='videoni tanlang', reply_markup=videolar())

@dp.message_handler(text='1-video')
async def video(message: Message):
    chatid = message.chat.id
    video = open('a.mp4', 'rb')
    await bot.send_video(chat_id=chatid, video=video)

@dp.message_handler(text='2-video')
async def video(message: Message):
    chatid = message.chat.id
    video = open('b.mp4', 'rb')
    await bot.send_video(chat_id=chatid, video=video)

@dp.message_handler(text='3-video')
async def video(message: Message):
    chatid = message.chat.id
    video = open('c.mp4', 'rb')
    await bot.send_video(chat_id=chatid, video=video)

@dp.message_handler(text='4-video')
async def video(message: Message):
    chatid = message.chat.id
    video = open('d.mp4', 'rb')
    await bot.send_video(chat_id=chatid, video=video)

@dp.message_handler(text='5-video')
async def video(message: Message):
    chatid = message.chat.id
    video = open('Sizda ta+.mp4', 'rb')
    await bot.send_video(chat_id=chatid, video=video)

@dp.message_handler(text='⬅️ orqaga')
async def orqaga(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='asosiymenyu', reply_markup=asosiymenyu())







executor.start_polling(dp, skip_updates=True)
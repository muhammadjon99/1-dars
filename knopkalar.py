from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup

def asosiymenyu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton(text="Rasm jo'natish"),
        KeyboardButton(text="Video jo'natish")
    )
    return markup

def rasmlar():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton(text='1-rasm'),
        KeyboardButton(text='2-rasm'),
        KeyboardButton(text='3-rasm'),
        KeyboardButton(text='4-rasm'),
        KeyboardButton(text='5-rasm'),
        KeyboardButton(text='⬅️ orqaga')

    )
    return markup

def videolar():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton(text='1-video'),
        KeyboardButton(text='2-video'),
        KeyboardButton(text='3-video'),
        KeyboardButton(text='4-video'),
        KeyboardButton(text='5-video'),
        KeyboardButton(text='⬅️ orqaga')
    )
    return markup
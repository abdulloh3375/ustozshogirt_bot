import sqlite3
import asyncio
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command
from aiogram.types import Message
import logging
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import F
from db import create_user, get_data
import re
connection = sqlite3.connect("data_ustoz.db")
kursor = connection.cursor()
PHONE_PATTERN = r"\+998[0-9]{9}"


logging.basicConfig(level=logging.INFO)
bot = Bot(token="6930718163:AAH6zwGjrrB_xbf38XaPjkIMFgIqiXkou9c")
from_router = Router()
dp = Dispatcher()



def start_buttons():
    buttons = [
        [KeyboardButton(text="ustoz kerak"), KeyboardButton(text="shogirt kerak")],
        [KeyboardButton(text="hodim kerak"), KeyboardButton(text="ish joyi kerak")],
        [KeyboardButton(text="sherik kerak"), KeyboardButton(text="users")]

    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


def finish_button():
    button = [
        [KeyboardButton(text="Ha"), KeyboardButton(text="Yoq")]
    ]
    return ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)




class Ishjoyikerak(StatesGroup): #ish joyi kerak
    ism = State()
    yosh = State()
    texnologiya= State()
    tel_raqam = State()
    hudud = State()
    narx = State()
    kasb = State()
    vaqt = State()
    maqsad = State()

class Ustozkerak(StatesGroup): # ustoz kerak
    ism = State()
    yosh = State()
    texnologiya= State()
    tel_raqam = State()
    hudud = State()
    narx = State()
    kasb = State()
    vaqt = State()
    maqsad = State()

class Shogirtkerak(StatesGroup): # shogirt kerak
    ism = State()
    yosh = State()
    texnologiya= State()
    tel_raqam = State()
    hudud = State()
    narx = State()
    kasb = State()
    vaqt = State()
    maqsad = State()

class Hodimkerak(StatesGroup): # hodim kerak
    ism = State()
    yosh = State()
    texnologiya= State()
    tel_raqam = State()
    hudud = State()
    narx = State()
    kasb = State()
    vaqt = State()
    maqsad = State()

class Sherikkerak(StatesGroup): # sherik kerak
    ism = State()
    yosh = State()
    texnologiya= State()
    tel_raqam = State()
    hudud = State()
    narx = State()
    kasb = State()
    vaqt = State()
    maqsad = State()






@from_router.message(Command("start"))
async def get_started(message: Message):
    full_name = message.from_user.full_name
    await message.answer(f"Assalomu alaykum {full_name}", reply_markup=start_buttons())

@from_router.message(F.text=="users")
async def get_info_users(message: Message):

    pass

@from_router.message(F.text=="ish joyi kerak")
async def ish_joyi_kerak(message: Message, state: FSMContext):
    text="""
    Ish joyi topish uchun ariza berish

    Hozir sizga birnecha savollar beriladi. 
    Har biriga javob bering. 
    Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.

    
    Ism, familiyangizni kiriting?

"""
    await message.answer(text=text)
    await state.set_state(Ishjoyikerak.ism)


@from_router.message(Ishjoyikerak.ism)
async def set_user_name(message: Message, state: FSMContext):
    await state.update_data(ism=message.text)
    text = """🕑 Yosh: 

Yoshingizni kiriting?
Masalan, 19
"""
    await message.answer(text=text)
    await state.set_state(Ishjoyikerak.yosh)



@from_router.message(Ishjoyikerak.yosh)
async def set_user_age(message: Message, state: FSMContext):
   
    if not message.text.isdigit():
        return await message.answer(text="yosh faqat sonlardan iborat bolsin")
   
    await state.update_data(yosh=message.text)
    text="""📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#
"""
    await message.answer(text=text)
    await state.set_state(Ishjoyikerak.texnologiya)


@from_router.message(Ishjoyikerak.texnologiya)
async def set_user_texnologiya(message: Message, state: FSMContext):
    await state.update_data(texnologiya=message.text)
    text="""📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67
"""
    await message.answer(text=text)
    await state.set_state(Ishjoyikerak.tel_raqam)


@from_router.message(Ishjoyikerak.tel_raqam)
async def set_user_tel_raqam(message: Message, state: FSMContext):

    if not re.match(PHONE_PATTERN, message.text):
        return await message.answer(text="uzb raqam ekanligiga ishonch hosil qiling")

    await state.update_data(tel_raqam=message.text)
    text="""🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting
"""
    await message.answer(text=text)
    await state.set_state(Ishjoyikerak.hudud)

@from_router.message(Ishjoyikerak.hudud)
async def set_user_hudud(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    text="""💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?
"""
    await message.answer(text=text)
    await state.set_state(Ishjoyikerak.narx)

@from_router.message(Ishjoyikerak.narx)
async def set_user_narx(message: Message, state: FSMContext):
    await state.update_data(narx=message.text)
    text="""👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba
"""
    await message.answer(text=text)
    await state.set_state(Ishjoyikerak.kasb)

@from_router.message(Ishjoyikerak.kasb)
async def set_user_kasb(message: Message, state: FSMContext):
    await state.update_data(kasb=message.text)
    text="""🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
"""
    await message.answer(text=text)
    await state.set_state(Ishjoyikerak.vaqt)

@from_router.message(Ishjoyikerak.vaqt)
async def set_user_vaqt(message: Message, state: FSMContext):
    await state.update_data(vaqt=message.text)
    text="""🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering.
"""
    await message.answer(text=text)
    await state.set_state(Ishjoyikerak.maqsad)

@from_router.message(Ishjoyikerak.maqsad, F.text=="Ha")
async def send_message(message: Message, state: FSMContext):
    data = await state.get_data()
    text = "Ma'lumotlaringiz adminga yuborildi"

    await bot.send_message(chat_id=710148744,text=text)
    create_user(data['ism'], data['yosh'],data['texnologiya'],data['tel_raqam'],data['hudud'],data['narx'],data['kasb'],data['vaqt'],data['maqsad'])
    await state.clear()


@from_router.message(Ishjoyikerak.maqsad , F.text=="Yoq")
async def button_yoq(message: Message, state: FSMContext):
    await message.answer(text="Ma'lumotlaringiz qabul qilinmadi")
    await state.clear()

@from_router.message(Ishjoyikerak.maqsad)
async def set_user_maqsad(message: Message, state: FSMContext):
    await state.update_data(maqsad=message.text)
    data = await state.get_data()
    text = f"""Ish joyi kerak:

👨‍💼 Xodim: {data['ism']}
🕑 Yosh: {data['yosh']}
📚 Texnologiya: {data['texnologiya']} 
🇺🇿 Telegram: @{message.from_user.username} 
📞 Aloqa: {data['tel_raqam']}
🌐 Hudud: {data['hudud']}
💰 Narxi: {data['narx']} 
👨🏻‍💻 Kasbi: {data['kasb']}
🕰 Murojaat qilish vaqti: {data['vaqt']} 
🔎 Maqsad: {data['maqsad']}

#Xodim #{data['texnologiya']} #{data['hudud']}
"""
    await message.answer(text, reply_markup=finish_button())
    await message.answer(text="📚 Hamma ma'lumotlar to'g'rimi")

#********************************************************************************************************************
#********************************************************************************************************************


@from_router.message(F.text=="ustoz kerak")
async def ustoz_kerak(message: Message, state: FSMContext):
    text="""
    Ustoz topish uchun ariza berish

    Hozir sizga birnecha savollar beriladi. 
    Har biriga javob bering. 
    Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.

    
    Ism, familiyangizni kiriting!

"""
    await message.answer(text=text)
    await state.set_state(Ustozkerak.ism)


@from_router.message(Ustozkerak.ism)
async def set_ustoz_name(message: Message, state: FSMContext):
    await state.update_data(ism=message.text)
    text = """🕑 Yosh: 

Yoshingizni kiriting!
Masalan, 19
"""
    await message.answer(text=text)
    await state.set_state(Ustozkerak.yosh)



@from_router.message(Ustozkerak.yosh)
async def set_ustoz_age(message: Message, state: FSMContext):
   
    if not message.text.isdigit():
        return await message.answer(text="yosh faqat sonlardan iborat bolsin")
   
    await state.update_data(yosh=message.text)
    text="""📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#
"""
    await message.answer(text=text)
    await state.set_state(Ustozkerak.texnologiya)


@from_router.message(Ustozkerak.texnologiya)
async def set_ustoz_texnologiya(message: Message, state: FSMContext):
    await state.update_data(texnologiya=message.text)
    text="""📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67
"""
    await message.answer(text=text)
    await state.set_state(Ustozkerak.tel_raqam)


@from_router.message(Ustozkerak.tel_raqam)
async def set_ustoz_tel_raqam(message: Message, state: FSMContext):

    if not re.match(PHONE_PATTERN, message.text):
        return await message.answer(text="uzb raqam ekanligiga ishonch hosil qiling")

    await state.update_data(tel_raqam=message.text)
    text="""🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting
"""
    await message.answer(text=text)
    await state.set_state(Ustozkerak.hudud)

@from_router.message(Ustozkerak.hudud)
async def set_ustoz_hudud(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    text="""💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?
"""
    await message.answer(text=text)
    await state.set_state(Ustozkerak.narx)

@from_router.message(Ustozkerak.narx)
async def set_ustoz_narx(message: Message, state: FSMContext):
    await state.update_data(narx=message.text)
    text="""👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba
"""
    await message.answer(text=text)
    await state.set_state(Ustozkerak.kasb)

@from_router.message(Ustozkerak.kasb)
async def set_ustoz_kasb(message: Message, state: FSMContext):
    await state.update_data(kasb=message.text)
    text="""🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
"""
    await message.answer(text=text)
    await state.set_state(Ustozkerak.vaqt)

@from_router.message(Ustozkerak.vaqt)
async def set_ustoz_vaqt(message: Message, state: FSMContext):
    await state.update_data(vaqt=message.text)
    text="""🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering.
"""
    await message.answer(text=text)
    await state.set_state(Ustozkerak.maqsad)

@from_router.message(Ustozkerak.maqsad, F.text=="Ha")
async def send_message(message: Message, state: FSMContext):
    data = await state.get_data()
    text = "Ma'lumotlaringiz adminga yuborildi"

    await bot.send_message(chat_id=710148744,text=text)
    await state.clear()


@from_router.message(Ustozkerak.maqsad , F.text=="Yoq")
async def button_yoq_ustoz(message: Message, state: FSMContext):
    await message.answer(text="Ma'lumotlaringiz qabul qilinmadi")
    await state.clear()

@from_router.message(Ustozkerak.maqsad)
async def set_ustoz_maqsad(message: Message, state: FSMContext):
    await state.update_data(maqsad=message.text)
    data = await state.get_data()
    text = f"""Ustoz kerak:

👨‍💼 Ustoz: {data['ism']}
🕑 Yosh: {data['yosh']}
📚 Texnologiya: {data['texnologiya']} 
🇺🇿 Telegram: @{message.from_user.username} 
📞 Aloqa: {data['tel_raqam']}
🌐 Hudud: {data['hudud']}
💰 Narxi: {data['narx']} 
👨🏻‍💻 Kasbi: {data['kasb']}
🕰 Murojaat qilish vaqti: {data['vaqt']} 
🔎 Maqsad: {data['maqsad']}

#Ustoz #{data['texnologiya']} #{data['hudud']}
"""
    await message.answer(text=text, reply_markup=finish_button())
    await message.answer(text="📚 Hamma ma'lumotlar to'g'rimi")




#********************************************************************************************************************
#********************************************************************************************************************



@from_router.message(F.text=="shogirt kerak")
async def shogirt_kerak(message: Message, state: FSMContext):
    text="""
    Shogirt topish uchun ariza berish

    Hozir sizga birnecha savollar beriladi. 
    Har biriga javob bering. 
    Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.

    
    Ism, familiyangizni kiriting!

"""
    await message.answer(text=text)
    await state.set_state(Shogirtkerak.ism)


@from_router.message(Shogirtkerak.ism)
async def set_shogirt_name(message: Message, state: FSMContext):
    await state.update_data(ism=message.text)
    text = """🕑 Yosh: 

Yoshingizni kiriting!
Masalan, 19
"""
    await message.answer(text=text)
    await state.set_state(Shogirtkerak.yosh)



@from_router.message(Shogirtkerak.yosh)
async def set_shogirt_age(message: Message, state: FSMContext):
   
    if not message.text.isdigit():
        return await message.answer(text="yosh faqat sonlardan iborat bolsin")
   
    await state.update_data(yosh=message.text)
    text="""📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#
"""
    await message.answer(text=text)
    await state.set_state(Shogirtkerak.texnologiya)


@from_router.message(Shogirtkerak.texnologiya)
async def set_shogirt_texnologiya(message: Message, state: FSMContext):
    await state.update_data(texnologiya=message.text)
    text="""📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67
"""
    await message.answer(text=text)
    await state.set_state(Shogirtkerak.tel_raqam)


@from_router.message(Shogirtkerak.tel_raqam)
async def set_shogirt_tel_raqam(message: Message, state: FSMContext):

    if not re.match(PHONE_PATTERN, message.text):
        return await message.answer(text="uzb raqam ekanligiga ishonch hosil qiling")

    await state.update_data(tel_raqam=message.text)
    text="""🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting
"""
    await message.answer(text=text)
    await state.set_state(Shogirtkerak.hudud)

@from_router.message(Shogirtkerak.hudud)
async def set_shogirt_hudud(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    text="""💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?
"""
    await message.answer(text=text)
    await state.set_state(Shogirtkerak.narx)

@from_router.message(Shogirtkerak.narx)
async def set_shogirt_narx(message: Message, state: FSMContext):
    await state.update_data(narx=message.text)
    text="""👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba
"""
    await message.answer(text=text)
    await state.set_state(Shogirtkerak.kasb)

@from_router.message(Shogirtkerak.kasb)
async def set_shogirt_kasb(message: Message, state: FSMContext):
    await state.update_data(kasb=message.text)
    text="""🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
"""
    await message.answer(text=text)
    await state.set_state(Shogirtkerak.vaqt)

@from_router.message(Shogirtkerak.vaqt)
async def set_shogirt_vaqt(message: Message, state: FSMContext):
    await state.update_data(vaqt=message.text)
    text="""🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering.
"""
    await message.answer(text=text)
    await state.set_state(Shogirtkerak.maqsad)

@from_router.message(Shogirtkerak.maqsad, F.text=="Ha")
async def send_message(message: Message, state: FSMContext):
    data = await state.get_data()
    text = "Ma'lumotlaringiz adminga yuborildi"

    await bot.send_message(chat_id=710148744,text=text)
    await state.clear()


@from_router.message(Shogirtkerak.maqsad , F.text=="Yoq")
async def button_yoq_shogirt(message: Message, state: FSMContext):
    await message.answer(text="Ma'lumotlaringiz qabul qilinmadi")
    await state.clear()

@from_router.message(Shogirtkerak.maqsad)
async def set_shogirt_maqsad(message: Message, state: FSMContext):
    await state.update_data(maqsad=message.text)
    data = await state.get_data()
    text = f"""Shogirt kerak:

👨‍💼 Shogirt: {data['ism']}
🕑 Yosh: {data['yosh']}
📚 Texnologiya: {data['texnologiya']} 
🇺🇿 Telegram: @{message.from_user.username} 
📞 Aloqa: {data['tel_raqam']}
🌐 Hudud: {data['hudud']}
💰 Narxi: {data['narx']} 
👨🏻‍💻 Kasbi: {data['kasb']}
🕰 Murojaat qilish vaqti: {data['vaqt']} 
🔎 Maqsad: {data['maqsad']}

#Shogirt #{data['texnologiya']} #{data['hudud']}
"""
    await message.answer(text, reply_markup=finish_button())
    await message.answer(text="📚 Hamma ma'lumotlar to'g'rimi")


#********************************************************************************************************************
#********************************************************************************************************************



@from_router.message(F.text=="hodim kerak")
async def hodim_kerak(message: Message, state: FSMContext):
    text="""
    Hodim topish uchun ariza berish

    Hozir sizga birnecha savollar beriladi. 
    Har biriga javob bering. 
    Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.

    
    Ism, familiyangizni kiriting!

"""
    await message.answer(text=text)
    await state.set_state(Hodimkerak.ism)


@from_router.message(Hodimkerak.ism)
async def set_hodim_name(message: Message, state: FSMContext):
    await state.update_data(ism=message.text)
    text = """🕑 Yosh: 

Yoshingizni kiriting!
Masalan, 19
"""
    await message.answer(text=text)
    await state.set_state(Hodimkerak.yosh)



@from_router.message(Hodimkerak.yosh)
async def set_hodim_age(message: Message, state: FSMContext):
   
    if not message.text.isdigit():
        return await message.answer(text="yosh faqat sonlardan iborat bolsin")
   
    await state.update_data(yosh=message.text)
    text="""📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#
"""
    await message.answer(text=text)
    await state.set_state(Hodimkerak.texnologiya)


@from_router.message(Hodimkerak.texnologiya)
async def set_hodim_texnologiya(message: Message, state: FSMContext):
    await state.update_data(texnologiya=message.text)
    text="""📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67
"""
    await message.answer(text=text)
    await state.set_state(Hodimkerak.tel_raqam)


@from_router.message(Hodimkerak.tel_raqam)
async def set_hodim_tel_raqam(message: Message, state: FSMContext):

    if not re.match(PHONE_PATTERN, message.text):
        return await message.answer(text="uzb raqam ekanligiga ishonch hosil qiling")

    await state.update_data(tel_raqam=message.text)
    text="""🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting
"""
    await message.answer(text=text)
    await state.set_state(Hodimkerak.hudud)

@from_router.message(Hodimkerak.hudud)
async def set_hodim_hudud(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    text="""💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?
"""
    await message.answer(text=text)
    await state.set_state(Hodimkerak.narx)

@from_router.message(Hodimkerak.narx)
async def set_hodim_narx(message: Message, state: FSMContext):
    await state.update_data(narx=message.text)
    text="""👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba
"""
    await message.answer(text=text)
    await state.set_state(Hodimkerak.kasb)

@from_router.message(Hodimkerak.kasb)
async def set_hodim_kasb(message: Message, state: FSMContext):
    await state.update_data(kasb=message.text)
    text="""🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
"""
    await message.answer(text=text)
    await state.set_state(Hodimkerak.vaqt)

@from_router.message(Hodimkerak.vaqt)
async def set_hodim_vaqt(message: Message, state: FSMContext):
    await state.update_data(vaqt=message.text)
    text="""🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering.
"""
    await message.answer(text=text)
    await state.set_state(Hodimkerak.maqsad)

@from_router.message(Hodimkerak.maqsad, F.text=="Ha")
async def send_message(message: Message, state: FSMContext):
    data = await state.get_data()
    text = "Ma'lumotlaringiz adminga yuborildi"

    await bot.send_message(chat_id=710148744,text=text)
    await state.clear()


@from_router.message(Hodimkerak.maqsad , F.text=="Yoq")
async def button_yoq_hodim(message: Message, state: FSMContext):
    await message.answer(text="Ma'lumotlaringiz qabul qilinmadi")
    await state.clear()

@from_router.message(Hodimkerak.maqsad)
async def set_hodim_maqsad(message: Message, state: FSMContext):
    await state.update_data(maqsad=message.text)
    data = await state.get_data()
    text = f"""Hodim kerak:

👨‍💼 Hodim: {data['ism']}
🕑 Yosh: {data['yosh']}
📚 Texnologiya: {data['texnologiya']} 
🇺🇿 Telegram: @{message.from_user.username} 
📞 Aloqa: {data['tel_raqam']}
🌐 Hudud: {data['hudud']}
💰 Narxi: {data['narx']} 
👨🏻‍💻 Kasbi: {data['kasb']}
🕰 Murojaat qilish vaqti: {data['vaqt']} 
🔎 Maqsad: {data['maqsad']}

#Hodim #{data['texnologiya']} #{data['hudud']}
"""
    await message.answer(text, reply_markup=finish_button())
    await message.answer(text="📚 Hamma ma'lumotlar to'g'rimi")



#********************************************************************************************************************
#********************************************************************************************************************
   



@from_router.message(F.text=="sherik kerak")
async def sherik_kerak(message: Message, state: FSMContext):
    text="""
    Sherik topish uchun ariza berish

    Hozir sizga birnecha savollar beriladi. 
    Har biriga javob bering. 
    Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.

    
    Ism, familiyangizni kiriting!

"""
    await message.answer(text=text)
    await state.set_state(Sherikkerak.ism)


@from_router.message(Sherikkerak.ism)
async def set_sherik_name(message: Message, state: FSMContext):
    await state.update_data(ism=message.text)
    text = """🕑 Yosh: 

Yoshingizni kiriting!
Masalan, 19
"""
    await message.answer(text=text)
    await state.set_state(Sherikkerak.yosh)



@from_router.message(Sherikkerak.yosh)
async def set_sherik_age(message: Message, state: FSMContext):
   
    if not message.text.isdigit():
        return await message.answer(text="yosh faqat sonlardan iborat bolsin")
   
    await state.update_data(yosh=message.text)
    text="""📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#
"""
    await message.answer(text=text)
    await state.set_state(Sherikkerak.texnologiya)


@from_router.message(Sherikkerak.texnologiya)
async def set_sherik_texnologiya(message: Message, state: FSMContext):
    await state.update_data(texnologiya=message.text)
    text="""📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67
"""
    await message.answer(text=text)
    await state.set_state(Sherikkerak.tel_raqam)


@from_router.message(Sherikkerak.tel_raqam)
async def set_sherik_tel_raqam(message: Message, state: FSMContext):

    if not re.match(PHONE_PATTERN, message.text):
        return await message.answer(text="uzb raqam ekanligiga ishonch hosil qiling")

    await state.update_data(tel_raqam=message.text)
    text="""🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting
"""
    await message.answer(text=text)
    await state.set_state(Sherikkerak.hudud)

@from_router.message(Sherikkerak.hudud)
async def set_sherik_hudud(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    text="""💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?
"""
    await message.answer(text=text)
    await state.set_state(Sherikkerak.narx)

@from_router.message(Sherikkerak.narx)
async def set_sherik_narx(message: Message, state: FSMContext):
    await state.update_data(narx=message.text)
    text="""👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba
"""
    await message.answer(text=text)
    await state.set_state(Sherikkerak.kasb)

@from_router.message(Sherikkerak.kasb)
async def set_sherik_kasb(message: Message, state: FSMContext):
    await state.update_data(kasb=message.text)
    text="""🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
"""
    await message.answer(text=text)
    await state.set_state(Sherikkerak.vaqt)

@from_router.message(Sherikkerak.vaqt)
async def set_sherik_vaqt(message: Message, state: FSMContext):
    await state.update_data(vaqt=message.text)
    text="""🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering.
"""
    await message.answer(text=text)
    await state.set_state(Sherikkerak.maqsad)

@from_router.message(Sherikkerak.maqsad, F.text=="Ha")
async def send_message(message: Message, state: FSMContext):
    data = await state.get_data()
    text = "Ma'lumotlaringiz adminga yuborildi"

    await bot.send_message(chat_id=710148744,text=text)
    await state.clear()


@from_router.message(Sherikkerak.maqsad , F.text=="Yoq")
async def button_yoq_sherik(message: Message, state: FSMContext):
    await message.answer(text="Ma'lumotlaringiz qabul qilinmadi")
    await state.clear()

@from_router.message(Sherikkerak.maqsad)
async def set_sherik_maqsad(message: Message, state: FSMContext):
    await state.update_data(maqsad=message.text)
    data = await state.get_data()
    text = f"""Sherik kerak:

👨‍💼 Sherik: {data['ism']}
🕑 Yosh: {data['yosh']}
📚 Texnologiya: {data['texnologiya']} 
🇺🇿 Telegram: @{message.from_user.username} 
📞 Aloqa: {data['tel_raqam']}
🌐 Hudud: {data['hudud']}
💰 Narxi: {data['narx']} 
👨🏻‍💻 Kasbi: {data['kasb']}
🕰 Murojaat qilish vaqti: {data['vaqt']} 
🔎 Maqsad: {data['maqsad']}

#Sherik #{data['texnologiya']} #{data['hudud']}
"""
    await message.answer(text=text, reply_markup=finish_button())
    await message.answer(text="📚 Hamma ma'lumotlar to'g'rimi")





async def main():
    dp.include_router(from_router)
    print("bot ishladi")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

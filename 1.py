from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import StateFilter
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
import asyncio
import logging
import sys
from aiogram import types
from aiogram import Bot, Dispatcher, Router, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import re
import database as dtb
import os
import sqlite3
from dotenv import *
load_dotenv()
TOKEN = os.getenv('7501629492:AAEDjgxGKxV0DMNKu5Ms6lbYbs6FymJ4zME')
connection = sqlite3.connect('startup_loyiha.db')  # Ma'lumotlar bazasiga ulanish
# c = dtb.get_startup(connection)  # connection ni uzatish
#print(c)
#connection.close()
TOKEN='7501629492:AAEDjgxGKxV0DMNKu5Ms6lbYbs6FymJ4zME'
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Router()
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
router = Router()
router.include_router(dp)
def validate_phone_number(value: str) -> bool:
    pattern = re.compile(r'\+998[0-9]{9}')
    return bool(pattern.match(value))
class Order(StatesGroup):
    full_name = State()
    phone_number = State()
    field=State()
    item=State()
    #quantity=State()
@dp.message(F.text == '/start')
async def start(message: Message):
    if message.from_user.id=="5306481482":
        mb=[KeyboardButton(text='/bugungi_arizalar'),KeyboardButton(text='/barcha_arizalar')]
        buttons1 = ReplyKeyboardMarkup(keyboard=mb, resize_keyboard=True)

        await message.answer(f"Admin bugungi arizalarni olish uchun /bugungi_arizalar tugmasini bosing", reply_markup=buttons1)
        await message.answer(f"Admin barcha arizalarni olish uchun /barcha_arizalar tugmasini bosing", reply_markup=buttons1)
    else:   
        kb = [
            [KeyboardButton(text='/help'), KeyboardButton(text='/StartUp_taklif_yuborish')]
        ]

        buttons = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


        await message.answer(f"{message.from_user.first_name}, sizni botimizga ko'rganimizdan xursandmiz!, StartUp loyiha boshlash uchun\n/StartUp_taklif_yuborish tugmasini bosing", reply_markup=buttons)
@dp.message(F.text == '/bugungi_arizalar')
async def start_ordering(message: Message):
    await message.answer(text=dtb.get_startup())
@dp.message(F.text == '/barcha_arizalar')
async def start_ordering(message: Message):
    await message.answer(text=dtb.get_startup())
@dp.message(F.text == '/StartUp_taklif_yuborish')
async def start_ordering(message: Message, state: FSMContext):
    await message.answer(text='StartUp taklif boshlandi FIOni kiriting')
    await state.set_state(Order.full_name.state)
@dp.message(F.text == '/help')
async def start_ordering(message: Message):
    await message.answer(text="Sizga biror bir savol yoki yordam kerak bo'lsa @dasturch1_asilbek ga murojaat qiling")
@dp.message(StateFilter(Order.full_name))
async def set_full_name(message: Message, state: FSMContext):
    kb = [[KeyboardButton(text='Telefon raqamimni yuborish', request_contact=True)]]
    buttons = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await state.update_data(full_name=message.text)
    await message.answer(text='Telefom raqamingizni yuboring', reply_markup=buttons)
    await state.set_state(Order.phone_number.state)
@dp.message(StateFilter(Order.phone_number))
async def set_full_name(message: Message, state: FSMContext):
    phone_number = message.contact.phone_number if message.contact.phone_number.startswith("+") else "+" + message.contact.phone_number
    if not validate_phone_number(phone_number):
        return await message.answer(text="Tog'ri formatda telefon raqam kiriting")
    await state.update_data(phone_number=phone_number)
    await message.answer(text="Yo'nalishingiz nomi")
    await state.set_state(Order.field.state)    
@dp.message(StateFilter(Order.field))
async def set_full_name(message: Message, state: FSMContext):
    await state.update_data(field=message.text)
    await message.answer(text="StartUp loyihangiz haqida to'liqroq yozing")
    await state.set_state(Order.item.state)
#@dp.message(StateFilter(Order.item))
# async def set_full_name(message: Message, state: FSMContext):
#     await state.update_data(item=message.text)
#     await message.answer(text="Bu malumotlar to'g'rimi")
#     await state.set_state(Order.quantity.state)
# # @dp.message(StateFilter(Order.quantity))
# # async def set_full_name(message: Message, state: FSMContext):
#     data = await state.get_data()
#     if 'quantity' in data:
#         msg = f"""StartUp loyiha: \nFIO: {data['full_name']} \nTelefon raqam: {data['phone_number']} \nSizning StartUp loyihangiz: {data['item']} \n: {data['field']}"""
    
#     kb = [
#         [KeyboardButton(text='Ha'), KeyboardButton(text="Yo'q")]
#     ]

#     await state.update_data(quantity=message.text)
#     buttons = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
#     msg = f"""StartUp loyiha: \nIsm: {data['full_name']} \nTelefon raqam: {data['phone_number']}\nSizning StartUp loyihangiz: {data['item']} \nYo'nalish: {data['field']} """
   
#     await message.answer(msg, reply_markup=buttons)
#     if message.text == 'Ha':
        
#         a=dtb.insert_database(str(data['full_name']),str(data['phone_number']),str(data['item']),str(data['field']))
#         print(a)
#         await message.answer(text="Sizning StartUpingiz muvaffaqiyatli to'ldirildi")
#         print(dtb.get_startup(connection))
#         return await state.clear()
        
#     elif message.text == "Yo'q":
#         await message.answer(text='Sizning StartUp loyihangiz bekor qilindi')
#         return await state.clear() 
@dp.message(StateFilter(Order.item))
async def set_full_name(message: Message, state: FSMContext):
    await state.update_data(item=message.text)
    data = await state.get_data()
    msg = f"""    StartUp loyiha: 
    Ism: {data['full_name']} 
    Telefon raqam: {data['phone_number']}
    Sizning StartUp loyihangiz: {data['item']} 
    Yo'nalish: {data['field']}"""
    kb = [[KeyboardButton(text='Ha'), KeyboardButton(text="Yo'q")]]
    buttons = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(msg, reply_markup=buttons)
    if message.text == 'Ha':
        a = dtb.insert_database(str(data['full_name']), str(data['phone_number']), str(data['item']), str(data['field']))
        print(a)
        await message.answer(text="Sizning StartUpingiz muvaffaqiyatli to'ldirildi")
        all_startups = dtb.get_startup(connection)  # connection ni tekshiring
        print(all_startups)
        return await state.clear()
    elif message.text == "Yo'q":
        await message.answer(text='Sizning StartUp loyihangiz bekor qilindi')
        return await state.clear()
async def main() -> None:
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    commands = [types.BotCommand(command="start", description="Botni ishga tushurish uchun bosing"),]
    await bot.set_my_commands(commands)
    dp.include_router(router)
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
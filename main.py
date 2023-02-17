from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
import json
from db import DB

TOKEN='5845181398:AAFJlcA-QBUXlX5WVOjdDwb3Cr_vrR28WUo'

def start(update: Update, context: CallbackContext):
    bot=context.bot 
    chat_id=update.message.chat.id
    user_id=update.message.from_user.id
    db=DB('db.json')
    db.starting(chat_id)
    db.save()
    text='Tilni tanlang\n Chooze language'
    eng=InlineKeyboardButton('🏴󠁧󠁢󠁥󠁮󠁧󠁿English',callback_data='til eng')
    uz=InlineKeyboardButton('🇺🇿O\'zbek',callback_data='til uz')
    ru=InlineKeyboardButton('🇷🇺Русский',callback_data='til ru')
    ki_uz=InlineKeyboardButton('🇺🇿Узбек',callback_data='til ki')
    button=InlineKeyboardMarkup([[eng,uz],[ru,ki_uz]])
    bot.sendMessage(chat_id,text,reply_markup=button)

def obuna(update: Update, context: CallbackContext):
    query = update.callback_query
    chat_id = query.message.chat_id
    data = query.data[4:]
    bot = context.bot

    if data=='uz':
        text = '''Quyidagi kanallarimizga obuna bo'ling va "Tekshirish" tugnasini bosing! Botni keyin to'liq ishlatishingiz mumkin!'''
        kanal_1 = InlineKeyboardButton('1-kanal',callback_data='ob kanal-1', url='https://t.me/jannatizla')
        kanal_2 = InlineKeyboardButton('2-kanal',callback_data='ob kanal-2',url='nmadir')
        tekshirish = InlineKeyboardButton('Tekshirish',callback_data='ob tekshirish')
        button=InlineKeyboardMarkup([[kanal_1],[kanal_2],[tekshirish]])
        bot.sendMessage(chat_id,text,reply_markup=button)
    elif data=='eng':

    

updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(CallbackQueryHandler(query,pattern='til'))

updater.start_polling()
updater.idle()
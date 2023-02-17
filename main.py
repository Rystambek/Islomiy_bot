from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
import json

TOKEN='5845181398:AAFJlcA-QBUXlX5WVOjdDwb3Cr_vrR28WUo'

def strat(update: Update, context: CallbackContext):
    bot=context.bot 
    chat_id=update.message.chat.id
    user_id=update.message.from_user.id
    text='Tilni tanlang\n Chooze language'
    eng=InlineKeyboardButton('🏴󠁧󠁢󠁥󠁮󠁧󠁿English',callback_data='eng')
    uz=InlineKeyboardButton('🇺🇿O\'zbek',callback_data='uz')
    ru=InlineKeyboardButton('🇷🇺Русский',callback_data='ru')
    ki_uz=InlineKeyboardButton('🇺🇿Узбек',callback_data='ki')
    button=InlineKeyboardMarkup([[eng,uz],[ru,ki_uz]])
    bot.sendMessage(chat_id,text,reply_markup=button)

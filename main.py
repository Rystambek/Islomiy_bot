from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
from db import DB

TOKEN='5845181398:AAFJlcA-QBUXlX5WVOjdDwb3Cr_vrR28WUo'
# def ob_tekshir(update: Update, context: CallbackContext):
#     bot=context.bot 
#     chat_id=update.message.chat.id
#     data=DB('db.json')
#     kan1=data.get_channel()[0][13:]
#     kan2=data.get_channel()[1][13:]
#     chan1=bot.getChatMember(f'@{kan1}',chat_id)
#     chan2=bot.getChatMember(f'@{kan2}',chat_id)
#     data.save()
#     if not (chan1!='left' and chan2!='left'):
#         return True
#     else:
#         return False


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
    db=DB('db.json')
    db.add_lang(str(chat_id),lang=data)
    kan1=db.get_channel()[0]
    kan2=db.get_channel()[1]
    db.save()
    if data=='uz':
        text = '''Quyidagi kanallarimizga obuna bo'ling va "Tekshirish" tugnasini bosing! Botni keyin to'liq ishlatishingiz mumkin!'''
        kanal_1 = InlineKeyboardButton('1-kanal',callback_data='ob kanal-1', url=kan1)
        kanal_2 = InlineKeyboardButton('2-kanal',callback_data='ob kanal-2',url=kan2)
        tekshirish = InlineKeyboardButton('Tekshirish',callback_data='ob tek')
        button=InlineKeyboardMarkup([[kanal_1],[kanal_2],[tekshirish]])
        bot.sendMessage(chat_id,text,reply_markup=button)
    elif data=='eng':
        text = '''Subscribe to our channels below and click the "Check Out" button! You can fully use the bot afterwards!'''
        kanal_1 = InlineKeyboardButton('1-channel',callback_data='ob kanal-1', url=kan1)
        kanal_2 = InlineKeyboardButton('2-channel',callback_data='ob kanal-2',url=kan2)
        tekshirish = InlineKeyboardButton('Check',callback_data='ob tek')
        button=InlineKeyboardMarkup([[kanal_1],[kanal_2],[tekshirish]])
        bot.sendMessage(chat_id,text,reply_markup=button)
    elif data=='ru':
        text='Подпишитесь на наши каналы ниже и нажмите кнопку «Оформить заказ»! После этого вы сможете полноценно использовать бота!'
        kanal_1 = InlineKeyboardButton('Канал 1',callback_data='ob kanal-1', url=kan1)
        kanal_2 = InlineKeyboardButton('Канал 2',callback_data='ob kanal-2',url=kan2)
        tekshirish = InlineKeyboardButton('Проверять',callback_data='ob tek')
        button=InlineKeyboardMarkup([[kanal_1],[kanal_2],[tekshirish]])
        bot.sendMessage(chat_id,text,reply_markup=button)
    else:
        text='Қуйидаги каналларимизга обуна бўлинг ва "Текшириш" тугмасини босинг! Ботни кейин тўлиқ ишлатишингиз мумкин!'
        kanal_1 = InlineKeyboardButton('1-Канал',callback_data='ob kanal-1', url=kan1)
        kanal_2 = InlineKeyboardButton('2-Канал',callback_data='ob kanal-2',url=kan2)
        tekshirish = InlineKeyboardButton('Текшириш',callback_data='ob tek')
        button=InlineKeyboardMarkup([[kanal_1],[kanal_2],[tekshirish]])
        bot.sendMessage(chat_id,text,reply_markup=button)

def tekshirish(update: Update, context: CallbackContext):
    query = update.callback_query
    chat_id = query.message.chat_id
    data = query.data[3:]
    bot = context.bot
    dbm=DB('db.json')
    data=dbm.dbe()
    lang=dbm.get_lang(chat_id)
    menu=data['texts']['obuna']
    dbm.save()
    kan1=dbm.get_channel()[0][13:]
    kan2=dbm.get_channel()[1][13:]
    chan1=bot.getChatMember(f'@{kan1}',chat_id)['status']
    chan2=bot.getChatMember(f'@{kan2}',chat_id)['status']
    dbm.save()
    print(chan1,chan2)
    if (chan1!='left' and chan2!='left'):
        k=True
    else:
        k=False
    if k:
       text=data['texts']['obuna'][lang]
       button1=InlineKeyboardButton(text=menu['buttons'][lang]['film'], callback_data='key film')
       button2=InlineKeyboardButton(text=menu['buttons'][lang]['multik'], callback_data='key multik')
       button3=InlineKeyboardButton(text=menu['buttons'][lang]['qiroat'], callback_data='key qiroat')
       button4=InlineKeyboardButton(text=menu['buttons'][lang]['nashed'], callback_data='key nashed')
       buttons=InlineKeyboardMarkup([[button1,button2],[button3,button4]])
       bot.sendMessage(chat_id,text,reply_markup=buttons)
    else:
        text=data['texts']['obuna_e'][lang]
        bot.sendMessage(chat_id,text)



    

updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(CallbackQueryHandler(obuna,pattern='til'))
updater.dispatcher.add_handler(CallbackQueryHandler(tekshirish,pattern='ob'))

updater.start_polling()
updater.idle()
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler , Updater , CallbackContext
from telegram import Update
from telegram.constants import ChatAction
from telegram import ReplyKeyboardMarkup
from telegram.ext import MessageHandler
from telegram.ext import filters
# from telegram import InlineKeyboardMarkup
# from telegram import InlineKeyboardButton
# from telegram.ext import CallbackQueryHandler
# from telegram.ext import ConversationHandler

from fragmentbot import fragment

import logging

token = "####################################"

logging.basicConfig(filename='error.log', level=logging.ERROR,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


async def error(update:Update , context : CallbackContext) :
    logging.warning('Update "%s" caused error "%s"', update, context.error)

async def start (update : Update , context : CallbackContext) :
    chat_id = update.message.chat_id
    fisrname = update.message.chat.first_name
    lastname = update.message.chat.last_name
    if fisrname == None :
        fisrname = " "
    if lastname == None :
        lastname = " "
    await context.bot.send_chat_action(chat_id , ChatAction.TYPING)
    await context.bot.sendMessage(chat_id , " سلام " + str(fisrname) + " " + str(lastname) + "خوش آمدی")
    await user_menu(update , context)

async def user_menu(update : Update , context : CallbackContext) :
    buttons = [
        ["فرگمنت"],
        ["درباره"]
    ]
    await update.message.reply_text(text="منو اصلی :" , reply_markup=ReplyKeyboardMarkup(buttons , resize_keyboard=True))

async def fragment_handler (update : Update , context  : CallbackContext) :
    chat_id = update.message.chat_id
    await context.bot.send_chat_action(chat_id , ChatAction.TYPING)
    await context.bot.sendMessage(chat_id , "لطفا کانفیگ خود را ارسال کنید ... ")
    context.user_data['action'] = 'frag'

async def text_handler (update : Update , context : CallbackContext) :
    chat_id = update.message.chat_id
    if context.user_data['action'] == "frag" :
        text = update.message.text
        context.user_data['action'] = " "
        output = fragment(text)
        await context.bot.send_chat_action(chat_id , ChatAction.TYPING)
        await context.bot.sendMessage(chat_id , output)


async def about(update : Update , context : CallbackContext) :
    chat_id = update.message.chat_id
    await context.bot.send_chat_action(chat_id , ChatAction.TYPING)
    await context.bot.sendMessage(chat_id , "Created By @wikm360 with ❤️ \n V1.0" )

def main () :
    application = ApplicationBuilder().token(token).build()
    application.add_handler(CommandHandler("start" , start))
    #application.add_handler(CommandHandler("admin" , admin_handler))

    #application.add_handler(CallbackQueryHandler(query_handler))

    application.add_handler(MessageHandler(filters.Regex("فرگمنت") , fragment_handler))
    application.add_handler(MessageHandler(filters.Regex("درباره") , about))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND , text_handler))

    application.add_error_handler(error)

    application.run_polling()


main()
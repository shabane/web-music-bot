import href
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
import telegram
import requests
import os
import threading

token = '5198855944:AAEw5zbkC_2IaJLJTHD6qMsYu3Q8nLbgH4Q'

bot = telegram.Bot(token=token)


def getMusic(update, context):

    link = update.message.text
    cht_id = update.message.chat_id
    link = href.GetAllTags(link, '.*mp3.*')
    for i in link:
        # update.message.reply_text(f'downloading {os.path.basename(i)}')
        tmp = requests.get(i)
        # update.message.reply_text(f'download comleted, sending to telegram')
        bot.send_audio(chat_id=cht_id, audio=tmp.content, title=f'{os.path.basename(i)}')
    update.message.reply_text(f'all songs sent :)')


threads = []
def letStart(update, context):
    t = threading.Thread(target=getMusic, args=(update, context))
    threads.append(t.start())

updater = Updater(token=token)
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.text, letStart))

updater.start_polling()
updater.idle()
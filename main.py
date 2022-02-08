# Libraries
import os
import href
import telegram
import requests
import threading
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

# Config
TOKEN = '5198855944:AAHRBODh_sYxttNSdan46tqRXoLkFgcWL5U'

# Functions
def getMusic(update, context):
    link = update.message.text
    cht_id = update.message.chat_id
    link = href.GetAllTags(link)

    if link:
        update.message.reply_text(f'{len(link)} song found')
        for i in link:
            name = os.path.basename(i).replace('%', ' ')
            if 'http' in i:
                if not '.zip' in i:
                    print(i)
                    try:
                        print('by telegram', i)
                        bot.sendAudio(chat_id=cht_id, audio=i, title=name)
                    except:
                        print('by download', i)
                        tmp = requests.get(i)
                        if not (len(tmp.content) / 2**20) > 50:
                            bot.send_audio(chat_id=cht_id, audio=tmp.content, title=name)
        update.message.reply_text(f'all songs sent :)')
    else:
        print('no song found')
        update.message.reply_text(f'no song found :(')

def letStart(update, context):
    t = threading.Thread(target=getMusic, args=(update, context))
    threads.append(t.start())

def status(update, context):
    update.message.reply_text('bot is alive')

# Start point

print("Starting.")

threads = []

bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('status', status))
dispatcher.add_handler(MessageHandler(Filters.text, letStart))

updater.start_polling()
updater.idle()

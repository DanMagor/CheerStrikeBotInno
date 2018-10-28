from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler

TOKEN = open("../token.txt", "r").read()

users = {}

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def addStrike(bot, update, args):
    postUser = update.message.from_user
    if len(args) == 0:
        return
    username_formatted = args[0]
    username = str(args[0]).lower()
    if username == "@danmagor":
        bot.send_message(chat_id=update.message.chat_id,
                         text="LoL, Nope :)")
        return
    if username not in users:
        users[username] = 1
        print(users)
    else:
        users[username] = users[username] + 1
    if users[username] < 3:
        bot.send_message(chat_id=update.message.chat_id,
                         text="Cheerleader {} now has {} strike(s)!".format(username_formatted, users[username]))
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Too much strikes :C {} ".format(username))


strike_handler = CommandHandler('addStrike', addStrike, pass_args=True)

dispatcher.add_handler(strike_handler)

# Start Bot
updater.start_polling()

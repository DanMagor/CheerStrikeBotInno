from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler

TOKEN = open("../token.txt", "r").read()

realStrikes = {}

dummyStrikes = {}

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def addRealStrike(bot, update, args):
    username_formatted = args[0]
    username_lower = str(args[0]).lower()
    if username_lower == "@danmagor":
        bot.send_message(chat_id=update.message.chat_id,
                         text="LoL, Nope :)")
        return

    if username_lower not in realStrikes:
        realStrikes[username_lower] = 1
    else:
        realStrikes[username_lower] = realStrikes[username_lower] + 1

    if realStrikes[username_lower] + dummyStrikes[username_lower] < 3:
        bot.send_message(chat_id=update.message.chat_id,
                         text="Cheerleader {} now has {} strike(s)!".format(username_formatted,
                                                                            realStrikes[username_lower] + dummyStrikes[
                                                                                username_lower]))
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Too much strikes :C {} ".format(username_lower))


def addDummyStrike(bot, update, args):
    username_formatted = args[0]
    username_lower = str(args[0]).lower()
    if username_lower == "@danmagor":
        bot.send_message(chat_id=update.message.chat_id,
                         text="LoL, Nope :)")
        return
    if username_lower not in dummyStrikes:
        dummyStrikes[username_lower] = 1
    else:
        dummyStrikes[username_lower] = dummyStrikes[username_lower] + 1
    if dummyStrikes[username_lower] < 3:
        bot.send_message(chat_id=update.message.chat_id,
                         text="Cheerleader {} now has {} strike(s)!".format(username_formatted,
                                                                            dummyStrikes[username_lower] + dummyStrikes[
                                                                                username_lower]))
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Too much strikes :C {} ".format(username_lower))


def addStrike(bot, update, args):
    if len(args) == 0:
        return

    userSender = str(update.message.from_user).lower()

    if userSender == "@dammagor":
        addRealStrike(bot, update, args)
    else:
        addDummyStrike(bot, update, args)


strike_handler = CommandHandler('addStrike', addStrike, pass_args=True)

dispatcher.add_handler(strike_handler)

# Start Bot
updater.start_polling()

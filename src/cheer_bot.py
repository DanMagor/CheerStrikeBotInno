from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler

TOKEN = open("../token.txt", "r").read()

userStrikes = {}

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
    strike_key = "realStrikes"

    if username_lower not in userStrikes:
        userStrikes[username_lower] = {strike_key: 0, "dummyStrike": 0}
        userStrikes[username_lower][strike_key] = 1
    else:
        userStrikes[username_lower][strike_key] = userStrikes[username_lower][strike_key] + 1

    if userStrikes[username_lower][strike_key] + userStrikes[username_lower]["dummyStrike"] < 3:
        bot.send_message(chat_id=update.message.chat_id,
                         text="Cheerleader {} now has {} strike(s)!".format(username_formatted,
                                                                            userStrikes[username_lower][strike_key] +
                                                                            userStrikes[
                                                                                username_lower]["dummyStrike"]))
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Too much strikes :C {} ".format(username_lower))


def addDummyStrike(bot, update, args):
    username_formatted = args[0]
    username_lower = str(args[0]).lower()

    if username_lower == "@danmagor":
        bot.send_message(chat_id=update.message.chat_id,
                         text="LoL, Nope :)")
        return
    strike_key = "dummyStrikes"

    if username_lower not in userStrikes:
        userStrikes[username_lower] = {strike_key: 0, "realStrikes": 0}
        userStrikes[username_lower][strike_key] = 1
    else:
        userStrikes[username_lower][strike_key] = userStrikes[username_lower][strike_key] + 1

    if userStrikes[username_lower][strike_key] + userStrikes[username_lower][strike_key] < 3:
        bot.send_message(chat_id=update.message.chat_id,
                         text="Cheerleader {} now has {} strike(s)!".format(username_formatted,
                                                                            userStrikes[username_lower][strike_key] +
                                                                            userStrikes[
                                                                                username_lower]["realStrikes"]))
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Too much strikes :C {} ".format(username_lower))


def addStrike(bot, update, args):
    if len(args) == 0:
        return

    userSender = str(update.message.from_user.username).lower()

    if userSender == "danmagor":
        addRealStrike(bot, update, args)
    else:
        addDummyStrike(bot, update, args)


strike_handler = CommandHandler('addStrike', addStrike, pass_args=True)

dispatcher.add_handler(strike_handler)

# Start Bot
updater.start_polling()

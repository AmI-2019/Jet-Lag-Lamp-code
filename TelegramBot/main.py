from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from commandHandler import start, logout, about_the_team, login,echo
from reply_inline_module import *

# Main function definition
def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("650299894:AAH8mFuD7EtvY31GiOuC0OiM-m6_PphGbcY", use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('echo', echo))
    updater.dispatcher.add_handler(CommandHandler('login', login))
    updater.dispatcher.add_handler(CommandHandler('logout', logout))
    updater.dispatcher.add_handler(CommandHandler('about_the_team', about_the_team))
    updater.dispatcher.add_handler(CallbackQueryHandler(reply_inline))
    # not working: updater.dispatcher.add_handler(CallbackQueryHandler(replyInline))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()

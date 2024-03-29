from telegram import InlineKeyboardButton, InlineKeyboardMarkup, replymarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram import ChatAction

# define command handlers:
def start(update, context):
    custom_keyboard = [[KeyboardButton('/login'), KeyboardButton('/logout')],
                       [KeyboardButton('/about_the_team'), KeyboardButton(text='Help')], ]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=False, resize_keyboard=True)
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Let's begin!",
                             reply_markup=reply_markup)


def login(update, context):
    login_sing_up = [
        [InlineKeyboardButton("LOGIN", callback_data="login"),
         InlineKeyboardButton("SING UP", callback_data="singup")],
    ]
    reply_markup = InlineKeyboardMarkup(login_sing_up)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def logout(update, context):
    yes_no = [
        [InlineKeyboardButton("yes", callback_data="yes"),
         InlineKeyboardButton("no", callback_data="no")],
    ]
    reply_markup = InlineKeyboardMarkup(yes_no)
    update.message.reply_text('Are you sure yo want to logout?', reply_markup=reply_markup)


def about_the_team(update, context):
    teamComponents = [
        [InlineKeyboardButton("Fabio Baldo", callback_data="fabio"),
         InlineKeyboardButton("Marion Durafour", callback_data="marion")],
        [InlineKeyboardButton("Vincent Gautier", callback_data="vincent"),
         InlineKeyboardButton("Alessandro Bugliarelli", callback_data="alessandro")],
    ]
    reply_markup = InlineKeyboardMarkup(teamComponents)
    update.message.reply_text('Our team is composed of 4 people. About who you wanna learn more?',
                              reply_markup=reply_markup)


# TODO:new command handlers

'''



'''

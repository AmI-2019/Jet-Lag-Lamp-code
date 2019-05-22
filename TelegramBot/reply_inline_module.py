from telegram import InlineKeyboardButton, InlineKeyboardMarkup, replymarkup, ReplyKeyboardMarkup, KeyboardButton

def reply_inline(update, context):
    # query di ritorno
    query = update.callback_query
    q = query.data
    # about_the_team

    # dictionary of the team components
    #TODO write something about each onde

    team_components={
        "fabio":"my name is...",
        "marion":"my surname is",
        "vincent":"first man on the moon",
        "alessandro":"jekill boss"
    }
    if q=='fabio' or q=='vincent' or q=='alessandro' or q=='marion':
        context.bot.edit_message_text(text=team_components[q],
                                  chat_id=query.message.chat_id,
                                  message_id=query.message.message_id)

    login_menu={
        "singup":"Wanderfull, now you have to enter all your data!",
        "login":"Please enter your id"
    }
    if q == 'singup':
        context.bot.send_message(text=login_menu[q],
                                        chat_id=query.message.chat_id,
                                     message_id=query.message.message_id)

    elif q == 'login':
        login_id_password = [
            [InlineKeyboardButton("ID", callback_data="id"),
            InlineKeyboardButton("PASSWORD", callback_data="password")],
        ]
        reply_markup = InlineKeyboardMarkup(login_id_password)
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text="Choose what you want to enter",
                                 reply_markup=reply_markup)
    logout_menu={
        "yes":"Ok, you are logout.",
        "no":"Ok, nothing has been done."
    }
    # Logout the user
    if q=='yes':
        # to be compleated
        print('logout')

    if q == 'yes' or q == 'no':
        context.bot.edit_message_text(text=logout_menu[q],
                                        chat_id=query.message.chat_id,
                                     message_id=query.message.message_id)

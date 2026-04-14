@bot.message_handler(func=lambda message: message.text == '🎰 START ANALYSIS')
def game_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    # Video wale games
    btn1 = types.KeyboardButton('🔴 55 CLUB')
    btn2 = types.KeyboardButton('🟢 LOTTERY 7')
    btn3 = types.KeyboardButton('🟡 TIRANGA')
    btn4 = types.KeyboardButton('🔵 JALWA GAME')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, "🎯 **Select Your Game:**", reply_markup=markup, parse_mode='Markdown')


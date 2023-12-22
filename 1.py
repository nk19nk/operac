import telebot
import random

TOKEN = '6589778521:AAEq7EUmL41iCrbo38N9IQqmw5iTNMg4lAk'

bot = telebot.TeleBot(TOKEN)

sticks = 20  # Начальное количество палочек

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Добро пожаловать! Это игра в палочки. На столе лежат 20 палочек.")

@bot.message_handler(func=lambda message: True)
def game(message):
    global sticks
    try:
        num = int(message.text)
        if num < 1 or num > 3:
            bot.reply_to(message, "Можно взять только 1, 2 или 3 палочки.")
        else:
            sticks -= num
            if sticks <= 0:
                bot.reply_to(message, f"Вы взяли последнюю палочку(и) и выиграли!")
                sticks = 20
            else:
                bot.reply_to(message, f"Вы взяли {num} палочки. Осталось {sticks} палочек.")
                bot.send_message(message.chat.id, "Теперь мой ход...")
                b=random.randint(1, 3)
                sticks -= b
                if sticks <= 0:
                    bot.reply_to(message, f"Я взял последнюю палочку(и) и выиграл!")
                    sticks = 20
                else:
                    bot.send_message(message.chat.id, f"Я взял {b} палочки. Осталось {sticks} палочек.")           
    except ValueError:
        bot.reply_to(message, "Пожалуйста, введите число от 1 до 3.")

bot.polling()

import telebot
import random
TOKEN = '6589778521:AAEq7EUmL41iCrbo38N9IQqmw5iTNMg4lAk'
bot = telebot.TeleBot(TOKEN)
sticks = 20  # Начальное количество палочек
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f"Добро пожаловать! Это игра в палочки. На столе лежат 20 палочек.")
@bot.message_handler(func=lambda message: True) #функция должна быть вызывана для каждого входящего сообщения в чате
def game(message):
    global sticks
    try:
        num = int(message.text) #преобразвонное введенным сообщением число
        if num < 1 or num > 3: #диапазон допустимых значений
            bot.reply_to(message, f"Можно взять только 1, 2 или 3 палочки.")
        else:
            sticks -= num #остаток палочек после хода игрока
            if sticks <= 0:
                bot.reply_to(message, f"Вы взяли последнюю палочку(и) и выиграли!")
                sticks = 20 #новый запуск игры
            else:
                bot.reply_to(message, f"Вы взяли {num} палочки. Осталось {sticks} палочек.")
                bot.send_message(message.chat.id, "Теперь мой ход...")
                s=random.randint(1, 3) #ход компьютера
                sticks -= s #остаток палочек после хода компьютера
                if sticks <= 0:
                    bot.reply_to(message, f"Я взял последнюю палочку(и) и выиграл!")
                    sticks = 20 #новый запуск игры
                else:
                    bot.send_message(message.chat.id, f"Я взял {s} палочки. Осталось {sticks} палочек.")           
    except ValueError: #водд 0, или числа больше 3, или другого неподходящего символа
        bot.reply_to(message, f"Пожалуйста, введите число от 1 до 3.")
bot.polling()

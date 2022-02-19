from dotenv import load_dotenv
import os 
import telebot
from get_weather import get_weather



load_dotenv()
token = os.environ.get('TELEGRAM_TOKEN')
# print(token)

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, 'Привет. Я бот погоды. Введите название города')




# @bot.message_handler(content_types=["text"])
# def show_weather(message):
# 	weather, degrees = get_weather(message.text)
# 	bot.send_message(message.chat.id, "Погода в " + message.text + ': ' + weather + ', температура: ' + str(degrees))

@bot.message_handler(content_types=["text"])
def show_weather(message):
	try:
		weather, degrees = get_weather(message.text)
		bot.send_message(message.chat.id, "Погода в " + message.text + ': ' + weather + ', температура: ' + str(degrees))
	except TypeError:
		bot.send_message(message.chat.id, "Введите название города правильно!")

bot.polling()

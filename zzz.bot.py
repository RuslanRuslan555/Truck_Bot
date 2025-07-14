import telebot
import requests

API_TOKEN = " ******** "
bot = telebot.TeleBot(API_TOKEN)
API_URL = "http://127.0.0.1:8000/drivers"


@bot.message_handler(commands=['drivers'])
def response_command(message):
    
    response = requests.get(API_URL)
    data = response.json()
    drivers = data.get("drivers", [])

    if not drivers:
        bot.send_message(message.chat.id, "Пусто")
    else:
        reply = "\n\n".join(drivers)
        bot.send_message(message.chat.id, f"\n\n{reply}")
    
bot.polling()


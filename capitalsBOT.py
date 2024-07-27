# step-1

# AIMER Society - Indian Servers
# pip install pyTelegramBotAPI
# pip install pycountry
# pip install geonamescache

# step-2

import telebot
import pycountry
from geonamescache import GeonamesCache

API_TOKEN = '7227456546:AAFWMYY9nY31HtI4n9_uPXVq3s9k4XCfKlc'
bot = telebot.TeleBot(API_TOKEN)
gc = GeonamesCache()

countries_capitals = {
    'United States': 'Washington, D.C.',
    'Canada': 'Ottawa',
    'India': 'New Delhi',
    'Germany': 'Berlin',
    'France': 'Paris',
    'Spain': 'Madrid',

    # Add more countries and capitals here
}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Send me the name of a country, and I'll tell you its capital.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    country_names = message.text.split(',')
    print(message)
    capitals = []
    for country_name in country_names:
        country_name = country_name.strip()
        capital = countries_capitals.get(country_name, "Not found")
        capitals.append((country_name, capital))

    response = "\n".join([f"The capital of {country} is {capital}." for country, capital in capitals])
    bot.reply_to(message, response)
bot.polling()

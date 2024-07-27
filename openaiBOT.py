# step-1

# AIMER Society - Indian Servers
# pip install pyTelegramBotAPI
# pip install openai
# pip install google-generativeai #For Google Gemini AIMERS
# pip install anthropic
TelegramBOT_TOKEN = '7075200335:AAHZRHwZ1PCu8sUCfcXY1pEGXmCavzp7xkM'

#step-2

#Latest version
import telebot
import os
import openai
from openai import OpenAI


OPENAI_API_KEY = "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"
client = OpenAI(api_key=OPENAI_API_KEY)


bot = telebot.TeleBot(TelegramBOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! The MOST POWERFUL AI BOT from Mahesh")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
 try :
  print(message)
  completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": message.text},
  ]
    )
  bot.reply_to(message, completion.choices[0].message.content)
 except Exception as e:
        print(f"An error occurred: {e}")
        bot.reply_to(message, "Sorry, I couldn't process your request.")

bot.polling()
# step-1

# AIMER Society - Indian Servers
# pip install pyTelegramBotAPI
# pip install openai
# pip install google-generativeai #For Google Gemini AIMERS
# pip install anthropic
TelegramBOT_TOKEN = '7075200335:AAHZRHwZ1PCu8sUCfcXY1pEGXmCavzp7xkM'

# step-2

#Latest version #Gemini API #AIMER Society #IndianServers
import telebot
import os

import google.generativeai as genai

genai.configure(api_key="AIzaSyC6techBpi4OTSC06U1g4DDnNN53md6ZO8")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
])

bot = telebot.TeleBot(TelegramBOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! The MOST POWERFUL AI BOT from Mahesh")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
 try :
  print(message)
  convo.send_message(message.text)
  bot.reply_to(message, convo.last.text)
 except Exception as e:
        print(f"An error occurred: {e}")
        bot.reply_to(message, "Sorry, I couldn't process your request.")

bot.polling()
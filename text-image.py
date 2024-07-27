# step-1
# pip install pyTelegramBotAPI requests
# pip install torch diffusers
# pip install accelerate
# pip install transformers

# step-2̥

import telebot
import requests
from PIL import Image
import io
from diffusers import StableDiffusionPipeline
import torch


# Set up the bot with your token
bot_token = '7227456546:AAFWMYY9nY31HtI4n9_uPXVq3s9k4XCfKlc'
bot = telebot.TeleBot(bot_token)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Retrieve the message text
    text = message.text

    model_id = "dreamlike-art/dreamlike-photoreal-2.0"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")
    prompt = text
    image = pipe(prompt).images[0]
    bot.send_photo(message.chat.id, image)


bot.polling()
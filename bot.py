#!/usr/bin/env python3

import time
import logging
import telebot
import mscomputervision
from mscomputervision import _mskey
from mscomputervision import msProcessRequest
from translator import *

TOKEN = "" # YOUR BotFather token here
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, '''🇺🇸 Welcome!\n Send me an image\nRate the bot: https://telegram.me/storebot?start=imagevisionbot\n\n
🇧🇷 Bem-vindo!\nEnvie-me uma imagem.\nAvalie o bot: https://telegram.me/storebot?start=imagevisionbot\n\n\n
Desenvolvido com pyTelegramBotAPI, ComputerVision API e Bing Translator API''')

@bot.message_handler(commands=['info'])
def send_welcome(message):
    info = ('Bot ainda em desenvolvimento!\n'
        'Qualquer problema ou sugestão, por favor, fale comigo!\n'
        'Telegram: @moisespedro\n'
        'Avalie o bot: https://telegram.me/storebot?start=imagevisionbot \n')
    bot.reply_to(message, info)

@bot.message_handler(content_types=["photo"])
def answer_photo(message):
	photo = bot.get_file(message.photo[-1].file_id)
	# URL direction to image
	photo_url = "https://api.telegram.org/file/bot{0}/{1}".format(TOKEN, photo.file_path)

	# Computer Vision parameters
	params = { 'visualFeatures' : 'Description'} 

	headers = dict()
	headers['Ocp-Apim-Subscription-Key'] = _mskey
	headers['Content-Type'] = 'application/json' 

	json = { 'url': photo_url } 
	data = None

	result = msProcessRequest( json, data, headers, params )
	msg_en = result['description']['captions'][0]['text']
	msg_pt = translate_en_pt(msg_en)
	msg_persian = translate_en_persian(msg_en)
	bot.send_chat_action(message.chat.id, 'typing')
	time.sleep(1)
	bot.reply_to(message, "🇺🇸 " + msg_en + "\n🇧🇷 " + msg_pt + "\n🇮🇷 " + msg_persian)


@bot.message_handler(func=lambda m: True)
def reply_all(message):
	if message.chat.type == "private":
		bot.reply_to(message, '''🇺🇸 Please send me an image so I can describe it! 
		🇧🇷 Por favor envie uma imagem para que eu possa descrevê-la!
		🇮🇷 لطفا یک عکس ارسال کن تا بتونم توصیفش کنم!''')

bot.polling(none_stop=True)

while True:
    time.sleep(5)
    
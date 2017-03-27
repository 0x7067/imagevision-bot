#!/usr/bin/env python3

from BingTranslator import Translator #importing Translator class for translations.

# Your Bing API credentials here
client_id = ""
client_secret = ""

translator = Translator(client_id, client_secret)

def translate_en_pt(message):
	phrase_translated = translator.translate(message, "pt") #translating phrase
	return phrase_translated
def translate_en_persian(message):
	phrase_translated = translator.translate(message, "fa")
	return phrase_translated
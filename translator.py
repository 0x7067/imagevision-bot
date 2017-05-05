#!/usr/bin/env python3

from yandex_translate import YandexTranslate #importing Translator class for translations.

# Your Yandex API credentials here
translator = YandexTranslate('')

def translate_en_pt(message):
    phrase_translated = translator.translate(message, 'pt') 
    return phrase_translated
def translate_en_persian(message):
    phrase_translated = translator.translate(message, 'fa')
    return phrase_translated
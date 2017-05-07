#!/usr/bin/env python3

# importing Translator class for translations.
from yandex_translate import YandexTranslate

# Your Yandex API credentials here
translator = YandexTranslate('')


def translate_en_pt(message):
    phrase_translated = translator.translate(message, 'pt')
    str = "".join(phrase_translated.get('text'))
    return str


def translate_en_persian(message):
    phrase_translated = translator.translate(message, 'fa')
    str = "".join(phrase_translated.get('text'))
    return str

import speech_recognition as sr
from deep_translator import GoogleTranslator
from tkinter import *
# from tkinter import ttk
import tkinter as tk
import ttkbootstrap as tkk

r = sr.Recognizer()
# translator = Translator()


language_codes = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 
                  'assamese': 'as', 'aymara': 'ay', 'azerbaijani': 'az', 'bambara': 'bm', 'basque': 'eu', 
                  'belarusian': 'be', 'bengali': 'bn', 'bhojpuri': 'bho', 'bosnian': 'bs', 'bulgarian': 'bg', 
                  'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-CN', 
                  'chinese (traditional)': 'zh-TW', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 
                  'danish': 'da', 'dhivehi': 'dv', 'dogri': 'doi', 'dutch': 'nl', 'english': 'en', 
                  'esperanto': 'eo', 'estonian': 'et', 'ewe': 'ee', 'filipino': 'tl', 'finnish': 'fi', 
                  'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 
                  'greek': 'el', 'guarani': 'gn', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 
                  'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 
                  'icelandic': 'is', 'igbo': 'ig', 'ilocano': 'ilo', 'indonesian': 'id', 'irish': 'ga', 
                  'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 
                  'khmer': 'km', 'kinyarwanda': 'rw', 'konkani': 'gom', 'korean': 'ko', 'krio': 'kri', 
                  'kurdish (kurmanji)': 'ku', 'kurdish (sorani)': 'ckb', 'kyrgyz': 'ky', 'lao': 'lo', 
                  'latin': 'la', 'latvian': 'lv', 'lingala': 'ln', 'lithuanian': 'lt', 'luganda': 'lg', 
                  'luxembourgish': 'lb', 'macedonian': 'mk', 'maithili': 'mai', 'malagasy': 'mg', 'malay': 'ms', 
                  'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'meiteilon (manipuri)':'mni-Mtei', 
                  'mizo': 'lus', 'mongolian': 'mn', 'myanmar': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia (oriya)': 'or', 
                  'oromo': 'om', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 
                  'quechua': 'qu', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'sanskrit': 'sa', 'scots gaelic': 'gd', 
                  'sepedi': 'nso', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 
                  'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 
                  'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'tatar': 'tt', 
                  'telugu': 'te', 'thai': 'th', 'tigrinya': 'ti', 'tsonga': 'ts', 'turkish': 'tr', 'turkmen': 'tk', 
                  'twi': 'ak', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 
                  'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

# with sr.Microphone() as source:
#     print("Speak into the microphone!")
#     audio = r.listen(source)
# try:
#     text = r.recognize_google(audio, language='auto') # Automatically detect the source language
#     print("you said " + text)
#     # Translate the text to each of the supported languages
#     translated = GoogleTranslator(source='auto', target=out_code).translate(text)
#     print("In "+ lang + " you said: " + translated)

# except sr.UnknownValueError:
#     print("Sorry, I didn't understand what you said.")
# except sr.RequestError:
#     print("Sorry, I couldn't process your request at this time.")



# Window
window = Tk(className='Speech-To-Text App')
window.geometry("500x300")
window.configure(background='#012a36')

def button_go_func():
    lang = lang_input.get()
    lang.lower()
    out_code = ''
    for language, code in language_codes.items():
        if language == lang:
            out_code = code
            break
    
    with sr.Microphone() as source:
        lang_label.configure(text="Speak into the microphone!")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='auto') # Automatically detect the source language
        lang_label.configure(text="You said: " + text)
        # Translate the text to each of the supported languages
        translated = GoogleTranslator(source='auto', target=out_code).translate(text)
        lang = lang.capitalize()
        lang_output_label.configure(text="In "+ lang + " you said: " + translated)

    except sr.UnknownValueError:
        lang_label.configure(text="Sorry, I didn't understand what you said. Press Go and try again")
    except sr.RequestError:
        lang_label.configure(text="Sorry, I couldn't process your request at this time.")


style = tkk.Style()
style.theme_use('solar')


lang_label = tkk.Label(master=window, text='What language do you want the output as? (Type in all lower case!)')
lang_input = tkk.Entry(master=window)
lang_output_label = tkk.Label(master=window, text='Output will be here')
button_go = tkk.Button(master=window, text='Translate', command=lambda: button_go_func())

# Add padding and spacing to the widgets
lang_label.pack(pady=20)
lang_input.pack(pady=10, ipady=10, padx=10, fill='x')
lang_output_label.pack(pady=20)
button_go.pack(pady=10, ipadx=30, ipady=10, fill='x')

# Add hover effects to the button
button_go.bind('<Enter>', lambda e: button_go.configure(background='#4b88ff'))
button_go.bind('<Leave>', lambda e: button_go.configure(background='#1e90ff'))

# Output window
window.mainloop()

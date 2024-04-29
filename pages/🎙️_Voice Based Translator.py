import os
import time
import pygame
from gtts import gTTS
import streamlit as st
import speech_recognition as sr
from googletrans import Translator
isTranslateOn = False

LANGUAGES = {
    "bn": "Bengali",
    "en": "English",
    "gu": "Gujarati",
    "hi": "Hindi",
    "kn": "Kannada",
    "ml": "Malayalam",
    "mr": "Marathi",
    "ta": "Tamil",
    "te": "Telugu",
    "ur": "Urdu"}
translator = Translator() # Initialize the translator module.
pygame.mixer.init()  # Initialize the mixer module.

st.markdown('''
            <style>
            .st-emotion-cache-17mvwx7.eczjsme5{
             color:black;
             font-weight:bold;
            }
            </style>
            ''',unsafe_allow_html=True)
# Create a mapping between language names and language codes
language_mapping = {name: code for code, name in LANGUAGES.items()}

def get_language_code(language_name):
    return language_mapping.get(language_name, language_name)

def translator_function(spoken_text, from_language, to_language):
    return translator.translate(spoken_text, src='{}'.format(from_language), dest='{}'.format(to_language))

def text_to_voice(text_data, to_language):
    myobj = gTTS(text=text_data, lang='{}'.format(to_language), slow=False)
    myobj.save("cache_file.mp3")
    audio = pygame.mixer.Sound("cache_file.mp3")  # Load a sound.
    audio.play()
    os.remove("cache_file.mp3")

def main_process(output_placeholder, from_language, to_language):
    
    global isTranslateOn
    
    while isTranslateOn:

        rec = sr.Recognizer()
        with sr.Microphone() as source:
            output_placeholder.text("Listening...")
            rec.pause_threshold = 1
            audio = rec.listen(source, phrase_time_limit=10)
        
        try:
            output_placeholder.text("Processing...")
            spoken_text = rec.recognize_google(audio, language='{}'.format(from_language))
            
            output_placeholder.text("Translating...")
            translated_text = translator_function(spoken_text, from_language, to_language)

            text_to_voice(translated_text.text, to_language)
    
        except Exception as e:
            print(e)

# UI layout
st.title("Voice Based Tanslator")

# Dropdowns for selecting languages
from_language_name = st.selectbox("Select Source Language:", list(LANGUAGES.values()))
to_language_name = st.selectbox("Select Target Language:", list(LANGUAGES.values()))

# Convert language names to language codes
from_language = get_language_code(from_language_name)
to_language = get_language_code(to_language_name)

# Button to trigger translation
m = st.markdown("""
<style>
div.stButton > button:first-child {
    font-weight: bold;
    height:50px;
    background-color: black;
    width:300px;
    font-size: 20px;
}
</style>""", unsafe_allow_html=True)

b = st.button("Start 🎙️")
stop_button = st.button("Stop 🚫")
# Check if "Start" button is clicked
if b:
    if not isTranslateOn:
        isTranslateOn = True
        output_placeholder = st.empty()
        main_process(output_placeholder, from_language, to_language)

# Check if "Stop" button is clicked
if stop_button:
    isTranslateOn = False

st.markdown('')
st.markdown('''<b style="color:#FF5733;">Important Notice:</b> Please Turn On The Microphone Of Your Device Before Using This App.''',unsafe_allow_html=True)
st.markdown('**Steps For How To Use:**')
st.markdown('**1.** First Select The Language You Speak Or Any Language You Want To Use.')
st.markdown('**2.** After Selecting First Langauage Now, Select The Second Language.')
st.markdown('**3.** After Selecting Both Langauages Now Press Start 🎙️ Button and Speak')
st.markdown('**4.** It Is A Automatic Translator So You Dont Have To Press Start Repetitively.')
st.markdown('**5.** To Stop The App Simply, Press Stop 🚫 Button.')
footer="""<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: black;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p style='display: block; color:white; text-align: center; padding-top:10px;  font-weight: bold;' >Made With ❤️ By Kartik (leader) and Team.</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
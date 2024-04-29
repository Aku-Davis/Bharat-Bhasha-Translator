import streamlit as st
from mtranslate import translate
import pandas as pd
import os
from gtts import gTTS
import base64

# read language dataset
df = pd.read_excel(os.path.join('language.xlsx'),sheet_name='wiki')
df.dropna(inplace=True)
lang = df['name'].to_list()
langlist=tuple(lang)
langcode = df['iso'].to_list()

# create dictionary of language and 2 letter langcode
lang_array = {lang[i]: langcode[i] for i in range(len(langcode))}

# layout
st.title("Text Based Translator")
inputtext = st.text_area("Enter Text You Want To Translate:")

choice = st.selectbox('Select Language:',langlist)

speech_langs = {
    "bn": "Bengali",
    "en": "English",
    "gu": "Gujarati",
    "hi": "Hindi",
    "kn": "Kannada",
    "ml": "Malayalam",
    "mr": "Marathi",
    "ta": "Tamil",
    "te": "Telugu",
    "ur": "Urdu",
    "pa": "Punjabi"
}

# function to decode audio file for download
def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href=""></a>'
    return href
st.markdown('''
            <style>
            .st-emotion-cache-17mvwx7.eczjsme5{
             color:black;
             font-weight:bold;
            }
            </style>
            ''',unsafe_allow_html=True)
c1,c2 = st.columns([4,3])

# I/O
if len(inputtext) > 0 :
    try:
        output = translate(inputtext,lang_array[choice])
        with c1:
            st.text_area("Translated Text:",output,height=200,placeholder="Enter Text Here")
        # if speech support is available will render autio file
        if choice in speech_langs.values():
            with c2:
                aud_file = gTTS(text=output, lang=lang_array[choice], slow=False)
                aud_file.save("lang.mp3")
                audio_file_read = open('lang.mp3', 'rb')
                audio_bytes = audio_file_read.read()
                bin_str = base64.b64encode(audio_bytes).decode()
                st.audio(audio_bytes, format='audio/mp3')
                st.markdown(get_binary_file_downloader_html("lang.mp3", 'Audio File'), unsafe_allow_html=True)
    except Exception as e:
        st.error(e)
st.markdown('')
st.markdown('''<b style="color:#FF5733;">Important Notice:</b> By Default It Requires English Language Text But You Can Also Enter Indian Languages Text.''',unsafe_allow_html=True)
st.markdown('**Steps For How To Use:**')
st.markdown('**1.** Enter Text You Want To Translate In First Box.')     
st.markdown('**2.** After Entering The Text Now, Select The Language You Want To Translate Text In.')
st.markdown('**3.** Its An Automatic Text Translator, So You Just Need To Enter Text In Textbox.')   
st.markdown('**4.** You Can See The Translated Text In Second Box.')
st.markdown('**5.** There Is Also One Audio File Is Automatically Genrated You Can Listen To Translated Text.')  
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
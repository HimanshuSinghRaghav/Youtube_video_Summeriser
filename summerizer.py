import os
import streamlit as st
import google.generativeai as genai

from dotenv import load_dotenv
import tiktoken
from youtube_transcript_api import YouTubeTranscriptApi

load_dotenv()

st.title("Youtube Video Summariser")

st.sidebar.title("Video URL")


url = st.sidebar.text_input(f"URL ")
GOOGLE_API_KEY = st.sidebar.text_input("Enter your key")
print(GOOGLE_API_KEY)
submit = st.button("Summarise")
language_codes = [
    "af",  # Afrikaans
    "ak",  # Akan
    "sq",  # Albanian
    "am",  # Amharic
    "ar",  # Arabic
    "hy",  # Armenian
    "as",  # Assamese
    "ay",  # Aymara
    "az",  # Azerbaijani
    "bn",  # Bangla
    "eu",  # Basque
    "be",  # Belarusian
    "bho",  # Bhojpuri
    "bs",  # Bosnian
    "bg",  # Bulgarian
    "my",  # Burmese
    "ca",  # Catalan
    "ceb",  # Cebuano
    "zh-Hans",  # Chinese (Simplified)
    "zh-Hant",  # Chinese (Traditional)
    "co",  # Corsican
    "hr",  # Croatian
    "cs",  # Czech
    "da",  # Danish
    "dv",  # Divehi
    "nl",  # Dutch
    "en",  # English
    "eo",  # Esperanto
    "et",  # Estonian
    "ee",  # Ewe
    "fil",  # Filipino
    "fi",  # Finnish
    "fr",  # French
    "gl",  # Galician
    "lg",  # Ganda
    "ka",  # Georgian
    "de",  # German
    "el",  # Greek
    "gn",  # Guarani
    "gu",  # Gujarati
    "ht",  # Haitian Creole
    "ha",  # Hausa
    "haw",  # Hawaiian
    "iw",  # Hebrew
    "hi",  # Hindi
    "hmn",  # Hmong
    "hu",  # Hungarian
    "is",  # Icelandic
    "ig",  # Igbo
    "id",  # Indonesian
    "ga",  # Irish
    "it",  # Italian
    "ja",  # Japanese
    "jv",  # Javanese
    "kn",  # Kannada
    "kk",  # Kazakh
    "km",  # Khmer
    "rw",  # Kinyarwanda
    "ko",  # Korean
    "kri",  # Krio
    "ku",  # Kurdish
    "ky",  # Kyrgyz
    "lo",  # Lao
    "la",  # Latin
    "lv",  # Latvian
    "ln",  # Lingala
    "lt",  # Lithuanian
    "lb",  # Luxembourgish
    "mk",  # Macedonian
    "mg",  # Malagasy
    "ms",  # Malay
    "ml",  # Malayalam
    "mt",  # Maltese
    "mi",  # Māori
    "mr",  # Marathi
    "mn",  # Mongolian
    "ne",  # Nepali
    "nso",  # Northern Sotho
    "no",  # Norwegian
    "ny",  # Nyanja
    "or",  # Odia
    "om",  # Oromo
    "ps",  # Pashto
    "fa",  # Persian
    "pl",  # Polish
    "pt",  # Portuguese
    "pa",  # Punjabi
    "qu",  # Quechua
    "ro",  # Romanian
    "ru",  # Russian
    "sm",  # Samoan
    "sa",  # Sanskrit
    "gd",  # Scottish Gaelic
    "sr",  # Serbian
    "sn",  # Shona
    "sd",  # Sindhi
    "si",  # Sinhala
    "sk",  # Slovak
    "sl",  # Slovenian
    "so",  # Somali
    "st",  # Southern Sotho
    "es",  # Spanish
    "su",  # Sundanese
    "sw",  # Swahili
    "sv",  # Swedish
    "tg",  # Tajik
    "ta",  # Tamil
    "tt",  # Tatar
    "te",  # Telugu
    "th",  # Thai
    "ti",  # Tigrinya
    "ts",  # Tsonga
    "tr",  # Turkish
    "tk",  # Turkmen
    "uk",  # Ukrainian
    "ur",  # Urdu
    "ug",  # Uyghur
]
if submit:
    print("button clicked")
    video_id=url.split("=")[1]
    print(video_id)
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=language_codes)
    print(transcript)
    doc = ""
    for line in transcript:
        doc =doc+ ' ' + line['text']
    print(type(doc))
    print(doc)

    paragraph=" ".join(doc)
    print(paragraph)
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f"summerize this peragraph in 100 words:-  f{paragraph}")
    st.write(response.text)











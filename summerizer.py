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
if submit:
    print("button clicked")
    video_id=url.split("=")[1]
    print(video_id)
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['hi'])
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











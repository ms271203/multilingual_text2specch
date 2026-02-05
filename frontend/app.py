
import streamlit as st
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.language_detector import detect_language
from backend.emotion_detector import detect_emotion
from backend.tts_engine import text_to_speech

st.set_page_config(page_title="Emotion Aware TTS", page_icon="🎙️", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #e0f2fe, #fdf2f8);
}
h1, h2 {
    color: #1e3a8a;
}
.stButton>button {
    background: linear-gradient(to right, #6366f1, #4f46e5);
    color: white;
    border-radius: 12px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

st.title("🎙️ Emotion Aware Multilingual Text to Speech")
st.write("Supports English, Hindi, Marathi")

text = st.text_area("✍️ Enter text", height=150)

if st.button("🔊 Generate Speech"):
    if text.strip():
        lang = detect_language(text)
        emotion = detect_emotion(text)
        audio_path = text_to_speech(text, lang)
        st.success(f"Language: {lang} | Emotion: {emotion}")
        st.audio(audio_path)
    else:
        st.warning("Please enter some text")

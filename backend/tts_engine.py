
from gtts import gTTS
import time

def text_to_speech(text, language):
    lang_map = {"English":"en","Hindi":"hi","Marathi":"mr"}
    tts = gTTS(text=text, lang=lang_map.get(language,"en"))
    filename = f"audio_{int(time.time())}.mp3"
    tts.save(filename)
    return filename

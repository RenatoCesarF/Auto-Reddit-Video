from gtts import gTTS
import os

def default_text_to_speak(text: str, filename: str):
    language = 'en'
    try:
        myobj = gTTS(text=text, lang=language, slow=False)
        myobj.save(filename)
    except:
        return filename
    return filename

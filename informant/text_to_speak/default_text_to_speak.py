from gtts import gTTS
import os


def default_text_to_speak(text: str, filename: str):
    language = 'en'

    myobj = gTTS(text=text, lang=language, slow=False)
    path = myobj.save(filename)
    return path

from classes.voices import Voice
from text_to_speak.tik_tok_text_to_speak import tik_tok_text_to_speak


for v in Voice:
    print(v)
    tik_tok_text_to_speak("THis is a test of every single voice of tiktok", 
                          f"./test_{v}.mp3",
                          voice=v)

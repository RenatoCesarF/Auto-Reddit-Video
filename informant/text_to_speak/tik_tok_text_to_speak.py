import requests, base64
import os
from text_to_speak.voices import Voice

DEFAULT_API_PATH = 'https://api16-normal-useast5.us.tiktokv.com/media/api'

def text_to_speak(text: str,  filename: str, voice = Voice.EN_US_002):
    if text.__len__() < 5:
        raise Exception(f"To short text {text}")
    
    url = format_api_url(text_speaker=voice, req_text=text)

    res = requests.post(url)
    dictResponse = res.json()
    vstr = [dictResponse["data"]["v_str"]][0]

    return save_mp3(vstr, filename)
 
def format_api_url(text_speaker: Voice, req_text: str) -> str:
    req_text = req_text.replace("+", "plus")
    req_text = req_text.replace(" ", "+")
    req_text = req_text.replace("&", "and")
    return  f"{DEFAULT_API_PATH}/text/speech/invoke/?text_speaker={text_speaker}&req_text={req_text}&speaker_map_type=0"

def save_mp3(vstr: str, path: str):
    b64d = base64.b64decode(vstr)
    isExist = os.path.exists(path)
    
    out = open(path, "wb")
    out.write(b64d)
    out.close()
    
    return path
    

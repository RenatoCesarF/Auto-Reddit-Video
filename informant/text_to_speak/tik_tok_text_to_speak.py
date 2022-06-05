import requests, base64

from voices import Voice

DEFAULT_API_PATH = 'https://api16-normal-useast5.us.tiktokv.com/media/api'

def main():
    text_to_speak(text="Todo porco que é preto gosta de mochila branca", 
                   filename='./audio/teest.mp3')


def text_to_speak(voice = Voice.EN_US_002, text: str = "TikTok Text To Speech", 
                    filename: str = 'voice.mp3'):
    url = format_api_url(text_speaker=voice, req_text=text)
    r = requests.post(url)

    vstr = [r.json()["data"]["v_str"]][0]
    msg = [r.json()["message"]][0]

    b64d = base64.b64decode(vstr)

    out = open(filename, "wb")
    out.write(b64d)
    out.close()

    print(f"\n{msg.capitalize()}")

def format_api_url(text_speaker: Voice, req_text: str) -> str:
    req_text = req_text.replace("+", "plus")
    req_text = req_text.replace(" ", "+")
    req_text = req_text.replace("&", "and")
    return  f"{DEFAULT_API_PATH}/text/speech/invoke/?text_speaker={text_speaker}&req_text={req_text}&speaker_map_type=0"

if __name__ == "__main__":
    main()


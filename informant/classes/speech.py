import audioread
from text_to_speak.default_text_to_speak import default_text_to_speak
from text_to_speak.tik_tok_text_to_speak import tik_tok_text_to_speak

class Speech:
    path: str
    file_path: str
    lenght_in_seconds: int
    
    def __init__(self, text: str, file_name: str):
        print(f"[PROCESS] Generating speech for: '{text[0:30]}...'")
        self.file_path = f"../producer/public/audios/{file_name}.wav"
        
        if len(text) < 200:
            tik_tok_text_to_speak(text, filename=self.file_path)
        else:
            default_text_to_speak(text, filename=self.file_path)
        
        self.path = f'/audios/{file_name}.wav'
        print("[PROCESS] Calculating audio lenght")
        self.lenght_in_seconds = self._get_lenght_in_seconds()
        
    def _get_lenght_in_seconds(self):
        with audioread.audio_open(self.file_path) as f:
            print(f.duration)
            return f.duration 
        
               
    def toJson(self) -> dict:
        dictObject = { 
            'lenght': self.lenght_in_seconds,
            'path': self.path
        }
        
        return dictObject;

    
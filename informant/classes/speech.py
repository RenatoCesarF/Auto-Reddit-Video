import audioread
from enum import Enum

from text_to_speak.default_text_to_speak import default_text_to_speak
from text_to_speak.tik_tok_text_to_speak import tik_tok_text_to_speak



class SpeechType(Enum):
    def __str__(self):
        return str(self.value)
    TIKTOK= 0
    DEFAULT= 1
 

class Speech:
    path: str
    file_path: str
    lenght_in_seconds: int
    
    def __init__(self, text: str, file_name: str, speech_type: SpeechType = SpeechType.DEFAULT):
        print(f"[PROCESS] Generating speech for: '{text[0:30]} [...]'")
        self.file_path = f"../producer/public/audios/{file_name}.wav"
        self.path = f'/audios/{file_name}.wav'
        
        if speech_type == SpeechType.TIKTOK:
            tik_tok_text_to_speak(text, filename=self.file_path)
        else:
            default_text_to_speak(text, filename=self.file_path)
        
        print("[PROCESS] Calculating audio lenght")
        self.lenght_in_seconds = self._get_lenght_in_seconds()
    
    def _get_lenght_in_seconds(self):
        with audioread.audio_open(self.file_path) as f:
            return f.duration 
        
               
    def toJson(self) -> dict:
        dictObject = { 
            'lenght': self.lenght_in_seconds,
            'path': self.path
        }
    
        return dictObject;

    @staticmethod
    def get_speech_type(phrases: list) -> SpeechType:
        for phrase in phrases:
            if len(phrase) > 200:
                return SpeechType.DEFAULT
            
        return SpeechType.TIKTOK
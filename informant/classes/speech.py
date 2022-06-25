import audioread
from enum import Enum

from text_to_speak.default_text_to_speak import default_text_to_speak
from text_to_speak.tik_tok_text_to_speak import tik_tok_text_to_speak


class SpeechType(Enum):
    def __str__(self):
        return str(self.value)
    TIKTOK= "TIKTOK"
    GTTS= "GTTS"
 

class Speech:
    """Create a audio from a string, it receeves the relative path + filename and a speech type
    \n:param: text (str): to be transformed into an audio
    \n:param: file_path (str): the relative path where the file will be saved at and name of the file;
    \n:param: speech_type (SpeechType): the speech algorithm that will be used, it can be tiktok (for 200 characters) or GTTS for bigger texts
    """
    path: str
    file_path: str
    lenght_in_seconds: int

    def __init__(self, text: str, file_path: str, speech_type: SpeechType = SpeechType.GTTS):
        log(LogType.INFO, f"Generating speech for:'{text[0:30]} ...'")
        self.file_path = f"../producer/public/audios/{file_path}.wav"
        self.path = f'/audios/{file_path}.wav'
        
        if speech_type == SpeechType.TIKTOK:
            tik_tok_text_to_speak(text, filename=self.file_path)
        else:
            default_text_to_speak(text, filename=self.file_path)
        
        self.lenght_in_seconds = self._get_lenght_in_seconds()
        log(LogType.INFO, f"Calculated audio lenght {self.lenght_in_seconds}")
    
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
                return SpeechType.GTTS
            
        return SpeechType.TIKTOK
    
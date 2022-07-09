import audioread
from time import sleep
from os import remove as os_remove
from enum import Enum

from text_to_speak.default_text_to_speak import default_text_to_speak
from text_to_speak.tik_tok_text_to_speak import tik_tok_text_to_speak
from utils.log import log

class SpeechType(Enum):
    TIKTOK= "TIKTOK"
    GTTS= "GTTS"
    
    def __str__(self):
        return str(self.value)
 

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
        log.info(f"Generating speech for:'{text[0:30]} ...'")
        self.file_path = file_path
        self.text = text

        self.generate_audio_with_type(speech_type)
        
        self.lenght_in_seconds = self._get_lenght_in_seconds()
        log.info(f"Calculated audio lenght {self.lenght_in_seconds}")
    
    def generate_audio_with_type(self, speech_type):
        if speech_type == SpeechType.TIKTOK:
            tik_tok_text_to_speak(self.text, filename=self.file_path)
        else:
            default_text_to_speak(self.text, filename=self.file_path)
        log.info(f"Saved mp3 file in {self.file_path}")
    
    def set_path(self, new_path):
        self.path = new_path
    
    def delete_generated_file(self):
        os_remove(self.file_path)
        
    def _get_lenght_in_seconds(self):
        with audioread.audio_open(self.file_path) as f:
            return f.duration 
                       
    def to_json(self) -> dict:
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
    
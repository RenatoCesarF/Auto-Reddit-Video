import audioread
from text_to_speak.default_text_to_speak import default_text_to_speak

class Speech:
    path: str
    file_name: str
    file_path: str
    lenght_in_seconds: int
    
    def __init__(self, text: str, file_name: str):
        if text is None or str(text) == "null" or not text:
            raise Exception("Speech received a null or none text to translate")
        
        print(f"[PROCESS] Generating speech for: '{text[0:30]}...'")
        self.file_name = file_name
        self.file_path = f"../producer/public/audios/{self.file_name}.wav"
        
        default_text_to_speak(text, filename=self.file_path)
        
        self.path = f'/audios/{self.file_name}.wav'
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

    
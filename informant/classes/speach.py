import audioread
from text_to_speak.default_text_to_speak import default_text_to_speak


class Speach:
    path: str
    file_name: str
    lenght_in_seconds: int
    
    def __init__(self, text: str,file_name: str):
        default_text_to_speak(text, filename=f'../audios/{file_name}.wavaaa')
        self.file_name = file_name
        self.path = f'../../../audios/{self.file_name}.wav'
        self.lenght_in_seconds = self._get_lenght_in_seconds()
        
    def _get_lenght_in_seconds(self):
        with audioread.audio_open(f'../audios/{self.file_name}.wav') as f:
            return f.duration
        
               
    def toJson(self) -> dict:
        dictObject = {
            # 'text': self.text, 
            'lenght': self.lenght_in_seconds,
            'path': self.path
        }
        
        return dictObject;

    
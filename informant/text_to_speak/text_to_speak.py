from gtts import gTTS
import os
  
mytext = 'Welcome to auto reddit videos!'
language = 'en'
  
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("audio/welcome.mp3")
  

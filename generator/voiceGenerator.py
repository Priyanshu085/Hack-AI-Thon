import os
from gtts import gTTS
import requests



def Text_voice(texts,i):
  language = 'en'
  output= gTTS(text=texts,lang=language,slow=False)
  output.save(f"output{i}.mp3")
  os.system(f"start output{i}.mp3")

def voice_text(i):
    url="https://whisper.lablab.ai/asr"
    payload={}
    files=[
        ('audio_file',('output.mp3',open(f'output1.mp3','rb'),'audio/mpeg'))
    ]
    response=requests.request("POST",url,data=payload,files=files)
    response=response.json()
    return(response["text"])
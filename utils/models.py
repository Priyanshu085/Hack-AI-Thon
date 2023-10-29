import os
import openai 
import requests
from gtts import gTTS
from PIL import Image

# Text Generation Model
def description(text):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=text,
    temperature=0.2,
    max_tokens=250,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )
  
  ans=response.choices[0].text
  return (ans)

def concept_keypoints(text):
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt=text,
  temperature=0.2,
  max_tokens=1500,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
  )
  ans=response.choices[0].text
  return ans


# Image Generation Model
def generate_IMG(description,i):
  images = openai.Image.create(
    prompt=description,
    n=2,
    size="512x512"
  )
  
  image_url = images['data'][0]['url']
  img = Image.open(requests.get(image_url, stream = True).raw)
  img.save(f'output{i}.png')
  file=Image.open('output0.png')
  return file

# Voice Generation Model
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

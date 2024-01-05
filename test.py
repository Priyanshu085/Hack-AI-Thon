import streamlit as st
import gtts
import os 
#import playsound
from pydub import AudioSegment
from pydub.playback import play




slot = st.empty()
text = st.text_input('Enter ')

def Text_voice(texts,i):
  language = 'en'
  output= gtts.gTTS(text=texts,lang=language,slow=False)
  output.save(f"output{i}.wav")
  sound = AudioSegment.from_wav(f"output{i}.wav")
  play(sound)
  # os.system(f"start output{i}.mp3")
 # playsound.playsound(f"output{i}.mp3")

if(text):
  if st.button("Read Lines"):
    slot.empty()
    Text_voice(texts=text, i=1)
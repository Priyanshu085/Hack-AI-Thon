from modal.models import concept_keypoints
from utils.prompt import generate_prompt
import streamlit as st
from generator.voiceGenerator import Text_voice

def textprompt(text):
  prompt=choser(text)
  st.subheader("Your input : ")
  st.write(text)
  ans=concept_keypoints(prompt)
  st.write("The Result")
  result_show(ans,0)

def choser(text):
  type1=st.sidebar.selectbox("Select option",("concept","key points"))
  prompt=""
  if(text):
    if(type1=="concept"):
      st.write("Concept of the passage : ")
      prompt=generate_prompt(text,"concept")
    else:
      st.write("KeyPoints of the passage : ")
      prompt=generate_prompt(text,"keypoints")
  return prompt

def result_show(text,i):
  type1=st.sidebar.selectbox("Select option",("text","voice"))
  if(type1=="text"):
    with st.container():
     st.write(text)
  else:
    with st.container():
     st.write(text)
    Text_voice(text,i)
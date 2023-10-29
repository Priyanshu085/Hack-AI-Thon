from modal.models import description, generate_IMG
from utils.prompt import filter_description, generate_prompt
import streamlit as st

def imageprompt(text):
  if(input=="person"):
    st.subheader(f"Your input: \"{text}\" ")
    prompt=generate_prompt(text,"person")
    prompt=description(prompt)
    st.write("Person's Description :")
    prompt=filter_description(prompt, input)
    st.write("The Image : ")
    image = generate_IMG(prompt,0)
    st.image(image, use_column_width=True)

  else:
    if(text != ''):
      st.subheader(f"Your input : \"{text}\" ")
      prompt=generate_prompt(text,"place")
      prompt=description(prompt)
      # st.write("Place's Description :")
      # prompt=filter_description(prompt, input)  
      # st.write("The Image : ")
      # image = generate_IMG(prompt,0)
      # st.image(image, use_column_width=True)
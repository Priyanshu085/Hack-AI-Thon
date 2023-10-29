from generator.imageGenator import imageprompt
from generator.voiceGenerator import voice_text
import streamlit as st
from generator.textGenerator import choser, result_show, textprompt
from utils.models import concept_keypoints

st.markdown(
  """
  <style>

    h1{
        font-size: 3em;
        text-align: center;
        margin-bottom: 25px; 
        box-shadow: 8px 8px 3px grey; 
        border: 4px solid whitesmoke;
        border-radius: 8px;          
      }

  </style>

  <h1> Readlites </h1>
  """,
  unsafe_allow_html=True
)

type=st.sidebar.selectbox("Select option",("image Generation","concept from book","concept from voice book"))

if(type=="image Generation"):
  input=st.sidebar.selectbox("Select option",("person","place"))  
  st.markdown(
  """
    <style>
    h2{
      color: silver
    }
    </style>
    <h2>/* Image Generation Section */</h2>
  """, 
  unsafe_allow_html=True
  )
  if(input == "person"):
    slot = st.empty()
    text = slot.text_input(label=".", placeholder="Enter the text: " )
    
    if st.button("Generate Image"):
      slot.empty()
      if st.button("Reset"):
        slot = ''
      imageprompt(text)

  else:
    slot = st.empty()
    text = slot.text_input(label=".", placeholder="Enter the text: " )
    
    if st.button("Generate Image"):
      slot.empty()
      if st.button("Reset"):
        slot = ''
      imageprompt(text)  # generate_IMG(prompt,0)
  
elif (type=="concept from book"):
  st.markdown(
    """
      <style>
      h2{
        color: silver
      }
      </style>
      # <h2>/* Text Generation Section */</h2>
    """, 
    unsafe_allow_html=True
  )
  slot = st.empty()
  text=slot.text_input(label=".",placeholder="Enter the text: " )
  choser(text)
  if( st.button("Generate Text") and text):
    slot.empty()
    if st.button("Reset"):
      slot = ''
    textprompt(text)
  
elif (type=="concept from voice book"):
    st.markdown(
      """
      <style>
        h2{
          color: silver
        }
      </style>

      <h2>
        /* Voice Transription Section */
      </h2/>

      """,
      unsafe_allow_html=True
    )
    voice=st.file_uploader("Upload audio",type=["mp3"])
    if st.button("Generate Button"):
      with open("output1.mp3","wb") as f:
          f.write(voice.getbuffer())
      text=voice_text(0)
      st.write(text)
      prompt=choser(text)
      ans=concept_keypoints(prompt)
      st.write("The Result")
      result_show(ans,0)  
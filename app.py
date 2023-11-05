import streamlit as st
import openai
import requests
import os
from gtts import gTTS
from PIL import Image
 
#import playsound

st.set_page_config(
  page_title="readLites",
  page_icon="images/logo.png",
)

# Add custom CSS styles
st.markdown(
    """
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .header {
            font-size: 3em;
            text-align: center;
            box-shadow: 8px 8px 3px grey; 
            border: 4px solid whitesmoke;
            border-radius: 8px;          
        }
        
        .header::hover{
          font-color:blue;
          font-size:14px;
          }

        .subheader {
            font-size: 1.5em;
            margin-bottom: 10px;
          
        }
        .input-text {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            font-size: 1em;
          
        }
        .output-text {
            font-size: 1em;
            background-color: #f8f8f8;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        .result-image {
            max-width: 100%;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        .result-audio {
            max-width: 100%;
            border-radius: 5px;
            margin-bottom: 10px;
        }
          div[data-testid="stVerticalBlock"] div[style*="flex-direction: column;"] div[data-testid="stVerticalBlock"] {
        border: 1px solid whitesmoke;
        padding: 12px;
        margin: 10px;
    }
    </style>

    <h1 class='header'>readLites</h1>
    """,
    unsafe_allow_html=True  
)

# openai.api_key = os.environ['OPENAI_API_KEY']
openai.api_key = st.secrets["api_key"]

st.markdown("<h1 class='custom-header'>Output</h1>", unsafe_allow_html=True)

#generate prompt and filtering description

def generate_prompt(text,choice):
  if(choice == "person"):
      return """Extract  person's look from the passage:
      {}""".format(text)
  elif (choice == "concept"):
      return """generate the concept of the  passage:
      {}""".format(text)
  elif (choice == "place"):
      return """Extract keywords of the description of a place from the passage:
      {}""".format(text)
  elif (choice == "keypoints"):
      return """Extract key points from the passage:
      {}""".format(text)
  else:
      return ""

def filter_description(response):
  s="A person who is"+response
  s+=" + Photorealism art"
  return s

def filter_description1(response):
  s="THis place is "+response
  s+=" + Photorealism art"
  return s

  #get concept/keypoints from para

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


#extract looks and generate image

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
  st.image(file,use_column_width=True)



#voice to text  and text to voice
def Text_voice(texts,i):
  language = 'en'
  output= gTTS(text=texts,lang=language,slow=False)
  output.save(f"output{i}.mp3")
  os.system(f"start output{i}.mp3")
  #playsound.playsound(f"output{i}.mp3")

def voice_text(i):
    url="https://whisper.lablab.ai/asr"
    payload={}
    files=[
        ('audio_file',('output.mp3',open(f'output1.mp3','rb'),'audio/mpeg'))
    ]
    response=requests.request("POST",url,data=payload,files=files)
    response=response.json()
    #print(response.text)
    return(response["text"])

#helpers
def choser(text):
  type1=st.sidebar.selectbox("Select option",("concept","key points"))
  prompt=""
  if(type1=="concept"):
    with st.container():
       st.write("Concept of the passage : ")
       prompt=generate_prompt(text,"concept")
  else:
    with st.container():
      st.write("KeyPoints of the passage : ")
      prompt=generate_prompt(text,"keypoints")
  return prompt

def result_show(text,i):
    with st.container():
     st.write(text)

slot = st.empty()
#main code
type=st.sidebar.selectbox("Select option",("image Generation","concept from book"))

if(type=="image Generation"):
    type1=st.sidebar.selectbox("Select option",("person","place"))
    
    if(type1=="person"):
    # st.markdown(
    #   """
    #     <div>
    #     <div>
    #   """, 
    #   unsafe_allow_html=True  
    # )
    #  with st.container():
      text=st.text_input(label="Enter Text", placeholder="Enter the text for image generation : " )
      st.subheader("Your input : ")
      st.write(text)
      prompt=generate_prompt(text,"person")
      prompt=description(prompt)
      st.write("Person's Description : ")
      st.write(prompt)
      prompt=filter_description(prompt)
      #st.write(prompt)
    else:
      # with st.container():
      text=st.text_input(label="Enter Text",placeholder="Enter the text below : " )
      st.subheader("Your input : ")
      st.write(text)
      prompt=generate_prompt(text,"place")
      prompt=description(prompt)
      st.write("Place's Description : ")
      st.write(prompt)
      prompt=filter_description1(prompt)
      st.write("The Image : ")
    generate_IMG(prompt,0)

elif (type=="concept from book"):
  text=st.text_input(label="Enter Text",placeholder="Enter the text below : " )
  st.subheader("Your input : ")
  st.write(text)
  prompt=choser(text)
  ans=concept_keypoints(prompt)
  st.write("The Result")
  result_show(ans,0)
  if(ans):
    if st.button("Read Aloud"):
        slot.empty()
        Text_voice(texts=ans, i=1)
        
# elif (type=="concept from voice book"):
#     voice=st.file_uploader("Upload audio",type=["mp3"])
#     if voice is not None:
#       with open("output1.mp3","wb") as f:
#         f.write(voice.getbuffer())
#       text=voice_text(0)
#       st.write(text)
#       prompt=choser(text)
#       ans=concept_keypoints(prompt)
#       st.write("The Result")
#       result_show(ans,0)
#     else:
#        st.write("Please upload an audio file.")
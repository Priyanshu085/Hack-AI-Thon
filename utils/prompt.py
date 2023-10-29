# Image Prompts
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

def filter_description(response, input):

  if(input == "person"):
    s="A person who is"+response+" Photorealism art"
    
  s="This place is "+response+" Photorealism art"
  
  return s
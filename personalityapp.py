### Personality Recognition App

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=st.secrets['API_KEY'])

## Function to load Google Gemini Pro Vision API And get response

def get_gemini_repsonse(input,image,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
##initialize our streamlit app

st.set_page_config(page_title="Personality Recognition App")

st.header("Personality Recognition App")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit=st.button("Tell me about this personality")

input_prompt="""
You are an expert in recognising people, where you need to see that person recognise him/her and tell everything about him/her like there full name about there birth place & date also with death date & place
in addition to there achievements, about there educational details in the below format.

               1. Name - name of that personality with short description about him
               2. Place of Birth - place of birth with birth date
               3. Death - place and date of death
               4. Education - write about there educational background
               5. Family - write little information about there family 
               6. Achievements - write about there achievements like prices, inventions, discoveries they did
               ----
               ----


"""

## If submit button is clicked

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)
      

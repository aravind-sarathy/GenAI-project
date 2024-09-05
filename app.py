from dotenv import load_dotenv
load_dotenv() # Activae the local env variables.

import streamlit as st
import os
import google.generativeai as genai

# Setup the local environment for the google api key
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))

model = genai.GenerativeModel("gemini-pro")
# Function to create the content

def generate(question):
    response = model.generate_content(question)
    return(response.text)

## Streamlit webpage##
st.set_page_config(page_title="LLM Q&A application")
st.header("Generating answer using gemini pro")
input = st.text_input(label="Ask the question",key=input)
submit = st.button(label="Generate response")

if submit:
    response = generate(input)
    st.subheader("The response is: ")
    st.write(response)
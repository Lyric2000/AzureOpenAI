import streamlit as st
from dotenv import load_dotenv
import openai
import os

load_dotenv("../.env")

# Set the OpenAI API key.
openai.api_key = os.environ["OPENAI_API_KEY"]
# openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_base = os.environ["OPENAI_API_BASE"]
openai.api_type = os.environ["OPENAI_API_TYPE"]
openai.api_version = os.environ["OPENAI_API_VERSION"]

# Function to query the language model.
def llm_model(prompt_question):
    response = openai.ChatCompletion.create(
        engine="chat",
        messages=[{"role": "system", "content": "You are a helpful research and\
            programming assistant"},
                  {"role": "user", "content": prompt_question}]
    )
    
    return response["choices"][0]["message"]["content"]

# Streamlit app
st.title('Chat with ChatGPT')

# Text input for the user's question.
prompt_question = st.text_input('__Enter the prompt for the model:__', '')

# Button to submit the question.
if st.button('Ask ChatGPT'):
    response = llm_model(prompt_question)
    st.text_area('__ChatGPT response:__', response, height=200)

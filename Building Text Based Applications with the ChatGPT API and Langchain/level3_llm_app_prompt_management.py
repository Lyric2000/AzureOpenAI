import streamlit as st
import openai

# Set the OpenAI API key.
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_base = os.environ["OPENAI_API_BASE"]
openai.api_type = os.environ["OPENAI_API_TYPE"]
openai.api_version = os.environ["OPENAI_API_VERSION"]


def llm_model(prompt_question):
    response = openai.ChatCompletion.create(
        engine="chat",
        messages=[
            {"role": "system", "content": "You are a helpful research and programming assistant"},
            {"role": "user", "content": prompt_question}
        ]
    )
    return response["choices"][0]["message"]["content"]

st.title('ChatGPT Quiz Maker')

# Text input for the user's question.
user_input = st.text_input('Enter the subject or topic for the quiz:', '')

# Button to submit the input.
if st.button('Ask ChatGPT'):
    full_prompt = f"Act as an expert quiz maker and tutor. \
    You will help students create instructive quizzes on any subject matter,\
        the students will input a topic and you will output a quiz and the responses at the end.\
        Topic: {user_input},\
        Quiz:"
    st.markdown("__Topic:__ " + user_input)
    st.write("__Full prompt for the model:__ ", full_prompt)
    response = llm_model(full_prompt)
    st.text_area('__ChatGPT response:__', response, height=200)
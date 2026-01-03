from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

load_dotenv()  # take environment variables from .env.

client = OpenAI()

initial_message = [
        {"role": "system", "content": "You are a expert trip planner in Dubai who has good knowledge in Dubai tourism, locations, food, events, hotels etc. You have to ask questions and guide users to plan their vacation in Dubai. Respond professionally and should not exceed 200 words.If they insist, provide a daywise iternary after asking questions."},
        {
            "role": "assistant",
            "content": "Hey there, I am Ghafoor ka Dosth, your Dubai trip planner, How can I help you? "
        }
    ]

def get_response_from_llm(messages):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
)
    return completion.choices[0].message.content

if "messages" not in st.session_state:
    st.session_state.messages = initial_message

st.title(" :red[Ghafoor ka Dosth] :sunglasses:")
st.image("dubainew.jpg")

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

user_message = st.chat_input("Enter your message")
if user_message:
    new_message = {
         "role": "user",
        "content": user_message
        }
    st.session_state.messages.append(new_message)
    with st.chat_message(new_message["role"]):
            st.markdown(new_message["content"])
            
    response = get_response_from_llm(st.session_state.messages)
    if response:
     response_message = {
        "role": "assistant",
            "content": response
        }
     st.session_state.messages.append(response_message)
     with st.chat_message(response_message["role"]):
            st.markdown(response_message["content"])

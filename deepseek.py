import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

st.title("Sahil's Chatbot")
user_input = st.text_input("Enter Your Query")



client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

if st.button("Generate Response") and user_input:
    try:
        # API Call
       completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>",
    "X-Title": "<YOUR_SITE_NAME>", 
  },
  extra_body={},
  model="openrouter/free",
  messages=[
    {
      "role": "user",
      "content": user_input
    }
  ]
)

       st.write("Chatbot Response:")
       st.write(completion.choices[0].message.content)
    except Exception as e:
        st.error("Error fetching response: " + str(e))


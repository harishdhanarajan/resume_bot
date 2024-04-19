import streamlit as st
from llama_index.llms.openai import OpenAI
try:
  from llama_index import VectorStoreIndex, ServiceContext, Document, SimpleDirectoryReader
except ImportError:
  from llama_index.core import VectorStoreIndex, ServiceContext, Document, SimpleDirectoryReader
import openai

st.set_page_config(page_title="Harish's Bot", page_icon=" 🤖📚", layout="wide", initial_sidebar_state="auto", menu_items=None)
openai.api_key = st.secrets["my_cool_secrets"]["openai_key"]
st.title("🌟 Ask anything about Harish....")

st.info("Check Out my Complete Portfolio [here](https://harishdhanarajan.streamlit.app/) !", icon="📃")

#Initiate the Session and Create a temp memory
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about Streamlit's open-source Python library!"}
    ]
  
#[my_cool_secrets]
#openai_key = "sk-proj-tMubK0K5nswmWfUCDMjhT3BlbkFJmvMJhM5PiUk8Gnj8F6CI"

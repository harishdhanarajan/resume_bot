import streamlit as st
from llama_index.llms.openai import OpenAI
try:
  from llama_index import VectorStoreIndex, ServiceContext, Document, SimpleDirectoryReader
except ImportError:
  from llama_index.core import VectorStoreIndex, ServiceContext, Document, SimpleDirectoryReader
import openai

st.set_page_config(page_title="Chat with the Streamlit docs, powered by LlamaIndex", page_icon="🦙", layout="centered", initial_sidebar_state="auto", menu_items=None)
openai.api_key = st.secrets["my_cool_secrets"]["openai_key"]

st.write(openai.api_key)

#[my_cool_secrets]
#openai_key = "sk-proj-tMubK0K5nswmWfUCDMjhT3BlbkFJmvMJhM5PiUk8Gnj8F6CI"

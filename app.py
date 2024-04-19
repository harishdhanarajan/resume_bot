import streamlit as st
from llama_index.llms.openai import OpenAI
try:
  from llama_index import VectorStoreIndex, ServiceContext, Document, SimpleDirectoryReader
except ImportError:
  from llama_index.core import VectorStoreIndex, ServiceContext, Document, SimpleDirectoryReader
import openai

st.write(st.secrets["my_cool_secrets"]["openai_key"])

#[my_cool_secrets]
#openai_key = "sk-proj-tMubK0K5nswmWfUCDMjhT3BlbkFJmvMJhM5PiUk8Gnj8F6CI"

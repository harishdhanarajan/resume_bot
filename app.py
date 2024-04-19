import time
import streamlit as st
from llama_index.llms.openai import OpenAI
try:
  from llama_index import VectorStoreIndex, ServiceContext, Document, SimpleDirectoryReader
except ImportError:
  from llama_index.core import VectorStoreIndex, ServiceContext, Document, SimpleDirectoryReader
import openai

st.set_page_config(page_title="Harish's Bot", page_icon=" 🤖📚", layout="centered", initial_sidebar_state="auto", menu_items=None)
openai.api_key = st.secrets.openai_key
st.title("🌟 Ask anything about Harish....")
st.info("Check Out my Complete Portfolio [here](https://harishdhanarajan.streamlit.app/) !", icon="📃")

#Initiate the Session and Create a temp memory
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "I am a Beta Version and Still Under Training by Mr. Harish!!"}
    ]

@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading and indexing all Required information about Mr.Harish from his knowledge base"):
        reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
        docs = reader.load_data()
        service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="I Don't Hallucinate, I just try to speak facts about Mr. Harish and give my best to give True Information about him."))
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index

index = load_data()

if "chat_engine" not in st.session_state.keys(): # Initialize the chat engine
        st.session_state.chat_engine = index.as_chat_engine(chat_mode="context", verbose=True)

if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])
      
def stream_data():
  response = st.session_state.chat_engine.chat(prompt)
  words = response.response
  for word in words.split(" "):
    yield word + " "
    time.sleep(0.05)
  
# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            #response = st.session_state.chat_engine.chat(prompt)
            st.write_stream(stream_data)
            message = {"role": "assistant", "content": stream_data}
            st.session_state.messages.append(message) # Add response to message history

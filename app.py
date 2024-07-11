import streamlit as st
from llama_index.llms.openai import OpenAI
try:
  from llama_index import VectorStoreIndex, ServiceContext, Document, SimpleDirectoryReader
except ImportError:
  from llama_index.core import VectorStoreIndex, ServiceContext, Document, SimpleDirectoryReader
import openai

openai_key = "sk-proj-GOgJzknM0p1xjM4tdqkxT3BlbkFJHBBywcC8JPNquSvkpzP4"
st.set_page_config(page_title="🤖 Harish's Bot", page_icon= "🤖📚", layout="centered",initial_sidebar_state="collapsed")
st.subheader(" ", divider='rainbow')
openai.api_key = st.secrets.openai_key
gradient_text_html = """
<style>
.gradient-text {
    font-weight: bold;
    background: -webkit-linear-gradient(left, red, orange);
    background: linear-gradient(to right, red, orange);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline;
    font-size: 3em;
}
</style>
<div class="gradient-text">Ask Me About Harish....</div>
"""

st.markdown(gradient_text_html, unsafe_allow_html=True)
st.caption("Talk your way through")
st.info(":rainbow[[Check Out Harish's Complete Portfolio here](https://harishdhanarajan.streamlit.app/) !]", icon="📃")

with open("sidebar/sidebar.md", "r") as sidebar_file:
    sidebar_content = sidebar_file.read()

with open("sidebar/styles.md", "r") as styles_file:
    styles_content = styles_file.read()

st.sidebar.markdown(sidebar_content)

INITIAL_MESSAGE = [
        {"role": "assistant", "content": ":red[Hey there! I'm Sasha (Beta), ready to answer questions about Harish. Use the Arrow on left top corner to know more about this application.]"}
    ]
if st.sidebar.button("Reset Chat"):
    for key in st.session_state.keys():
        del st.session_state[key]
    st.session_state["messages"] = INITIAL_MESSAGE
    st.session_state["history"] = []

st.sidebar.markdown(
    "**Note:** <span style='color:red'>This is a Beta Version, Still Being Trained.</span>",
    unsafe_allow_html=True,
)

st.write(styles_content, unsafe_allow_html=True)

#Initiate the Session and Create a temp memory
if "messages" not in st.session_state.keys():
    st.session_state.messages = INITIAL_MESSAGE

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

if prompt := st.chat_input("Technical intiatives taken by Harish / His Proud achievements"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)     



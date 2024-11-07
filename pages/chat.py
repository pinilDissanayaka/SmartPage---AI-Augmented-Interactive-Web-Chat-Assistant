import os
import streamlit as st
from secret import load_secret
from web_page import load_page


st.set_page_config(page_title="SmartPage", page_icon="🤖")


with st.sidebar:
    st.title("SmartPage – Your AI-Enhanced Web Chat Assistant 🤖💬")
    
    
    if not ("GROQ_API_KEY" in st.secrets.keys() and "PINECONE_API_KEY" in st.secrets.keys()):
        groq_api_key = st.text_input(label="Enter your Groq API key :", value=None, type="password")
        
        pinecone_api_key = st.text_input(label="Enter your Pinecone API key :", value=None, type="password")

        if groq_api_key and pinecone_api_key:
            if st.button("Load API Keys"):
                load_secret(groq_api_key=groq_api_key, pinecone_api_key=pinecone_api_key)
        else:
            st.error("Please enter both Groq and Pinecone API keys.", icon="🚨")
    else:
        load_secret()
        
    if "GROQ_API_KEY" in os.environ.keys() and "PINECONE_API_KEY" in os.environ.keys():
        st.success("Groq and Pinecone API keys loaded successfully!", icon="✅")
        
web_url=st.text_input(label="Enter your webpage URL :", value=None, type="default")

if web_url:
    if st.button("Load Webpage"):
        documents=load_page(web_url)
        st.write(documents)

        
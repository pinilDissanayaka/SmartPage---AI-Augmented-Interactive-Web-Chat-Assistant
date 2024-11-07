import os
import streamlit as st


def load_secret(groq_api_key=None, pinecone_api_key=None):
    if groq_api_key and pinecone_api_key:
        os.environ["GROQ_API_KEY"] = groq_api_key
        os.environ["PINECONE_API_KEY"] = pinecone_api_key
    else:
        if "GROQ_API_KEY" in st.secrets.keys() and "PINECONE_API_KEY" in st.secrets.keys():
            os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
            os.environ["PINECONE_API_KEY"] = st.secrets["PINECONE_API_KEY"]
        else:
            st.error("Please enter both Groq and Pinecone API keys.", icon="🚨")
            

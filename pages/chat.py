import os
import streamlit as st


st.set_page_config(page_title="SmartPage", page_icon="🤖")


with st.sidebar:
    st.title("Welcome to SmartPage – Your AI-Enhanced Web Chat Assistant 🤖💬")
    
    
    if not ("GROQ_API_KEY" in st.session_state.keys() and "PINECONE_API_KEY" in st.session_state.keys()):
        st.session_state["GROQ_API_KEY"] = st.text_input("Enter your Groq API key :", type="password")
        
        st.session_state["PINECONE_API_KEY"] = st.text_input("Enter your Pinecone API key :", type="password")
    
    
import os
import streamlit as st
from secret import load_secret

st.set_page_config(page_title="SmartPage", page_icon="🤖")

with st.sidebar:
    st.title("SmartPage – Your AI-Enhanced Web Chat Assistant 🤖💬")
    
    
    if not ("GROQ_API_KEY" in st.secrets.keys() and "PINECONE_API_KEY" in st.secrets.keys()):
        groq_api_key = st.text_input(label="Enter your Groq API key :", value=None, type="password")
        
        pinecone_api_key = st.text_input(label="Enter your Pinecone API key :", value=None, type="password")

        if groq_api_key and pinecone_api_key:
            load_secret(groq_api_key=groq_api_key, pinecone_api_key=pinecone_api_key)
        else:
            st.error("Please enter both Groq and Pinecone API keys.", icon="🚨")
    else:
        load_secret()
        
    if "GROQ_API_KEY" in os.environ.keys() and "PINECONE_API_KEY" in os.environ.keys():
        st.success("Groq and Pinecone API keys loaded successfully!", icon="✅")

st.header("Welcome to SmartPage – Your AI-Enhanced Web Chat Assistant 🤖💬")

st.write("Need quick, accurate answers from trusted sources? SmartPage is here to help! 🌐✨")

st.image(image="assets/smartPage.jpg", caption="SmartPage: Your AI-Enhanced Web Chat Assistant")

st.write("SmartPage combines the latest in AI technology with real-time information retrieval, delivering you precise, up-to-date answers from selected, reputable webpages. Our intelligent chat assistant draws from trusted sources, providing answers to your queries while referencing the web content you can rely on.")

st.subheader("Why SmartPage?")
st.write("Real-Time, Relevant Information 📅🔍: Get responses based on the latest content from trusted sites. Our AI pulls information directly from sources we've carefully curated.")
st.write("Interactive & Conversational 🗣️💡: Ask questions naturally, and SmartPage will respond in a friendly, easy-to-understand manner, guiding you to the answers you need.")
st.write("Direct Source Links 🔗📑: Verify information with quick links to source pages, so you’re always in control of your research and decisions.")
st.write("Whether you're here for product details, educational help, or customer support, SmartPage is designed to connect you with the right information faster than ever. 🚀")

st.subheader("Try it now and experience the future of AI-enhanced web interaction! 🔥")
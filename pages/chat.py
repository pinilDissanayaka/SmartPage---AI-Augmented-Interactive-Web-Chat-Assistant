import os
import streamlit as st
from secret import load_secret
from web_page import load_page, split_page
from vector_store import load_vector_store, get_retrieve_vector_store, delete_vector_store, chroma_path
from chat import chat_with_webpage

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
        
        
        if os.path.exists(chroma_path):
            if st.button("Delete Vector Store"):
                delete_vector_store()
            
        web_url=st.text_input(label="Enter your webpage URL :", value=None, type="default")
        if web_url:
            if st.button("Load Webpage"):
                with st.spinner("Loading..."):
                    documents=load_page(urls=web_url)
                    
                    if "scraped_documents" not in st.session_state.keys():
                        st.session_state.scraped_documents = documents
                    
                    splitted_documents=split_page(documents=documents)
                    
                    load_vector_store(documents=splitted_documents)
                    
                    st.success("Vector store loaded successfully!", icon="✅")
                
if os.path.exists(chroma_path):
    if "scraped_documents" in st.session_state.keys():
        st.markdown(body=st.session_state['scraped_documents'], unsafe_allow_html=True)
    
    # Store LLM generated responses
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [{"role": "assistant", "content": "How may I help you? 👋"}]

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Function for generating LLM response
    def generate_response(prompt_input):
        return chat_with_webpage(question=prompt_input)


    # User-provided prompt
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

    # Generate a new response if last message is not from assistant
    if st.session_state.messages[-1]["role"] != "assistant":
        try:
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = generate_response(prompt) 
                    st.write(response)
            message = {"role": "assistant", "content": response}
            st.session_state.messages.append(message)
        except Exception as e:
            st.warning(f"An unexpected error occurred: {str(e.args)}. Please try again.", icon="⚠️")
else:
    st.warning("Please load your webpage first.", icon="🚨")

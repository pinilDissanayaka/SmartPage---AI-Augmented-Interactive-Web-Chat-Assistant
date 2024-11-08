import os
import streamlit as st
from shutil import rmtree
from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_community.vectorstores.chroma import Chroma
from config import get_embeddings


chroma_path="vector_store"

def load_vector_store(documents):
    try:
        embeddings = get_embeddings()
        
        if os.path.exists(chroma_path):
            rmtree(path=chroma_path)
            
        vector_store=Chroma.from_documents(
            documents=documents,
            embedding=embeddings,
            persist_directory=chroma_path
        )
        
        vector_store_persist=vector_store.persist()
    except Exception as e:
        st.error("Error in loading vector store.", icon="🚨")
        st.error(e.args)
        

def get_retrieve_vector_store():
    try:        
        embeddings = get_embeddings()
        
        vector_store=Chroma(persist_directory=chroma_path, embedding_function=embeddings)
        
        return vector_store.as_retriever()
    except Exception as e:
        st.error("Error in loading vector store.", icon="🚨")
        st.error(e.args)
        
def delete_vector_store():
    try:
        if os.path.exists(chroma_path):
            rmtree(path=chroma_path)
            st.success("Vector store deleted successfully.", icon="✅")
    except Exception as e:
        st.error("Error in deleting vector store.", icon="🚨")
        st.error(e.args)
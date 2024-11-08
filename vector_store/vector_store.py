import os
import streamlit as st
from shutil import rmtree
from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_community.vectorstores.chroma import Chroma


chroma_path="/vector_store/"

def load_vector_store(documents):
    try:
        model_name = "sentence-transformers/all-mpnet-base-v2"
        model_kwargs = {'device': 'cpu'}
        encode_kwargs = {'normalize_embeddings': False}
        
        embeddings = HuggingFaceEmbeddings(
            model_name=model_name,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs
        )
        
        if os.path.exists(chroma_path):
            rmtree(path=chroma_path)
            
        vector_store=Chroma.from_documents(
            documents=documents,
            embeddings=embeddings,
            persist_directory=chroma_path
        )
        
        vector_store_persist=vector_store.persist()
    except Exception as e:
        st.error("Error in loading vector store.", icon="🚨")
        st.error(e.args)
        

def get_retrieve_vector_store():
    try:
        model_name = "sentence-transformers/all-mpnet-base-v2"
        model_kwargs = {'device': 'cpu'}
        encode_kwargs = {'normalize_embeddings': False}
        
        embeddings = HuggingFaceEmbeddings(
            model_name=model_name,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs
        )
        
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
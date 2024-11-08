from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from time import sleep
from config import get_llm, get_chat_prompt
from vector_store import get_retrieve_vector_store

def chat_with_webpage(question:str, history=None):
    
    chat_chain=(
        {"QUESTION" : RunnablePassthrough(), "CONTEXT" : get_retrieve_vector_store()} |
        get_chat_prompt() |
        get_llm() |
        StrOutputParser()
    )
    
    response=chat_chain.invoke({"QUESTION" : question})
    
    return response

def stream_response(response:str, delay=0.05):
    for word in response.split(" "):
        yield word + " "
        sleep(delay)
        
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate


def get_embeddings(model_name="sentence-transformers/all-mpnet-base-v2") -> HuggingFaceEmbeddings:
    model_name = model_name
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}
        
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    
    return embeddings

def get_llm(model="llama-3.1-8b-instant", temperature=0.85):
    llm=ChatGroq(model=model, temperature=temperature)
    
    return llm


def get_chat_prompt():
    chat_prompt_template = """Given the following context and a question, 
    generate an answer based on this context only.
    In the answer try to provide as much text as possible from "ANSWER" 
    section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." 
    Don't try to make up an answer.

        CONTEXT: {CONTEXT}

        QUESTION: {QUESTION}
    
        ANSWER:
    """
    
    prompt_template=ChatPromptTemplate.from_template(chat_prompt_template)
    
    return prompt_template
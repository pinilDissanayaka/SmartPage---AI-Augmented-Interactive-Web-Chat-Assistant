from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter



def load_page(urls):
    loader = WebBaseLoader(web_path=urls)
    documents = loader.load()
    
    return documents

def split_page(documents):
    splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0, length_function=len)
    
    return splitter.split_documents(documents)
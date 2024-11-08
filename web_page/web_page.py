from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter



def load_page(urls):
    loader = WebBaseLoader(web_path=urls)
    documents = loader.load()
    
    cleaned_documents = []
    
    for document in documents:
        page_content=document.page_content.replace("\n", "")
        meta_data=document.metadata.replace("\n", "")
        cleaned_documents.append(Document(page_content=page_content, metadata=meta_data))
    
    return cleaned_documents

def split_page(documents):
    splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0, length_function=len)
    
    return splitter.split_documents(documents)
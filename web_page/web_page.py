from langchain.document_loaders import WebBaseLoader



def load_page(urls):
    loader = WebBaseLoader(web_path=urls)
    documents = loader.load()
    
    return documents
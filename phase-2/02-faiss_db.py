from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os


def doc_loader(pdf):
    loader = PyPDFLoader(pdf)
    doc = loader.load()
    return doc


def chunking(doc):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 400,
        chunk_overlap = 50
    )
    chunks = splitter.split_documents(doc)
    return chunks


def build_faiss_vectorstores(chunks):
    embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embedder)
    return vectorstore


def save_faiss_vectorstores(vectorestores):
    if not os.path.exists("phase-2/KB/faiss_store"):
        os.makedirs("phase-2/KB/faiss_store")
    vectorestores.save_local("phase-2/KB/faiss_store")    


def main():
    doc = doc_loader("phase-2/KB/01-dummy-ecom-policy-pdf.pdf") 
    chunks = chunking(doc)
    vectorstores = build_faiss_vectorstores(chunks)
    save_faiss_vectorstores(vectorstores)   
    print("Vector Store Created!!")



if __name__ == "__main__":
    main()    
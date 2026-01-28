from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
# from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts  import PromptTemplate
from langchain_ollama import OllamaLLM
import os



# document loading
def doc_loading(pdf):
    loader = PyPDFLoader(pdf)
    doc = loader.load()
    return doc




# text splitting
def chunking(doc):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 400,
        chunk_overlap = 60
    )
    chunks = splitter.split_documents(doc)
    return chunks




# embedding generation
def faiss_embedding(chunks):
    embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstores = FAISS.from_documents(chunks, embedder)

    if not os.path.exists("phase-2/KB/faiss_store_HP"):
        os.makedirs("phase-2/KB/faiss_store_HP")

    vectorstores.save_local("phase-2/KB/faiss_store_HP")





# load vector, embed user query 
def load_faiss():
    embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    vectorstores = FAISS.load_local(
        "phase-2/KB/faiss_store_HP",
        embeddings=embedder,
        allow_dangerous_deserialization=True
    )    
    return vectorstores



# chunk retrieval
def retrieval(vectorstores, query):
    results = vectorstores.similarity_search(query, k=3)
    return results







# augment prompt
def aug_prompt(query, context):

    template = """
You are a helpful assistant.

Context:
{context}

Question:
{query}

Answer in simple language.
"""
    prompt = PromptTemplate.from_template(template)
    final_prompt = prompt.format(context=context, query=query)
    return final_prompt
    


# load llm 
def load_llm(final_prompt):
    # llm = HuggingFaceEndpoint(
    #     repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    #     temperature = 0.2, 
    #     max_new_tokens=200
    # )
    llm = OllamaLLM(model="llama3", temperature=0.7)
    response = llm.invoke(final_prompt)
    return response
     


def ask_user():
    if input("Are you a Potter Head?: ").lower() == "yes":
        query = input("Please ask anything about Harry Potter my dear! \n")
        return query
    else:
        print("GoodBye! we can't be friends..")

    



# main function call
def main():
    # doc = doc_loading("phase-2/KB/04-HP-dummy.pdf")
    # chunks = chunking(doc)

    # faiss_embedding(chunks)
    vectorstores = load_faiss()
    
    user_query = ask_user()

    if user_query:
        results = retrieval(vectorstores, user_query)
        final_prompt = aug_prompt(user_query, results)

        answer = load_llm(final_prompt)
        print(answer)



if __name__ == "__main__":
    main() 
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings



def load_faiss(path):
    embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstores = FAISS.load_local(
        folder_path = path,
        embeddings = embedder,
        allow_dangerous_deserialization = True
    )
    return vectorstores




def retrieve_top_k(vectorstores, query, k=3):
    results = vectorstores.similarity_search(query, k=k)
    return results




def main():
    vectorstores = load_faiss("phase-2/KB/faiss_store")
    query = input("Enter a topic: ")
    results = retrieve_top_k(vectorstores, query)
    
    for index, result in enumerate(results, start=1):
        print(index, result.page_content[:300])




if __name__ == "__main__":
    main()

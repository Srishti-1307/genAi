from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")           # embedding model

client = chromadb.Client()                    # creating a vector db client, Making connection to chromadb 
# chromadb.Client() creates a (in-memory) chroma client, which creates a temporary database in RAM not on disk
# If you do  ```client = chromadb.PersistentClient(path="my_chroma_db")```  Now inside my_chroma_db folder, chroma.sqlite, index folder and collections folder will appear


collection = client.create_collection("test-embeddings")                 # A collection is like a table/bucket, storing embeddings & metadata & IDs

text = [
    "vector db stores embeddings",
    "chromaDb is a vector db",
    "we're learning genAi here"
]

embeddings = model.encode(text)

collection.add(
    ids = ["1", "2", "3"],               # or do, ids = [str(i) for i in range(1, len(text) + 1)]
    embeddings = embeddings,
    metadatas = [{"text" : text[0]}, {"text" : text[1]}, {"text" : text[2]}]            # or do, metadatas = [{"text": t} for t in texts]
)

result = collection.query(
    query_embeddings = model.encode(["Chroma DB is what kind of database?"]),
    n_results = 1
)

print(result)                    # result is a dictionary, you can print result.ids & result.metadatas
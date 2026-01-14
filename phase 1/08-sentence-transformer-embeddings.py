from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

text = "sentence_transformer is a python library to create embeddings."

embedding = model.encode(text)

print(type(embedding))
print(len(embedding))

print(embedding[:10])


'''
we get 1 vector for the whole sentence cuz, SentenceTransformer applies Sentence-level embeddings
i.e,   1 single vector for the whole meaning of the sentence.

depending upon the model, 1 embedding = 512~2048 tokens
So.. if you have a large text (or a pdf) it needs to be splitted into chunks
Then for each chunk, embedding is created 

While, At transformer level, each token gets its own vector. Each token passes through every transformer layer
As a developer, no need to care for token-level embeddings rn. Token-level embedding is required during model training or fine tuning

openAi embedding model also generate 1 token per string/sentence/chunk 
'''
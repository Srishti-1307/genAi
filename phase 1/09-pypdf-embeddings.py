'''
Workflow:
Extract text from pdf, split it into chunks, convert chunks into embeddings, store in vector db
'''

from sentence_transformers import SentenceTransformer
from pypdf import PdfReader

model = SentenceTransformer("all-MiniLM-L6-v2")

reader = PdfReader("phase 1/09-sample-pdf.pdf")

'''
reader is a PdfReader object that contains entire pdf structure. Lie below:
reader = {
    pages: [Page1, Page2, Page3, ...],
    metadata: {...},
    outlines: {...},
    etc...
}
'''

text = ""            # a string will contain whole pdf data, each page data in new line

for page in reader.pages:
    text += page.extract_text() + "\n"                # extract_text() reads the text on Page1 



def chunk_text(text, chunk_size = 400):
    words = text.split()                        # splits the complete pdf text into individual word and returns a list of words now, This is done as counting words is better than counting characters
    chunks = []
    current = []
    for word in words:
        current.append(word)
        if len(current) >= chunk_size:
            chunks.append(" ".join(current))
            current = []

    return chunks


chunk = chunk_text(text)
print(chunk[2])

embeddings = model.encode(chunk)

print(len(embeddings))
print(embeddings.shape)


# PdfReader is only for textual pdfs.. not for pdfs containing images, logos, tables, symbols etc.

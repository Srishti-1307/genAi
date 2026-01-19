from pypdf import  PdfReader

# Loading pdf
reader = PdfReader("phase-2/01-dummy-ecom-policy-pdf.pdf")

# Empty String
text = ""

# Loading pdf context page by page into a string
for page in reader.pages:
    text += page.extract_text() + "\n"



# Chunking
def manual_chunking(text, chunk_size=400, overlap=50):
    chunk_list = []
    start = 0
    chunk_id = 1

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        chunk_list.append(
            {
                "id" : chunk_id,
                "chunk" : chunk.strip()
            }
        )   

        start = end - overlap
        chunk_id += 1

    return chunk_list


res = manual_chunking(text)

print(len(res))
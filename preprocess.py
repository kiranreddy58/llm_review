import re
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

def clean(text):
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def chunk_text(text, limit=400):
    tokens = enc.encode(text)
    chunks = []
    i = 0
    while i < len(tokens):
        sub = tokens[i : i + limit]
        chunks.append(enc.decode(sub))
        i += limit
    
    if len(chunks) == 0:
        chunks.append(text)
        
    return chunks

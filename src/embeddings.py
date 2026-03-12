from sentence_transformers import SentenceTransformer
import chromadb
import os

# Load cleaned text
def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# Split text into chunks
def split_text(text, chunk_size=400):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i + chunk_size]))
    return chunks

if __name__ == "__main__":
    text_path = "data/processed/cleaned_text.txt"

    if not os.path.exists(text_path):
        raise FileNotFoundError("❌ cleaned_text.txt not found")

    text = load_text(text_path)
    chunks = split_text(text)

    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(chunks).tolist()

    client = chromadb.Client()
    collection = client.create_collection(name="rag_docs")

    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk],
            embeddings=[embeddings[i]],
            ids=[str(i)]
        )

    print("✅ Embeddings stored successfully using ChromaDB")

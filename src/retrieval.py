from sentence_transformers import SentenceTransformer
import faiss

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("vector_store/faiss_index")

def load_chunks():
    with open("vector_store/chunks.txt", "r", encoding="utf-8") as file:
        return file.readlines()

def search(query, top_k=3):

    query_embedding = model.encode([query])

    distances, indices = index.search(query_embedding, top_k)

    chunks = load_chunks()

    results = [chunks[i] for i in indices[0] if i < len(chunks)]

    return results


if __name__ == "__main__":
    query = input("Enter your question: ")
    results = search(query)

    print("\n🔍 Relevant Information Retrieved:\n")
    for res in results:
        print("-", res.strip())from sentence_transformers import SentenceTransformer
import faiss

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("vector_store/faiss_index")

def load_chunks():
    with open("vector_store/chunks.txt", "r", encoding="utf-8") as file:
        return file.readlines()

def search(query, top_k=3):

    query_embedding = model.encode([query])

    distances, indices = index.search(query_embedding, top_k)

    chunks = load_chunks()

    results = [chunks[i] for i in indices[0] if i < len(chunks)]

    return results


if __name__ == "__main__":
    query = input("Enter your question: ")
    results = search(query)

    print("\n🔍 Relevant Information Retrieved:\n")
    for res in results:
        print("-", res.strip())from sentence_transformers import SentenceTransformer
import faiss

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("vector_store/faiss_index")

def load_chunks():
    with open("vector_store/chunks.txt", "r", encoding="utf-8") as file:
        return file.readlines()

def search(query, top_k=3):

    query_embedding = model.encode([query])

    distances, indices = index.search(query_embedding, top_k)

    chunks = load_chunks()

    results = [chunks[i] for i in indices[0] if i < len(chunks)]

    return results


if __name__ == "__main__":
    query = input("Enter your question: ")
    results = search(query)

    print("\n🔍 Relevant Information Retrieved:\n")
    for res in results:
        print("-", res.strip())
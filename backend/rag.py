import chromadb
from openai import OpenAI
import os

client = OpenAI()
chroma = chromadb.PersistentClient(path="../vector_db")
collection = chroma.get_or_create_collection("insurance_docs")

def get_rag_answer(query):
    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    context = "\n".join(results["documents"][0])

    prompt = f"""
    You are Alliance Insurance support AI.
    Use ONLY this context to answer:

    {context}

    User question: {query}
    """

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message["content"]

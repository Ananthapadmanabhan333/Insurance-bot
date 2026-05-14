import chromadb
from openai import OpenAI
import os

client = OpenAI()
chroma = chromadb.PersistentClient(path="../vector_db")
collection = chroma.get_or_create_collection("insurance_docs")

def add_document(doc_id, text):
    collection.add(
        documents=[text],
        ids=[doc_id]
    )

if __name__ == "__main__":
    motor = open("../data/extracted_text/motor_policy.txt").read()
    health = open("../data/extracted_text/health_policy.txt").read()
    claims = open("../data/extracted_text/claims_process.txt").read()

    add_document("motor", motor)
    add_document("health", health)
    add_document("claims", claims)

    print("Documents added successfully.")

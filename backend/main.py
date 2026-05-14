from fastapi import FastAPI
from pydantic import BaseModel
from rag import get_rag_answer
from sentiment import detect_sentiment
from complaints import create_complaint

app = FastAPI()

class Query(BaseModel):
    user_id: str
    message: str


@app.post("/chat")
def chat(q: Query):
    sentiment = detect_sentiment(q.message)

    # If angry → create complaint
    if sentiment in ["angry", "very angry"]:
        complaint_id = create_complaint(q.user_id, q.message, sentiment)
        complaint_msg = f"Your complaint has been registered. Complaint ID: {complaint_id}"
    else:
        complaint_msg = None

    reply = get_rag_answer(q.message)

    return {
        "reply": reply,
        "sentiment": sentiment,
        "complaint": complaint_msg
    }

from openai import OpenAI

client = OpenAI()

def detect_sentiment(text):
    prompt = f"Classify sentiment: positive, neutral, angry, very angry.\nText: {text}"

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message["content"].lower()

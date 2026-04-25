import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_answer(query):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Answer concisely and factually."},
                {"role": "user", "content": query}
            ]
        )
        return response.choices[0].message.content

    except:
        return f"Fallback answer for: {query}"
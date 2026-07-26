import os
from dotenv import load_dotenv
from groq import Groq
from prompt import build_prompt

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def retrieve_chunks(vector_store, question, k=4):
    results = vector_store.similarity_search(question, k=k)
    return results


def format_context(chunks):
    context_parts = []
    for chunk in chunks:
        source = chunk.metadata.get("source", "unknown")
        page = chunk.metadata.get("page", "?")
        context_parts.append(f"[{source}, page {page}]\n{chunk.page_content}")
    return "\n\n".join(context_parts)


def generate_answer(question, vector_store):
    chunks = retrieve_chunks(vector_store, question)

    if len(chunks) == 0:
        return "I could not find this information in the uploaded documents.", []

    context = format_context(chunks)
    prompt = build_prompt(context, question)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    answer = response.choices[0].message.content
    return answer, chunks
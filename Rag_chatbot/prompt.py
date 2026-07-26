PROMPT_TEMPLATE = """You are a document question-answering assistant.

Answer only using the context below. Do not use outside knowledge.
If the answer is not present in the context, reply exactly with:
"I could not find this information in the uploaded documents."

Context:
{context}

Question:
{question}

Answer:
"""


def build_prompt(context, question):
    return PROMPT_TEMPLATE.format(context=context, question=question)

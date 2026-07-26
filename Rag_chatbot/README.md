# Domain-Specific RAG Chatbot

A chatbot that answers questions from your own uploaded PDFs — course notes,
policies, manuals, or any document set. Built with Retrieval-Augmented
Generation (RAG), so answers are grounded in your documents, not the
model's general knowledge.

## How it works

1. Upload PDFs
2. Text is extracted page by page (`document_loader.py`)
3. Text is split into overlapping chunks (`vector_store.py`)
4. Chunks are converted into embeddings and stored in FAISS
5. Your question is embedded and matched against the closest chunks
6. The matched chunks + your question are sent to an LLM (Groq)
7. The answer is displayed along with its source document and page number

## Setup

1. Clone this repo and move into the folder:
```
git clone <your-repo-url>
cd domain_rag_chatbot
```

2. Create a virtual environment (optional but recommended):
```
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Get a free Groq API key from https://console.groq.com and add it:
```
cp .env.example .env
```
Then open `.env` and paste your key in.

5. Run the app:
```
streamlit run app.py
```

## Project structure

```
domain_rag_chatbot/
|-- app.py               Streamlit UI
|-- rag_pipeline.py       retrieval + LLM call
|-- document_loader.py    PDF text extraction
|-- vector_store.py       chunking + embeddings + FAISS
|-- prompt.py             grounded answer prompt template
|-- requirements.txt
|-- .env.example
|-- documents/            uploaded PDFs get saved here
|-- vector_store/         saved FAISS index (optional persistence)
```

## Notes

- The chatbot will refuse to answer if the information isn't in your
  uploaded documents, instead of making something up.
- Always verify high-stakes answers (legal, medical, financial) yourself.
- Do not upload confidential documents you don't have permission to share.

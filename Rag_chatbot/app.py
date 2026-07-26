import os
import streamlit as st
from dotenv import load_dotenv

from document_loader import load_pdfs
from vector_store import chunk_pages, build_vector_store
from rag_pipeline import generate_answer

load_dotenv()

st.set_page_config(page_title="Domain RAG Chatbot", layout="wide")
st.title("Domain-Specific RAG Chatbot")

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.sidebar:
    st.header("Upload Documents")
    uploaded_files = st.file_uploader(
        "Upload one or more PDFs", type=["pdf"], accept_multiple_files=True
    )

    if uploaded_files:
        for f in uploaded_files:
            st.write(f.name)

    if st.button("Process Documents"):
        if not uploaded_files:
            st.warning("Please upload at least one PDF first.")
        else:
            os.makedirs("documents", exist_ok=True)
            file_paths = []
            for f in uploaded_files:
                path = os.path.join("documents", f.name)
                with open(path, "wb") as out:
                    out.write(f.getbuffer())
                file_paths.append(path)

            with st.spinner("Extracting text and building vector store..."):
                pages = load_pdfs(file_paths)
                chunks = chunk_pages(pages)
                st.session_state.vector_store = build_vector_store(chunks)

            st.success(f"Processed {len(uploaded_files)} document(s) into {len(chunks)} chunks.")

    if st.button("Clear Chat"):
        st.session_state.chat_history = []

st.caption("Answers are generated only from your uploaded documents. Verify high-stakes information yourself.")

for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.write(message)

question = st.chat_input("Ask a question about your documents")

if question:
    if st.session_state.vector_store is None:
        st.warning("Please upload and process a document first.")
    else:
        st.session_state.chat_history.append(("user", question))
        with st.chat_message("user"):
            st.write(question)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer, sources = generate_answer(question, st.session_state.vector_store)
                st.write(answer)

                if sources:
                    with st.expander("Sources"):
                        for s in sources:
                            st.write(f"{s.metadata.get('source')} — page {s.metadata.get('page')}")

        st.session_state.chat_history.append(("assistant", answer))

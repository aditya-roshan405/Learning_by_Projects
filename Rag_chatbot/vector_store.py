from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document


def chunk_pages(pages, chunk_size=800, chunk_overlap=120):
    """
    Takes the list of page dicts from document_loader.py
    Splits each page's text into smaller chunks.
    Returns a list of LangChain Document objects (text + metadata).
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = []
    for page in pages:
        pieces = splitter.split_text(page["text"])
        for piece in pieces:
            chunks.append(Document(
                page_content=piece,
                metadata={"source": page["source"], "page": page["page"]}
            ))

    return chunks


def build_vector_store(chunks):
    """
    Converts chunks into embeddings and stores them in FAISS.
    Returns the FAISS vector store object.
    """
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(chunks, embedding_model)
    return vector_store


def save_vector_store(vector_store, path="vector_store/saved_index"):
    vector_store.save_local(path)


def load_vector_store(path="vector_store/saved_index"):
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.load_local(path, embedding_model, allow_dangerous_deserialization=True)

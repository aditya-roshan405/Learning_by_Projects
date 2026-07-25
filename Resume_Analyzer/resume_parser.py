"""
resume_parser.py
Reads a resume file (PDF or DOCX) and pulls out the raw text.
"""

from pypdf import PdfReader
import docx
from utils import get_file_extension


def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from a PDF resume."""
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text


def extract_text_from_docx(file_path: str) -> str:
    """Extract text from a DOCX resume."""
    document = docx.Document(file_path)
    text = ""
    for para in document.paragraphs:
        text += para.text + "\n"
    return text


def parse_resume(file_path: str) -> str:
    """
    Main function other files should call.
    Figures out the file type and extracts text accordingly.
    """
    ext = get_file_extension(file_path)

    if ext == ".pdf":
        text = extract_text_from_pdf(file_path)
    elif ext == ".docx":
        text = extract_text_from_docx(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}. Please upload PDF or DOCX.")

    if not text.strip():
        raise ValueError("No text could be extracted from this resume. It may be a scanned image.")

    return text


# quick test when running this file directly
if __name__ == "__main__":
    sample_path = "sample_resumes/sample.pdf"
    try:
        resume_text = parse_resume(sample_path)
        print(resume_text[:500])
    except Exception as e:
        print("Error:", e)

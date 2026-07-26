from pypdf import PdfReader


def load_pdfs(file_paths):
    """
    Takes a list of PDF file paths.
    Returns a list of dicts: {text, source, page}
    Each dict is one page of one PDF.
    """
    all_pages = []

    for path in file_paths:
        reader = PdfReader(path)
        file_name = path.split("/")[-1]

        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text()

            if text is None or text.strip() == "":
                continue

            all_pages.append({
                "text": text,
                "source": file_name,
                "page": page_number
            })

    return all_pages

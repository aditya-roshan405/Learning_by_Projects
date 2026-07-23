"""
text_cleaner.py
Cleans raw resume/job description text so it is ready for TF-IDF and
skill matching. Removes extra symbols, numbers, and stopwords.
"""

import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


def clean_text(text: str) -> str:
    """
    Lowercase the text, remove punctuation/numbers/extra spaces,
    and drop common stopwords like 'the', 'and', 'is'.
    """
    text = text.lower()

    # remove anything that is not a letter or space
    text = re.sub(r"[^a-z\s]", " ", text)

    # collapse multiple spaces into one
    text = re.sub(r"\s+", " ", text).strip()

    # remove stopwords
    words = text.split()
    words = [w for w in words if w not in ENGLISH_STOP_WORDS and len(w) > 1]

    return " ".join(words)


# quick test
if __name__ == "__main__":
    sample = "I have 3 years of experience in Python, SQL & Machine-Learning!!"
    print(clean_text(sample))

"""
utils.py
Small helper functions used by other files in the project.
"""

import os
import pandas as pd

# absolute path to the project's root folder (where this utils.py file lives)
# using this instead of a plain relative path means CSV loading works no
# matter which folder you run "streamlit run app.py" from
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.
    If a relative path like 'data/skill_dictionary.csv' is given, it is
    resolved relative to the project root, not the current working directory.
    """
    if not os.path.isabs(file_path):
        file_path = os.path.join(PROJECT_ROOT, file_path)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV file not found: {file_path}")
    return pd.read_csv(file_path)


def get_file_extension(file_path: str) -> str:
    """Return the lowercase file extension, e.g. '.pdf' or '.docx'."""
    _, ext = os.path.splitext(file_path)
    return ext.lower()


def skills_string_to_list(skills_string: str) -> list[str]:
    """Convert 'python,sql,excel' into ['python', 'sql', 'excel']."""
    if not skills_string:
        return []
    return [skill.strip().lower() for skill in skills_string.split(",")]
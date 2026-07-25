"""
utils.py
Small helper functions used by other files in the project.
"""

import os
import pandas as pd

# absolute path to the project's root folder (where this utils.py file lives)
# using this instead of a plain relative path means CSV loading works no
# matter which folder you run "streamlit run app.py" from
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame safely across all operating systems.
    """
    # Clean up any accidental mixed slashes from Windows string inputs
    file_path = file_path.replace("\\", "/")
    
    # If it's a relative path, join it with the project root
    if not os.path.isabs(file_path):
        # If your data folder is in the root directory alongside utils.py:
        full_path = os.path.join(PROJECT_ROOT, file_path)
    else:
        full_path = file_path

    # Normalize the final path to avoid slash conflicts
    full_path = os.path.normpath(full_path)

    if not os.path.exists(full_path):
        raise FileNotFoundError(f"CSV file not found at: {full_path}. Current Project Root: {PROJECT_ROOT}")
        
    return pd.read_csv(full_path)


def get_file_extension(file_path: str) -> str:
    """Return the lowercase file extension, e.g. '.pdf' or '.docx'."""
    _, ext = os.path.splitext(file_path)
    return ext.lower()


def skills_string_to_list(skills_string: str) -> list[str]:
    """Convert 'python,sql,excel' into ['python', 'sql', 'excel']."""
    if not skills_string:
        return []
    return [skill.strip().lower() for skill in skills_string.split(",")]

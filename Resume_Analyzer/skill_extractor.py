"""
skill_extractor.py
Finds which skills (from our skill_dictionary.csv) appear inside a
resume's text.
"""

from utils import load_csv


def get_all_skills(skill_csv_path: str = "data\skill_dictionary.csv") -> list[str]:
    """Load the master skill list from the CSV file."""
    df = load_csv(skill_csv_path)
    return df["skill"].str.lower().tolist()


def extract_skills(cleaned_text: str, skill_list: list[str]) -> list[str]:
    """
    Check each known skill against the resume text.
    Returns the list of skills found.
    """
    found_skills = []
    for skill in skill_list:
        # handle multi-word skills like "machine learning" or "power bi"
        if skill in cleaned_text:
            found_skills.append(skill)
    return found_skills


def find_missing_skills(resume_skills: list[str], required_skills: list[str]) -> list[str]:
    """Return the required skills that are NOT present in the resume."""
    return [skill for skill in required_skills if skill not in resume_skills]


# quick test
if __name__ == "__main__":
    all_skills = get_all_skills()
    text = "i know python sql and power bi for data analysis"
    print(extract_skills(text, all_skills))

"""
matcher.py
The core AI part of the project. Uses TF-IDF + Cosine Similarity to
compare a resume against a job description / job role, and also to
recommend the best matching job roles from our job_roles.csv.
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from utils import load_csv, skills_string_to_list
from text_cleaner import clean_text


def get_match_score(resume_text: str, job_text: str) -> float:
    """
    Compare resume text and job description text.
    Returns a similarity score between 0 and 100 (percentage).
    """
    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_text)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_clean, job_clean])

    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
    score = round(similarity[0][0] * 100, 2)
    return score


def recommend_job_roles(resume_text: str, job_roles_csv: str = "data/job_roles.csv", top_n: int = 3) -> pd.DataFrame:
    """
    Compare the resume against every job role's description and
    return the top N best matching roles, sorted by match score.
    """
    job_roles_df = load_csv(job_roles_csv)

    scores = []
    for _, row in job_roles_df.iterrows():
        job_text = row["role"] + " " + row["description"] + " " + row["required_skills"]
        score = get_match_score(resume_text, job_text)
        scores.append(score)

    job_roles_df["match_score"] = scores
    result = job_roles_df.sort_values(by="match_score", ascending=False)
    return result.head(top_n)


# quick test
if __name__ == "__main__":
    resume_sample = "I know python, sql, pandas and machine learning basics"
    job_sample = "Looking for python developer with sql and machine learning skills"
    print("Score:", get_match_score(resume_sample, job_sample))

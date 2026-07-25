"""
app.py
Main Streamlit app. This is the file you run to launch the project:
    streamlit run app.py

It connects all the other files together:
resume_parser -> text_cleaner -> skill_extractor -> matcher ->
roadmap_generator -> report_generator
"""

import os
import streamlit as st

from resume_parser import parse_resume
from text_cleaner import clean_text
from skill_extractor import get_all_skills, extract_skills, find_missing_skills
from matcher import get_match_score, recommend_job_roles
from roadmap_generator import generate_roadmap
from report_generator import generate_report
from utils import load_csv, skills_string_to_list


st.set_page_config(page_title="AI Resume Analyzer", layout="centered")
st.title("AI Resume Analyzer & Job Recommendation System")
st.write("Upload your resume and find out which job role fits you best.")

# make sure the folders we write to actually exist
os.makedirs("sample_resumes", exist_ok=True)
os.makedirs("reports", exist_ok=True)

uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file is not None:
    # save the uploaded file temporarily so resume_parser can read it
    temp_path = os.path.join("sample_resumes", uploaded_file.name)
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    try:
        with st.spinner("Reading your resume..."):
            resume_text = parse_resume(temp_path)
            cleaned_resume = clean_text(resume_text)

        st.success("Resume uploaded and read successfully!")

        # extract skills
        all_skills = get_all_skills()
        candidate_skills = extract_skills(cleaned_resume, all_skills)

        st.subheader("Skills Found in Your Resume")
        if candidate_skills:
            st.write(", ".join(candidate_skills))
        else:
            st.warning("No known skills were detected. Try adding a skills section.")

        # recommend job roles
        st.subheader("Top Matching Job Roles")
        top_roles = recommend_job_roles(resume_text, top_n=3)
        st.dataframe(top_roles[["role", "match_score"]])

        # pick the best role for the roadmap
        best_role_row = top_roles.iloc[0]
        best_role = best_role_row["role"]
        best_score = best_role_row["match_score"]
        required_skills = skills_string_to_list(best_role_row["required_skills"])

        missing_skills = find_missing_skills(candidate_skills, required_skills)

        st.subheader(f"Skill Gap for: {best_role}")
        if missing_skills:
            st.write("You are missing these skills for this role:")
            st.write(", ".join(missing_skills))
        else:
            st.success("You already have all the required skills for this role!")

        # roadmap
        roadmap = generate_roadmap(missing_skills)
        if roadmap:
            st.subheader("Suggested Learning Roadmap")
            for skill, tip in roadmap.items():
                st.write(f"**{skill}**: {tip}")

        # download report button
        if st.button("Generate Downloadable Report"):
            report_path = generate_report(
                candidate_skills=candidate_skills,
                matched_role=best_role,
                match_score=best_score,
                missing_skills=missing_skills,
                roadmap=roadmap,
            )
            with open(report_path, "rb") as f:
                st.download_button(
                    label="Download Report (.docx)",
                    data=f,
                    file_name="resume_report.docx",
                )

    except ValueError as e:
        st.error(f"Error: {e}")
    except Exception as e:
        st.error(f"Something went wrong: {e}")

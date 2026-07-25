# AI Resume Analyzer & Job Recommendation System

An AI-powered web app that analyzes a resume, matches it against job roles using **TF-IDF + Cosine Similarity**, highlights missing skills for the best-fit role, and generates a downloadable Word report with a personalized learning roadmap.

Built with Python, Streamlit, Pandas, NumPy, Scikit-learn, PyPDF, and python-docx.

---

## Features

- Upload a resume in **PDF** or **DOCX** format
- Automatically extracts and cleans resume text
- Detects known skills from a skill dictionary
- Matches the resume against multiple job roles using **TF-IDF vectorization** and **cosine similarity**
- Ranks and recommends the top 3 best-fitting job roles with a match score (%)
- Identifies missing skills for the best-matching role
- Suggests a learning roadmap for each missing skill
- Generates and downloads a full **.docx analysis report**

---

## Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.10+ |
| Web UI | Streamlit |
| Data Handling | Pandas, NumPy |
| Machine Learning / NLP | Scikit-learn (TF-IDF, Cosine Similarity) |
| File Parsing | PyPDF, python-docx |
| Report Generation | python-docx |

---

## Project Structure

```
Resume_Analyzer/
├── app.py                     # Streamlit entry point — run this file
├── resume_parser.py           # Extracts text from PDF/DOCX
├── text_cleaner.py            # Cleans text for NLP
├── skill_extractor.py         # Detects known skills in resume text
├── matcher.py                 # TF-IDF + cosine similarity matching
├── roadmap_generator.py       # Suggests learning resources
├── report_generator.py        # Builds the downloadable .docx report
├── utils.py                   # Shared helper functions
├── requirements.txt           # Python dependencies
├── data/
│   ├── skill_dictionary.csv   # Master list of known skills
│   └── job_roles.csv          # Job roles + required skills
├── sample_resumes/            # Temporary storage for uploaded resumes
└── reports/                   # Generated report output folder
```

---

## Installation & Setup

1. **Clone or download this repository** into a folder, e.g. `Resume_Analyzer/`.

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # Mac/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app** (always run this from inside the project folder):
   ```bash
   streamlit run app.py
   ```

5. Your browser will open automatically at `http://localhost:8501`.

---

## How It Works (Pipeline)

```
Resume (PDF/DOCX)
      │
      ▼
resume_parser.py      → extracts raw text
      │
      ▼
text_cleaner.py        → lowercases, removes punctuation/stopwords
      │
      ▼
skill_extractor.py      → finds known skills present in the text
      │
      ▼
matcher.py               → TF-IDF + cosine similarity vs. every job role
      │
      ▼
Best matching role + missing skills
      │
      ▼
roadmap_generator.py     → learning suggestions for missing skills
      │
      ▼
report_generator.py       → downloadable .docx report
```

---

## Troubleshooting

- **`CSV file not found` error:** Make sure `skill_dictionary.csv` and `job_roles.csv` actually exist inside the `data/` folder, with those exact filenames, and always run `streamlit run app.py` from inside the project root folder.
- **No skills detected:** Add a clear "Skills" section to the resume listing tools/technologies by name.
- **Unsupported file type error:** Only `.pdf` and `.docx` files are supported.

---

## Future Improvements

- Replace TF-IDF with sentence embeddings (e.g. `sentence-transformers`) for semantic matching
- Add an LLM-powered bullet-point rewriting assistant
- Move from CSV files to a PostgreSQL database
- Add user accounts to track resume history over time
- Deploy with a React/FastAPI stack for a production-grade UI

---

## Author

Built as a college major project — AI Resume Analyzer & Job Recommendation System.

## License

This project is for educational purposes.

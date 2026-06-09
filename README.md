# AI Resume Analyzer

An AI-powered Resume Analyzer built using Python and Streamlit.

## Features

- Resume PDF Upload
- Resume Text Extraction
- Name Extraction
- Email Extraction
- Phone Number Extraction
- Skill Detection
- ATS Score Calculation
- Job Match Analysis
- Missing Skills Detection
- Resume Recommendations
- PDF Report Download

# 🛠️ Tech Stack

### Frontend

- Streamlit

### Backend

- Python

### NLP

- SpaCy
- Regular Expressions

### Data Processing

- Pandas
- NumPy

### Resume Parsing

- PDFPlumber
- python-docx

### Reporting

- ReportLab

# 🏗️ Project Architecture

```text
                ┌─────────────────┐
                │ Resume PDF      │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ PDF Parser      │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Text Extraction │
                └────────┬────────┘
                         │
       ┌─────────────────┼─────────────────┐
       ▼                 ▼                 ▼

┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Skill Engine │ │ ATS Scoring  │ │ JD Matching  │
└──────┬───────┘ └──────┬───────┘ └──────┬───────┘
       │                │                │
       └────────────────┼────────────────┘
                        ▼

              ┌───────────────────┐
              │ Recommendation AI │
              └─────────┬─────────┘
                        ▼

              ┌───────────────────┐
              │ PDF Report Export │
              └───────────────────┘
```

### Project Structure
AI-Resume-Analyzer
│
├── app.py
├── resume_parser.py
├── skill_extractor.py
├── ats_score.py
├── job_matcher.py
├── recommendation_engine.py
├── pdf_generator.py
├── requirements.txt
└── README.md

# 📊 ATS Scoring Methodology

The ATS score is calculated using:

| Criteria | Weight |
|-----------|----------|
| Keyword Match | 50% |
| Projects | 20% |
| Education | 10% |
| Experience | 10% |
| Resume Formatting | 10% |

### Formula

```text
ATS Score =
Keyword Score +
Project Score +
Education Score +
Experience Score +
Formatting Score

# 🎯 Supported Job Roles

- Data Analyst
- Data Scientist
- AI Engineer
- Machine Learning
- Generative AI
- Web development
- Cloud
- Cyber security
- Deep learning

## Future Enhancements
- Gemini AI Integration
- Resume vs JD Semantic Matching
- ATS Dashboard
- Resume Improvement Suggestions

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/AI-Resume-Analyzer.git
```

```bash
cd AI-Resume-Analyzer
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Download SpaCy Model

```bash
python -m spacy download en_core_web_sm
```

---

## Run Application

```bash
streamlit run app.py
```

---
# 👩‍💻 Author

**Hitika Vij**

B.Tech CSE (AI & DS)

Passionate about:
- Artificial Intelligence
- Machine Learning
- Data Analytics
- NLP Applications

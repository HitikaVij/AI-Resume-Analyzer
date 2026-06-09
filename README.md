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

## Technologies Used

- Python
- Streamlit
- SpaCy
- PDFPlumber
- Scikit-learn
- ReportLab

## Installation

```bash
pip install -r requirements.txt
streamlit run app.py

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

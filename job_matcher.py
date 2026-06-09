def calculate_job_match(resume_skills, job_skills):

    matched_skills = []

    missing_skills = []

    for skill in job_skills:

        if skill in resume_skills:
            matched_skills.append(skill)

        else:
            missing_skills.append(skill)

    match_score = (
        len(matched_skills) / len(job_skills)
    ) * 100

    return round(match_score, 2), missing_skills

JOB_ROLES = {

    "Data Analyst": [
        "Python",
        "SQL",
        "Excel",
        "Power BI",
        "Statistics"
    ],

    "Data Scientist": [
        "Python",
        "SQL",
        "Machine Learning",
        "Pandas",
        "Statistics"
    ],

    "AI Engineer": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "NLP"
    ],
    
    "Machine Learning": [
        "Deep Learning",
        "Scikit-learn",
        "TensorFlow",
        "PyTorch",
        "NLP"
        ],

    "Generative AI": [
        "Prompt Engineering",
        "LangChain",
        "OpenAI",
        "ChatGPT",
        "Gemini",
        "RAG"],

    "Web Development": [
        "HTML",
        "CSS",
        "Bootstrap",
        "React",
        "Node.js",
        "Express.js",
        "Flask",
        "Django"],

    "Cloud": [
        "AWS",
        "Azure",
        "Google Cloud"],

    "Cyber Security": [
        "Network Security",
        "Penetration Testing",
        "Ethical Hacking"],

    "Deep Learning": [
        "TensorFlow",
        "Keras",
        "PyTorch",
        "CNN",
        "RNN",
        "LSTM"],

}
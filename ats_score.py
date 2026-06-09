import re

def calculate_ats_score(resume_text, resume_skills, job_skills):

    # ==========================
    # 1. Keyword Match (50 Marks)
    # ==========================

    matched_skills = [
        skill for skill in job_skills
        if skill in resume_skills
    ]

    keyword_score = (
        len(matched_skills) / len(job_skills)
    ) * 50

    # ==========================
    # 2. Projects Score (20 Marks)
    # ==========================

    project_keywords = [
        "project",
        "machine learning",
        "prediction",
        "classification",
        "dashboard",
        "analysis",
        "chatbot",
        "ai"
    ]

    project_count = 0

    for keyword in project_keywords:
        if keyword.lower() in resume_text.lower():
            project_count += 1

    project_score = min(project_count * 3, 20)

    # ==========================
    # 3. Education Score (10 Marks)
    # ==========================

    education_keywords = [
        "b.tech",
        "bachelor",
        "engineering",
        "computer science",
        "data science",
        "artificial intelligence",
        "ai"
    ]

    education_score = 0

    for keyword in education_keywords:
        if keyword.lower() in resume_text.lower():
            education_score = 10
            break

    # ==========================
    # 4. Experience Score (10 Marks)
    # ==========================

    experience_keywords = [
        "internship",
        "intern",
        "experience",
        "freelance",
        "training",
        "trainee"
    ]

    experience_score = 0

    for keyword in experience_keywords:
        if keyword.lower() in resume_text.lower():
            experience_score = 10
            break

    # ==========================
    # 5. Formatting Score (10 Marks)
    # ==========================

    required_sections = [
        "education",
        "skills",
        "projects",
        "experience"
    ]

    section_count = 0

    for section in required_sections:
        if section.lower() in resume_text.lower():
            section_count += 1

    formatting_score = (
        section_count / len(required_sections)
    ) * 10

    # ==========================
    # Final ATS Score
    # ==========================

    total_score = (
        keyword_score +
        project_score +
        education_score +
        experience_score +
        formatting_score
    )

    return {
        "ats_score": round(total_score, 2),
        "keyword_score": round(keyword_score, 2),
        "project_score": round(project_score, 2),
        "education_score": round(education_score, 2),
        "experience_score": round(experience_score, 2),
        "formatting_score": round(formatting_score, 2)
    }
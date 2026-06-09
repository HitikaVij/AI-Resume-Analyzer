import streamlit as st
import matplotlib.pyplot as plt
from resume_parser import extract_text_from_pdf
from skill_extractor import (
    extract_email,
    extract_phone,
    extract_name
)
from skill_extractor import extract_skills
from score_calculator import calculate_score
from recommendation_engine import get_recommendations
from job_matcher import (
    calculate_job_match,
    JOB_ROLES
)
from ats_score import calculate_ats_score
from pdf_generator import generate_pdf
from datetime import datetime

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Your Resume",
    type=["pdf"]
)

selected_role = st.selectbox(

    "Select Target Job Role",

    list(JOB_ROLES.keys())

)

if uploaded_file is not None:
    
    st.success("Resume Uploaded Successfully!")

    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=300
    )
    
    email = extract_email(resume_text)

    phone = extract_phone(resume_text)

    name = extract_name(resume_text)

    skills = extract_skills(resume_text) 

    job_skills = JOB_ROLES[selected_role]

    match_score, missing_skills = calculate_job_match(
        skills,
        job_skills
    )

    ats_report = calculate_ats_score(
    resume_text,
    skills,
    job_skills
    )
    score = calculate_score(skills)

    recommendations = get_recommendations(skills)

    st.subheader("Candidate Information")

    st.write("Name:", name)

    st.write("Email:", email)

    st.write("Phone:", phone)

    st.subheader("Detected Skills")

    st.subheader("Detected Skills")

    col1, col2 = st.columns(2)

    for i, skill in enumerate(skills):

        if i % 2 == 0:
            col1.write(f"✔ {skill}")
        else:
            col2.write(f"✔ {skill}")
    st.write("Total Skills Found:", len(skills))

    st.subheader("Resume Score")

    st.subheader("Resume Score")

    st.progress(int(score))

    st.metric(
        "Resume Score",
        f"{score}%"
    )

    if score >= 80:
        st.success("Excellent Resume")

    elif score >= 60:
        st.warning("Good Resume - Can Be Improved")

    else:
        st.error("Needs Improvement")

    st.subheader("Recommendations")

    for rec in recommendations:
        st.write("👉", rec)
    st.subheader("Job Match Analysis")

    st.metric(
        "Job Match Score",
        f"{match_score}%"
    )
    st.subheader("Missing Skills")

    # for skill in missing_skills:
    #     st.write("❌", skill)

    for skill in missing_skills:
        st.warning(skill)

    st.subheader("Skill Analysis")

    fig, ax = plt.subplots()

    ax.bar(
        ["Detected", "Missing"],
        [len(skills), len(missing_skills)]
    )

    st.pyplot(fig)

    st.subheader("ATS Score Report")

    st.metric(
        "Overall ATS Score",
        f"{ats_report['ats_score']}/100"
    )

    st.write(
        f"Keyword Match: {ats_report['keyword_score']}/50"
    )

    st.write(
        f"Projects: {ats_report['project_score']}/20"
    )

    st.write(
        f"Education: {ats_report['education_score']}/10"
    )

    st.write(
        f"Experience: {ats_report['experience_score']}/10"
    )

    st.write(
        f"Formatting: {ats_report['formatting_score']}/10"
    )

    ats = ats_report["ats_score"]

    if ats >= 85:
        st.success(
            "Excellent ATS Resume"
        )

    elif ats >= 70:
        st.warning(
            "Good Resume - Minor Improvements Needed"
        )

    else:
        st.error(
            "ATS Score Low - Resume Needs Optimization"
        )

    current_time = datetime.now().strftime(
        "%d-%m-%Y %H:%M"
    )


    report = f"""
    AI RESUME ANALYZER REPORT

    ========================================

    CANDIDATE DETAILS

    Name: {name}
    Email: {email}
    Phone: {phone}

    ========================================

    TARGET JOB ROLE

    {selected_role}

    ========================================

    ATS ANALYSIS

    Overall ATS Score: {ats_report['ats_score']}/100

    Keyword Match: {ats_report['keyword_score']}/50

    Projects Score: {ats_report['project_score']}/20

    Education Score: {ats_report['education_score']}/10

    Experience Score: {ats_report['experience_score']}/10

    Formatting Score: {ats_report['formatting_score']}/10

    ========================================

    JOB MATCH ANALYSIS

    Match Score: {match_score}%

    ========================================

    DETECTED SKILLS

    {chr(10).join(['• ' + skill for skill in skills])}

    ========================================

    MISSING SKILLS

    {chr(10).join(['• ' + skill for skill in missing_skills])}

    ========================================

    RECOMMENDATIONS

    {chr(10).join(['• ' + rec for rec in recommendations])}

    ========================================
    Generated On: {current_time}
    Generated by AI Resume Analyzer
    """

    pdf_file = generate_pdf(
        report,
        "ATS_Report.pdf"
    )

    with open(pdf_file, "rb") as file:

        st.download_button(
            label="📄 Download Professional ATS Report",
            data=file,
            file_name="ATS_Report.pdf",
            mime="application/pdf"
        )

   
   
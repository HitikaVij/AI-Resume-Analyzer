def get_recommendations(skills):

    recommendations = []

    important_skills = [
        "Python",
        "SQL",
        "Power BI",
        "Machine Learning",
        "GitHub",
        "Statistics",
        "Excel",
        "Tableau"
    ]

    for skill in important_skills:
        if skill not in skills:
            recommendations.append(f"Consider learning {skill}")

    return recommendations
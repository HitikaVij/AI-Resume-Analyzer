def calculate_score(skills):

    total_possible_skills = 30

    score = min((len(skills) / total_possible_skills) * 100, 100)

    return round(score, 2)
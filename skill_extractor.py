import re
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_email(text):
    pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

    emails = re.findall(pattern, text)

    if emails:
        return emails[0]

    return "Not Found"


def extract_phone(text):
    pattern = r'\b\d{10}\b'

    phones = re.findall(pattern, text)

    if phones:
        return phones[0]

    return "Not Found"


def extract_name(text):
    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text

    return "Not Found"

def extract_skills(text):

    skills_db = [

    # Programming Languages
    "Python", "Java", "C", "C++", "C#", "JavaScript", "TypeScript",
    "PHP", "R", "Go", "Kotlin", "Swift",

    # Web Development
    "HTML", "CSS", "Bootstrap", "Tailwind CSS",
    "React", "Angular", "Vue.js",
    "Node.js", "Express.js",
    "Django", "Flask", "FastAPI",
    "REST API",

    # Databases
    "SQL", "MySQL", "PostgreSQL",
    "MongoDB", "SQLite", "Oracle",
    "Firebase",

    # Data Analysis
    "Excel", "Power BI", "Tableau",
    "Data Analysis", "Data Visualization",
    "Statistics", "Business Analytics",

    # Data Science
    "Pandas", "NumPy", "Matplotlib",
    "Seaborn", "SciPy", "Jupyter Notebook",

    # Machine Learning
    "Machine Learning",
    "Supervised Learning",
    "Unsupervised Learning",
    "Regression",
    "Classification",
    "Clustering",
    "Feature Engineering",

    # Deep Learning
    "Deep Learning",
    "TensorFlow",
    "Keras",
    "PyTorch",
    "CNN",
    "RNN",
    "LSTM",

    # AI / NLP
    "NLP",
    "Natural Language Processing",
    "Sentiment Analysis",
    "Text Classification",
    "Named Entity Recognition",

    # Generative AI
    "Generative AI",
    "Prompt Engineering",
    "OpenAI",
    "ChatGPT",
    "Gemini",
    "Claude",
    "LangChain",
    "LlamaIndex",
    "RAG",
    "Vector Database",
    "FAISS",
    "Pinecone",

    # Cloud Computing
    "AWS",
    "Azure",
    "Google Cloud",
    "Docker",
    "Kubernetes",

    # DevOps
    "Git",
    "GitHub",
    "GitLab",
    "CI/CD",
    "Jenkins",

    # Cyber Security
    "Ethical Hacking",
    "Network Security",
    "Penetration Testing",
    "Cryptography",

    # Mobile Development
    "Android",
    "Flutter",
    "React Native",

    # Operating Systems
    "Linux",
    "Windows",

    # Soft Skills
    "Communication",
    "Leadership",
    "Teamwork",
    "Problem Solving",
    "Critical Thinking",
    "Time Management",
    "Presentation Skills",

    # Project Management
    "Agile",
    "Scrum",
    "JIRA",

    # Testing
    "Unit Testing",
    "Selenium",
    "Manual Testing",

    # AI & DS Specific
    "Computer Vision",
    "Image Processing",
    "Recommendation Systems",
    "Time Series Analysis",
    "Big Data",
    "Hadoop",
    "Spark"
    ]

    found_skills = []

    for skill in skills_db:

        pattern = r'\b' + re.escape(skill) + r'\b'

        if re.search(pattern, text, re.IGNORECASE):
            found_skills.append(skill)

    return found_skills
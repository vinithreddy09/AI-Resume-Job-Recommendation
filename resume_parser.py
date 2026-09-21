import os
import re

from PyPDF2 import PdfReader
from docx import Document


# --------------------------------------------------
# PDF TEXT EXTRACTION
# --------------------------------------------------

def extract_pdf_text(file_path):

    text = ""

    reader = PdfReader(file_path)

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


# --------------------------------------------------
# DOCX TEXT EXTRACTION
# --------------------------------------------------

def extract_docx_text(file_path):

    document = Document(file_path)

    text = []

    for paragraph in document.paragraphs:

        if paragraph.text.strip():
            text.append(paragraph.text.strip())

    return "\n".join(text)


# --------------------------------------------------
# GENERAL RESUME TEXT EXTRACTION
# --------------------------------------------------

def extract_resume_text(file_path):

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":

        return extract_pdf_text(file_path)

    elif extension == ".docx":

        return extract_docx_text(file_path)

    else:

        raise ValueError(
            "Unsupported file format. Please upload PDF or DOCX."
        )


# --------------------------------------------------
# EMAIL EXTRACTION
# --------------------------------------------------

def extract_email(text):

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group(0)

    return "Not found"


# --------------------------------------------------
# PHONE NUMBER EXTRACTION
# --------------------------------------------------

def extract_phone(text):

    patterns = [
        r"\+91[\s-]?\d{10}",
        r"\+91[\s-]?\d{5}[\s-]?\d{5}",
        r"\b\d{10}\b",
        r"\b\d{5}[\s-]\d{5}\b"
    ]

    for pattern in patterns:

        match = re.search(pattern, text)

        if match:
            return match.group(0)

    return "Not found"


# --------------------------------------------------
# NAME EXTRACTION
# --------------------------------------------------

def extract_name(text):

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    # First try common name labels
    for line in lines[:15]:

        lower_line = line.lower()

        if lower_line.startswith("name:"):

            name = line.split(":", 1)[1].strip()

            if name:
                return name

        if lower_line.startswith("name -"):

            name = line.split("-", 1)[1].strip()

            if name:
                return name

    # Otherwise use the first suitable line
    for line in lines[:10]:

        clean_line = re.sub(
            r"[^A-Za-z.\s]",
            "",
            line
        ).strip()

        words = clean_line.split()

        if 2 <= len(words) <= 5:

            excluded_words = [
                "resume",
                "curriculum vitae",
                "cv",
                "profile",
                "objective",
                "summary",
                "education",
                "skills",
                "experience"
            ]

            if clean_line.lower() not in excluded_words:

                return clean_line

    return "Not found"


# --------------------------------------------------
# SKILL EXTRACTION
# --------------------------------------------------

SKILL_LIST = [

    "Python",
    "Java",
    "C",
    "C++",
    "C#",
    "JavaScript",
    "HTML",
    "CSS",
    "React",
    "Angular",
    "Node.js",

    "SQL",
    "MySQL",
    "PostgreSQL",
    "MongoDB",
    "Oracle",

    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "Data Science",
    "Natural Language Processing",
    "NLP",

    "Pandas",
    "NumPy",
    "Scikit-learn",
    "TensorFlow",
    "PyTorch",

    "Flask",
    "Django",

    "Power BI",
    "Tableau",
    "Excel",

    "Git",
    "GitHub",

    "AWS",
    "Azure",
    "Google Cloud",

    "Statistics",
    "Data Analysis",
    "Communication",
    "Problem Solving"
]


def extract_skills(text):

    found_skills = []

    text_lower = text.lower()

    for skill in SKILL_LIST:

        skill_lower = skill.lower()

        if skill_lower in text_lower:

            found_skills.append(skill)

    return found_skills


# --------------------------------------------------
# EDUCATION EXTRACTION
# --------------------------------------------------

def extract_education(text):

    lines = text.splitlines()

    education_keywords = [
        "education",
        "b.tech",
        "btech",
        "bachelor",
        "degree",
        "b.sc",
        "bca",
        "m.tech",
        "mtech",
        "mca",
        "m.sc",
        "intermediate",
        "12th",
        "10th",
        "ssc",
        "diploma",
        "university",
        "college"
    ]

    education_lines = []

    for line in lines:

        line_clean = line.strip()

        if not line_clean:
            continue

        lower_line = line_clean.lower()

        if any(
            keyword in lower_line
            for keyword in education_keywords
        ):

            education_lines.append(line_clean)

    if education_lines:

        return "\n".join(education_lines[:10])

    return "Not found"


# --------------------------------------------------
# EXPERIENCE EXTRACTION
# --------------------------------------------------

def extract_experience(text):

    lines = text.splitlines()

    experience_keywords = [
        "experience",
        "internship",
        "intern",
        "work experience",
        "professional experience",
        "employment",
        "developer",
        "analyst",
        "engineer"
    ]

    experience_lines = []

    capture = False

    for line in lines:

        line_clean = line.strip()

        if not line_clean:
            continue

        lower_line = line_clean.lower()

        if any(
            keyword in lower_line
            for keyword in experience_keywords
        ):

            capture = True

        if capture:

            experience_lines.append(line_clean)

        if len(experience_lines) >= 15:

            break

    if experience_lines:

        return "\n".join(experience_lines)

    return "Not found"


# --------------------------------------------------
# COMPLETE RESUME ANALYSIS
# --------------------------------------------------

def analyze_resume(file_path):

    text = extract_resume_text(file_path)

    result = {

        "name": extract_name(text),

        "email": extract_email(text),

        "phone": extract_phone(text),

        "skills": extract_skills(text),

        "education": extract_education(text),

        "experience": extract_experience(text),

        "resume_text": text
    }

    return result
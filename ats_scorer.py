import re


def calculate_ats_score(resume_data):
    """
    Calculate a professional ATS-style resume score out of 100.
    """

    resume_text = str(resume_data.get("resume_text", ""))
    skills = resume_data.get("skills", [])
    education = str(resume_data.get("education", ""))
    experience = str(resume_data.get("experience", ""))

    name = str(resume_data.get("name", ""))
    email = str(resume_data.get("email", ""))
    phone = str(resume_data.get("phone", ""))

    suggestions = []

    # =========================================================
    # 1. CONTACT INFORMATION - 15 POINTS
    # =========================================================

    contact_score = 0

    if name and name.lower() != "not found":
        contact_score += 5
    else:
        suggestions.append(
            "Add your full name clearly at the top of the resume."
        )

    if email and email.lower() != "not found":
        contact_score += 5
    else:
        suggestions.append(
            "Add a professional email address."
        )

    if phone and phone.lower() != "not found":
        contact_score += 5
    else:
        suggestions.append(
            "Add a valid phone number."
        )

    # =========================================================
    # 2. SKILLS - 25 POINTS
    # =========================================================

    skill_count = len(skills)

    if skill_count >= 10:
        skill_score = 25
    elif skill_count >= 8:
        skill_score = 22
    elif skill_count >= 6:
        skill_score = 18
    elif skill_count >= 4:
        skill_score = 14
    elif skill_count >= 2:
        skill_score = 8
    elif skill_count == 1:
        skill_score = 4
    else:
        skill_score = 0
        suggestions.append(
            "Add a dedicated Technical Skills section."
        )

    if skill_count < 8:
        suggestions.append(
            "Add more relevant technical skills to improve ATS keyword coverage."
        )

    # =========================================================
    # 3. EDUCATION - 15 POINTS
    # =========================================================

    education_score = 0

    education_lower = education.lower()

    if education and education_lower != "not found":

        education_keywords = [
            "b.tech",
            "btech",
            "bachelor",
            "b.sc",
            "bca",
            "m.tech",
            "mtech",
            "mca",
            "m.sc",
            "degree",
            "engineering",
            "university",
            "college"
        ]

        if any(keyword in education_lower for keyword in education_keywords):
            education_score = 15
        else:
            education_score = 10

    else:
        suggestions.append(
            "Add your education details clearly."
        )

    # =========================================================
    # 4. EXPERIENCE / PROJECTS - 20 POINTS
    # =========================================================

    experience_score = 0

    experience_lower = experience.lower()
    text_lower = resume_text.lower()

    experience_keywords = [
        "experience",
        "internship",
        "intern",
        "developer",
        "engineer",
        "analyst",
        "project",
        "work experience"
    ]

    experience_matches = sum(
        1
        for keyword in experience_keywords
        if keyword in experience_lower or keyword in text_lower
    )

    if experience_matches >= 5:
        experience_score = 20
    elif experience_matches >= 3:
        experience_score = 16
    elif experience_matches >= 2:
        experience_score = 12
    elif experience_matches >= 1:
        experience_score = 8
    else:
        experience_score = 0
        suggestions.append(
            "Add internship, project, or work experience details."
        )

    # =========================================================
    # 5. RESUME CONTENT / SECTIONS - 15 POINTS
    # =========================================================

    important_sections = {
        "summary": [
            "summary",
            "profile",
            "objective"
        ],

        "skills": [
            "skills",
            "technical skills"
        ],

        "education": [
            "education",
            "academic"
        ],

        "projects": [
            "projects",
            "project"
        ],

        "experience": [
            "experience",
            "internship",
            "employment"
        ],

        "certifications": [
            "certification",
            "certifications"
        ]
    }

    detected_sections = 0
    detected_section_names = []

    for section, keywords in important_sections.items():

        if any(keyword in text_lower for keyword in keywords):
            detected_sections += 1
            detected_section_names.append(section)

    content_score = min(detected_sections * 2.5, 15)

    if "project" not in text_lower:
        suggestions.append(
            "Add a Projects section describing your technical projects."
        )

    if (
        "certification" not in text_lower
        and "certifications" not in text_lower
    ):
        suggestions.append(
            "Add relevant certifications if available."
        )

    # =========================================================
    # 6. FORMATTING / KEYWORD QUALITY - 10 POINTS
    # =========================================================

    formatting_score = 0

    # Reasonable resume length
    word_count = len(resume_text.split())

    if word_count >= 300:
        formatting_score += 3
    elif word_count >= 150:
        formatting_score += 2
    elif word_count >= 75:
        formatting_score += 1
    else:
        suggestions.append(
            "Add more detailed resume content."
        )

    # Email format check
    email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if email != "Not found" and re.match(email_pattern, email):
        formatting_score += 2
    else:
        suggestions.append(
            "Use a valid professional email format."
        )

    # Technical keyword coverage
    technical_keywords = [
        "python",
        "java",
        "sql",
        "javascript",
        "machine learning",
        "data science",
        "flask",
        "react",
        "power bi",
        "excel",
        "aws",
        "azure",
        "git",
        "html",
        "css"
    ]

    keyword_matches = sum(
        1
        for keyword in technical_keywords
        if keyword in text_lower
    )

    if keyword_matches >= 8:
        formatting_score += 5
    elif keyword_matches >= 5:
        formatting_score += 4
    elif keyword_matches >= 3:
        formatting_score += 3
    elif keyword_matches >= 1:
        formatting_score += 2
    else:
        formatting_score += 0
        suggestions.append(
            "Include relevant technical keywords from your target job."
        )

    # Maximum 10
    formatting_score = min(formatting_score, 10)

    # =========================================================
    # FINAL SCORE
    # =========================================================

    final_score = (
        contact_score
        + skill_score
        + education_score
        + experience_score
        + content_score
        + formatting_score
    )

    final_score = round(min(final_score, 100), 2)

    # =========================================================
    # SCORE LEVEL
    # =========================================================

    if final_score >= 85:
        level = "Excellent"
        message = (
            "Your resume has strong ATS compatibility "
            "and good keyword coverage."
        )

    elif final_score >= 70:
        level = "Good"
        message = (
            "Your resume has good ATS compatibility "
            "but can still be improved."
        )

    elif final_score >= 50:
        level = "Average"
        message = (
            "Your resume has moderate ATS compatibility "
            "and needs some improvements."
        )

    else:
        level = "Needs Improvement"
        message = (
            "Your resume needs significant improvements "
            "for better ATS compatibility."
        )

    # Remove duplicate suggestions
    unique_suggestions = []

    for suggestion in suggestions:
        if suggestion not in unique_suggestions:
            unique_suggestions.append(suggestion)

    return {
        "score": final_score,
        "level": level,
        "message": message,

        "contact_score": contact_score,
        "skill_score": skill_score,
        "education_score": education_score,
        "experience_score": experience_score,
        "content_score": content_score,
        "formatting_score": formatting_score,

        "skills_detected": skill_count,
        "sections_detected": detected_sections,
        "sections": detected_section_names,

        "suggestions": unique_suggestions[:8]
    }
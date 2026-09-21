from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(resume_text, job_description):

    if not resume_text or not job_description:
        return 0.0

    documents = [
        resume_text,
        job_description
    ]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    vectors = vectorizer.fit_transform(
        documents
    )

    similarity = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0]

    return round(
        similarity * 100,
        2
    )


def calculate_skill_match(
        resume_skills,
        required_skills
):

    if not required_skills:
        return 0.0

    resume_set = {
        skill.strip().lower()
        for skill in resume_skills
    }

    job_set = {
        skill.strip().lower()
        for skill in required_skills.split(",")
    }

    matched = resume_set.intersection(
        job_set
    )

    score = (
        len(matched)
        / len(job_set)
    ) * 100

    return round(
        score,
        2
    )


def calculate_education_score(
        education
):

    if not education:
        return 0

    education_text = education.lower()

    keywords = [
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
        "engineering"
    ]

    for keyword in keywords:

        if keyword in education_text:
            return 100

    return 50


def calculate_experience_score(
        experience
):

    if not experience:
        return 20

    experience_text = experience.lower()

    if experience_text == "not found":
        return 20

    keywords = [
        "experience",
        "internship",
        "intern",
        "developer",
        "engineer",
        "analyst",
        "project"
    ]

    matches = sum(
        1
        for keyword in keywords
        if keyword in experience_text
    )

    if matches >= 3:
        return 100

    if matches == 2:
        return 80

    if matches == 1:
        return 60

    return 40


def calculate_overall_score(
        skill_score,
        nlp_score,
        education_score,
        experience_score
):

    overall = (

        (skill_score * 0.30)

        + (nlp_score * 0.30)

        + (education_score * 0.20)

        + (experience_score * 0.20)

    )

    return round(
        overall,
        2
    )
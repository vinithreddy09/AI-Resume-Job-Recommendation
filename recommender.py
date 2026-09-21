import pandas as pd

from nlp_model import (
    calculate_similarity,
    calculate_skill_match,
    calculate_education_score,
    calculate_experience_score,
    calculate_overall_score
)


def load_jobs():
    """
    Load available jobs from CSV.
    """
    jobs = pd.read_csv("data/jobs.csv")
    return jobs.to_dict(orient="records")


def normalize_skill(skill):
    """
    Normalize skill names for comparison.
    """
    return skill.strip().lower()


def find_matched_skills(resume_skills, job_skills):
    """
    Find skills present in both resume and job requirements.
    """

    resume_set = {
        normalize_skill(skill)
        for skill in resume_skills
    }

    job_skill_list = [
        skill.strip()
        for skill in job_skills.split(",")
        if skill.strip()
    ]

    matched = []

    for skill in job_skill_list:
        if normalize_skill(skill) in resume_set:
            matched.append(skill)

    return matched


def find_missing_skills(resume_skills, job_skills):
    """
    Find skills required by the job but missing from the resume.
    """

    resume_set = {
        normalize_skill(skill)
        for skill in resume_skills
    }

    job_skill_list = [
        skill.strip()
        for skill in job_skills.split(",")
        if skill.strip()
    ]

    missing = []

    for skill in job_skill_list:
        if normalize_skill(skill) not in resume_set:
            missing.append(skill)

    return missing


def get_recommendation_level(score):
    """
    Convert numerical match score into a recommendation level.
    """

    if score >= 85:
        return "Excellent Match"

    elif score >= 70:
        return "Strong Match"

    elif score >= 55:
        return "Good Match"

    elif score >= 40:
        return "Moderate Match"

    else:
        return "Low Match"


def recommend_jobs(
    resume_text,
    resume_skills,
    education="",
    experience=""
):
    """
    Generate job recommendations using:
    - Skill matching
    - NLP similarity
    - Education
    - Experience
    """

    jobs = load_jobs()

    recommendations = []

    education_score = calculate_education_score(
        education
    )

    experience_score = calculate_experience_score(
        experience
    )

    for job in jobs:

        # -------------------------------------------------
        # NLP MATCH
        # -------------------------------------------------

        nlp_score = calculate_similarity(
            resume_text,
            job["description"]
        )

        # -------------------------------------------------
        # SKILL MATCH
        # -------------------------------------------------

        skill_score = calculate_skill_match(
            resume_skills,
            job["skills"]
        )

        # -------------------------------------------------
        # OVERALL MATCH
        # -------------------------------------------------

        overall_score = calculate_overall_score(
            skill_score,
            nlp_score,
            education_score,
            experience_score
        )

        # -------------------------------------------------
        # MATCHED / MISSING SKILLS
        # -------------------------------------------------

        matched_skills = find_matched_skills(
            resume_skills,
            job["skills"]
        )

        missing_skills = find_missing_skills(
            resume_skills,
            job["skills"]
        )

        # -------------------------------------------------
        # RECOMMENDATION LEVEL
        # -------------------------------------------------

        recommendation_level = get_recommendation_level(
            overall_score
        )

        # -------------------------------------------------
        # MATCH PERCENTAGE
        # -------------------------------------------------

        match_percentage = round(
            overall_score,
            2
        )

        recommendations.append({

            "title": job["title"],

            "company": job["company"],

            "score": overall_score,

            "match_percentage": match_percentage,

            "nlp_score": nlp_score,

            "skill_score": skill_score,

            "education_score": education_score,

            "experience_score": experience_score,

            "skills": job["skills"],

            "matched_skills": matched_skills,

            "missing_skills": missing_skills,

            "recommendation_level":
                recommendation_level,

            "description":
                job["description"]
        })

    # -----------------------------------------------------
    # SORT BY BEST MATCH
    # -----------------------------------------------------

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    # -----------------------------------------------------
    # ADD RANK
    # -----------------------------------------------------

    for index, recommendation in enumerate(
        recommendations,
        start=1
    ):
        recommendation["rank"] = index

    # Return top 5 jobs
    return recommendations[:5]
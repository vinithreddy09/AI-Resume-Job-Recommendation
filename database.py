import sqlite3


DATABASE_NAME = "resume_screening.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            skills TEXT,
            education TEXT,
            experience TEXT,
            resume_file TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            skills TEXT,
            description TEXT,
            location TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recommendations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            candidate_id INTEGER,
            job_title TEXT,
            company TEXT,
            match_score REAL,
            missing_skills TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_candidate(candidate):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO candidates
        (
            name,
            email,
            phone,
            skills,
            education,
            experience,
            resume_file
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        candidate["name"],
        candidate["email"],
        candidate["phone"],
        ", ".join(candidate["skills"]),
        candidate["education"],
        candidate["experience"],
        candidate["resume_file"]
    ))

    candidate_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return candidate_id


def save_recommendations(candidate_id, recommendations):

    connection = get_connection()
    cursor = connection.cursor()

    for job in recommendations:

        cursor.execute("""
            INSERT INTO recommendations
            (
                candidate_id,
                job_title,
                company,
                match_score,
                missing_skills
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            candidate_id,
            job["title"],
            job["company"],
            job["score"],
            ", ".join(job["missing_skills"])
        ))

    connection.commit()
    connection.close()


def get_candidates():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM candidates
        ORDER BY id DESC
    """)

    candidates = cursor.fetchall()

    connection.close()

    return candidates


def get_dashboard_statistics():

    connection = get_connection()
    cursor = connection.cursor()

    # Total resumes
    cursor.execute("""
        SELECT COUNT(*)
        FROM candidates
    """)

    total_candidates = cursor.fetchone()[0]

    # Total recommendations
    cursor.execute("""
        SELECT COUNT(*)
        FROM recommendations
    """)

    total_recommendations = cursor.fetchone()[0]

    # Average match score
    cursor.execute("""
        SELECT AVG(match_score)
        FROM recommendations
    """)

    average_score = cursor.fetchone()[0]

    if average_score is None:
        average_score = 0

    # Highest match
    cursor.execute("""
        SELECT MAX(match_score)
        FROM recommendations
    """)

    highest_score = cursor.fetchone()[0]

    if highest_score is None:
        highest_score = 0

    # Top recommended job
    cursor.execute("""
        SELECT
            job_title,
            COUNT(*) AS total
        FROM recommendations
        GROUP BY job_title
        ORDER BY total DESC
        LIMIT 1
    """)

    top_job = cursor.fetchone()

    if top_job:
        top_job_name = top_job["job_title"]
    else:
        top_job_name = "No data"

    # Job recommendation chart
    cursor.execute("""
        SELECT
            job_title,
            COUNT(*) AS total
        FROM recommendations
        GROUP BY job_title
        ORDER BY total DESC
    """)

    job_rows = cursor.fetchall()

    job_labels = []
    job_counts = []

    for row in job_rows:
        job_labels.append(row["job_title"])
        job_counts.append(row["total"])

    # Match score chart
    cursor.execute("""
        SELECT
            job_title,
            ROUND(AVG(match_score), 2) AS average_score
        FROM recommendations
        GROUP BY job_title
        ORDER BY average_score DESC
    """)

    score_rows = cursor.fetchall()

    score_labels = []
    score_values = []

    for row in score_rows:
        score_labels.append(row["job_title"])
        score_values.append(row["average_score"])

    connection.close()

    return {
        "total_candidates": total_candidates,
        "total_recommendations": total_recommendations,
        "average_score": round(average_score, 2),
        "highest_score": round(highest_score, 2),
        "top_job": top_job_name,
        "job_labels": job_labels,
        "job_counts": job_counts,
        "score_labels": score_labels,
        "score_values": score_values
    }
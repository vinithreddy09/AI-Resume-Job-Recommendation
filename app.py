
from flask import Flask, render_template, request
import os

from resume_parser import analyze_resume
from recommender import recommend_jobs
from ats_scorer import calculate_ats_score

from database import (
    initialize_database,
    save_candidate,
    save_recommendations,
    get_candidates,
    get_dashboard_statistics
)

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {"pdf", "docx"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_resume():

    if "resume" not in request.files:
        return "No resume uploaded."

    file = request.files["resume"]

    if file.filename == "":
        return "Please select a resume."

    if not allowed_file(file.filename):
        return "Only PDF and DOCX files are supported."

    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    try:
        file.save(file_path)
    except Exception as error:
        return f"Error while saving resume: {error}"

    try:
        resume_data = analyze_resume(file_path)
    except Exception as error:
        return f"Error while analyzing resume: {error}"

    resume_data["resume_file"] = file.filename

    try:
        ats_score = calculate_ats_score(resume_data)
    except Exception as error:
        return f"Error while calculating ATS score: {error}"

    try:
        recommendations = recommend_jobs(
            resume_data["resume_text"],
            resume_data["skills"],
            resume_data["education"],
            resume_data["experience"]
        )
    except Exception as error:
        return f"Error while generating job recommendations: {error}"

    try:
        candidate_id = save_candidate(resume_data)
        save_recommendations(candidate_id, recommendations)
    except Exception as error:
        return f"Database error: {error}"

    return render_template(
        "result.html",
        filename=file.filename,
        resume=resume_data,
        jobs=recommendations,
        ats=ats_score
    )


@app.route("/dashboard")
def dashboard():

    try:
        statistics = get_dashboard_statistics()
    except Exception as error:
        return f"Dashboard database error: {error}"

    return render_template(
        "dashboard.html",
        statistics=statistics
    )


@app.route("/admin")
def admin():

    try:
        candidates = get_candidates()
    except Exception as error:
        return f"Admin database error: {error}"

    return render_template(
        "admin.html",
        candidates=candidates
    )


# Initialize database when Flask starts.
# This works both locally and with Gunicorn/Render.
initialize_database()


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )


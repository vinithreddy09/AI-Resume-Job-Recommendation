# AI-Based Resume Screening and Job Recommendation System

An AI-powered web application that analyzes resumes, calculates ATS compatibility scores, extracts candidate information and skills, and recommends suitable job opportunities using NLP and machine learning techniques.

## 🚀 Live Demo

**Live Application:**
https://ai-resume-job-recommendation.onrender.com

**GitHub Repository:**
https://github.com/vinithreddy09/AI-Resume-Job-Recommendation

---

## 📌 Project Overview

The **AI-Based Resume Screening and Job Recommendation System** is a web-based application designed to automate the initial resume screening process.

The system accepts resumes in **PDF and DOCX formats**, extracts important candidate information, analyzes technical skills, calculates an **ATS Resume Score**, and recommends relevant job roles based on resume-job similarity and skill matching.

It also provides an **Analytics Dashboard** and **Admin Panel** for viewing candidate and recommendation information.

---

## ✨ Key Features

### 📄 Resume Analysis

* Upload resumes in PDF or DOCX format
* Extract candidate name
* Extract email and phone number
* Detect technical skills
* Extract education information
* Identify experience and project details

### 🎯 ATS Resume Scoring

* Calculates ATS compatibility score out of 100
* Evaluates contact information
* Measures skill coverage
* Checks education details
* Analyzes experience
* Detects important resume sections
* Provides improvement suggestions

### 🤖 AI Job Recommendation

* Uses NLP-based text similarity
* Implements TF-IDF vectorization
* Uses cosine similarity
* Performs skill matching
* Identifies missing skills
* Calculates overall job match percentage
* Provides top job recommendations

### 📊 Analytics Dashboard

* Total candidates
* Total job recommendations
* Average match score
* Highest match score
* Most recommended job
* Job recommendation distribution
* Average job match score

### 👨‍💼 Admin Panel

* View analyzed candidates
* View candidate contact information
* View detected skills
* View education and experience
* Search candidate records

### 💾 Database

* SQLite database
* Stores candidate information
* Stores job recommendations
* Stores match scores
* Stores missing skills
* Maintains screening history

---

## 🛠️ Technologies Used

| Technology   | Purpose                      |
| ------------ | ---------------------------- |
| Python       | Backend programming          |
| Flask        | Web application framework    |
| NLP          | Resume and job text analysis |
| Scikit-learn | TF-IDF and cosine similarity |
| Pandas       | Job dataset processing       |
| SQLite       | Database                     |
| PyPDF2       | PDF resume extraction        |
| python-docx  | DOCX resume extraction       |
| HTML         | Web page structure           |
| CSS          | User interface design        |
| JavaScript   | Frontend functionality       |
| Chart.js     | Dashboard visualizations     |
| Gunicorn     | Production deployment        |
| Render       | Cloud deployment             |

---

## 🧠 AI/NLP Workflow

```text
             Resume Upload
                  │
                  ▼
          PDF / DOCX Parsing
                  │
                  ▼
        Resume Information Extraction
                  │
       ┌──────────┼──────────┐
       ▼          ▼          ▼
     Skills    Education   Experience
       │          │          │
       └──────────┼──────────┘
                  ▼
            ATS Score
                  │
                  ▼
          NLP Text Processing
                  │
                  ▼
         TF-IDF Vectorization
                  │
                  ▼
        Cosine Similarity
                  │
                  ▼
           Skill Matching
                  │
                  ▼
        Job Recommendation
                  │
                  ▼
       Dashboard / Admin Panel
```

---

## 📊 Job Recommendation Process

For every available job, the system calculates:

* NLP similarity score
* Technical skill match score
* Education score
* Experience score
* Overall match score

The system then ranks the jobs and displays the **top 5 recommendations**.

### Example

```text
Resume
   ↓
Python + SQL + Power BI + Excel
   ↓
Skill Matching
   ↓
NLP Similarity
   ↓
Overall Match Score
   ↓
Top Job Recommendations
```

---

## 🎯 ATS Scoring

The ATS module evaluates multiple aspects of a resume:

```text
Contact Information
        +
Technical Skills
        +
Education
        +
Experience
        +
Resume Sections
        +
Formatting & Keywords
        ↓
ATS Score / 100
```

The system also provides suggestions such as:

* Add more relevant technical skills
* Add project details
* Add experience or internship information
* Improve contact information
* Add relevant certifications
* Improve technical keyword coverage

---

## 📂 Project Structure

```text
AI-Resume-Job-Recommendation/
│
├── app.py
├── database.py
├── resume_parser.py
├── nlp_model.py
├── recommender.py
├── ats_scorer.py
├── requirements.txt
├── README.md
│
├── data/
│   └── jobs.csv
│
├── models/
│
├── uploads/
│
├── templates/
│   ├── index.html
│   ├── result.html
│   ├── dashboard.html
│   └── admin.html
│
└── static/
    ├── style.css
    └── script.js
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/vinithreddy09/AI-Resume-Job-Recommendation.git
```

### 2. Open the project

```bash
cd AI-Resume-Job-Recommendation
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```cmd
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

### 7. Open in browser

```text
http://127.0.0.1:5000
```

---

## 🌐 Application Pages

### Resume Analyzer

```text
/
```

Upload a resume and receive:

* Candidate information
* Detected skills
* ATS score
* ATS suggestions
* Job recommendations
* Matched skills
* Missing skills

### Dashboard

```text
/dashboard
```

Provides analytics and visualizations of screening and job recommendation data.

### Admin Panel

```text
/admin
```

Provides access to analyzed candidate records.

---

## ☁️ Deployment

The application is deployed using **Render** with Gunicorn.

```text
GitHub Repository
        ↓
      Render
        ↓
     Gunicorn
        ↓
      Flask
        ↓
  Live Web Application
```

**Live URL:**

https://ai-resume-job-recommendation.onrender.com

---

## 🔐 File & Data Handling

The application supports:

* PDF resumes
* DOCX resumes

Candidate screening information is stored using SQLite.

For the deployed demonstration version, uploaded files and SQLite data use the application's local deployment storage.

---

## 🔮 Future Enhancements

Possible future improvements include:

* Resume ranking for recruiters
* User authentication
* Recruiter login
* Job search API integration
* Advanced NLP models
* BERT-based semantic similarity
* LinkedIn job integration
* Personalized career recommendations
* Resume keyword optimization
* PDF report generation
* Email notifications
* Cloud database integration

---

## 👨‍💻 Developer

**Vinith Reddy**

B.Tech Student | Python | SQL | Data Analytics | AI/ML

### Profiles

**GitHub:**
https://github.com/vinithreddy09

**LinkedIn:**
https://www.linkedin.com/in/vinithreddy-nandhyala09

---

## 📜 License

This project is developed for educational, academic, and portfolio purposes.

---

## ⭐ Project Highlights

```text
✔ AI-Based Resume Screening
✔ ATS Resume Score
✔ NLP Text Similarity
✔ TF-IDF
✔ Cosine Similarity
✔ Skill Matching
✔ Missing Skill Detection
✔ Job Recommendation
✔ SQLite Database
✔ Analytics Dashboard
✔ Admin Panel
✔ Flask Web Application
✔ Cloud Deployment
```

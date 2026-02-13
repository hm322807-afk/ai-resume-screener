# AI Resume Screener

A production-ready AI Resume Screener that matches resumes against job descriptions using NLP techniques (TF-IDF and BERT).

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![AI](https://img.shields.io/badge/AI-BERT%20%26%20TF--IDF-orange)

## 📌 Project Overview
The system allows users to:
1. Upload a resume (PDF/Text).
2. Paste a job description.
3. Get an instant compatibility score based on keyword matching (TF-IDF) and semantic meaning (BERT).
4. See missing and matching skills.

## 🛠️ Tech Stack
- **Backend**: Flask
- **NLP**: TF-IDF (scikit-learn), BERT (sentence-transformers), NLTK, spaCy
- **Frontend**: HTML5, CSS3 (Modern UI)
- **Parsing**: pdfminer.six

## 🚀 How to Run

### 1. Setup Environment
```bash
# Clone or download the project
cd resume_match

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python app.py
```

### 3. Access
Open your browser and go to: `http://127.0.0.1:5000`

## 🧠 How It Works
1. **Extraction**: Text is extracted from the uploaded PDF.
2. **Cleaning**: Text is cleaned (lowercased, stopwords removed, lemmatized).
3. **Matching**:
   - **TF-IDF**: Calculates the frequency of matching keywords.
   - **BERT**: Converts text into vector embeddings to understand context (e.g., "AI" and "Artificial Intelligence" are related).
4. **Scoring**: A weighted average (40% TF-IDF, 60% BERT) gives the final score.

## 📂 Project Structure
```
ai-resume-screener/
├── app.py                 # Main Flask application
├── requirements.txt       # Dependencies
├── static/
│   └── style.css          # Modern CSS styles
├── templates/
│   ├── index.html         # Modern Upload page
│   └── ranking.html       # Responsive Results dashboard
├── utils/
│   ├── basic_nlp.py       # Cleaning & skill extraction
│   ├── matchers.py        # TF-IDF & BERT logic
│   ├── lml_feedback.py    # AI feedback generation
│   └── parsers.py         # PDF parsing
└── data/                  # Internal uploads folder
```

## 📸 Screenshots
(Add screenshots here after running the app)

## ⚠️ Notes
- The first run might be slightly slower as it downloads the BERT model (~100MB).
- Ensure you have a stable internet connection for the first run.

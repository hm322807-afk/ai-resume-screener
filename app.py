import os
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from utils.parsers import extract_text_from_pdf
from utils.basic_nlp import clean_text, extract_skills_from_text, COMMON_SKILLS
from utils.matchers import calculate_tfidf_similarity, calculate_bert_similarity, calculate_category_scores
from utils.llm_feedback import generate_feedback

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Change this for production
app.config['UPLOAD_FOLDER'] = 'data'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload

ALLOWED_EXTENSIONS = {'pdf', 'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'resume' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    files = request.files.getlist('resume')
    job_desc = request.form['job_desc']
    
    if not files or files[0].filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    results = []
    cleaned_job_desc = clean_text(job_desc)
    job_skills = set(extract_skills_from_text(cleaned_job_desc))
    
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # 1. Parsing
            if filename.endswith('.pdf'):
                resume_text = extract_text_from_pdf(filepath)
            else:
                resume_text = file.read().decode('utf-8')
            
            if not resume_text:
                continue

            # 2. Cleaning
            cleaned_resume = clean_text(resume_text)
            
            # 3. Skill Extraction
            resume_skills = set(extract_skills_from_text(cleaned_resume))
            missing_skills = list(job_skills - resume_skills)
            matching_skills = list(resume_skills.intersection(job_skills))
            
            # 4. Matching
            tfidf_score = calculate_tfidf_similarity(cleaned_resume, cleaned_job_desc)
            bert_score = calculate_bert_similarity(cleaned_resume, cleaned_job_desc)
            
            # Weighted average (40% TF-IDF, 60% BERT)
            final_score = (tfidf_score * 0.4) + (bert_score * 0.6)
            final_percentage = round(final_score * 100, 2)
            
            # 5. Advanced Analysis (V3)
            category_scores = calculate_category_scores(cleaned_resume, cleaned_job_desc)
            ai_feedback = generate_feedback(filename, final_percentage, matching_skills, missing_skills, resume_text)

             # Recommendation
            if final_percentage >= 75:
                recommendation = "Highly Suitable"
                rec_class = "success"
            elif final_percentage >= 50:
                recommendation = "Potentially Suitable"
                rec_class = "warning"
            else:
                recommendation = "Not Suitable"
                rec_class = "danger"

            results.append({
                'filename': filename,
                'tfidf_score': round(tfidf_score * 100, 2),
                'bert_score': round(bert_score * 100, 2),
                'final_score': final_percentage,
                'category_scores': category_scores,
                'ai_feedback': ai_feedback,
                'recommendation': recommendation,
                'rec_class': rec_class,
                'missing_skills': missing_skills,
                'matching_skills': matching_skills,
                'summary': resume_text[:200] + "..."
            })
    
    # Sort results by final score descending
    results.sort(key=lambda x: x['final_score'], reverse=True)
    
    return render_template('ranking.html', results=results, job_desc=job_desc[:200]+"...")

@app.route('/export', methods=['POST'])
def export_csv():
    # In a real app, you'd generate this dynamically from the current session or DB
    # For this demo, we can't easily pass data between requests without a DB
    # So we'll just redirect for now or implement client-side export in JS
    return redirect(url_for('index'))

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)

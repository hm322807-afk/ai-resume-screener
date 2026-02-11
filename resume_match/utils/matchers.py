from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, util
import numpy as np

# Load BERT model (will download on first run)
bert_model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_tfidf_similarity(text1, text2):
    """
    Calculates cosine similarity using TF-IDF vectors.
    """
    if not text1 or not text2:
        return 0.0
        
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return float(similarity)

def calculate_bert_similarity(text1, text2):
    """
    Calculates semantic similarity using BERT embeddings.
    """
    if not text1 or not text2:
        return 0.0

    # Encode texts to get embeddings
    embedding1 = bert_model.encode(text1, convert_to_tensor=True)
    embedding2 = bert_model.encode(text2, convert_to_tensor=True)

    # Compute cosine similarity
    similarity = util.pytorch_cos_sim(embedding1, embedding2)
    return float(similarity.item())

# Define lists for category scoring
SOFT_SKILLS = {
    'communication', 'teamwork', 'leadership', 'adaptability', 'creativity', 
    'problem solving', 'time management', 'work ethic', 'collaboration', 'critical thinking'
}

EXPERIENCE_KEYWORDS = {
    'managed', 'led', 'delivered', 'deployed', 'designed', 'architected', 
    'supervised', 'coordinated', 'launched', 'scale', 'production', 'years', 'senior', 'junior'
}

def calculate_category_scores(resume_text, job_desc_text):
    """
    Calculates scores (0-100) for specific categories: Technical, Soft Skills, Experience.
    Returns a dictionary of scores.
    """
    resume_words = set(resume_text.lower().split())
    job_words = set(job_desc_text.lower().split())
    
    # Helper to calculate overlap percentage
    def get_overlap_score(keywords, source_text_set, target_text_set):
        # Find relevant keywords that appear in the Job Description
        target_relevant = keywords.intersection(target_text_set)
        if not target_relevant:
            return 0 # Job doesn't ask for these, so score is N/A (or 0)
        
        # Check how many of those the candidate has
        match = target_relevant.intersection(source_text_set)
        if not match:
             return 0
        return round((len(match) / len(target_relevant)) * 100, 2)

    # 1. Soft Skills Score
    soft_score = get_overlap_score(SOFT_SKILLS, resume_words, job_words)
    
    # 2. Experience Score (Action Verbs)
    exp_score = get_overlap_score(EXPERIENCE_KEYWORDS, resume_words, job_words)
    
    # 3. Technical Score (Heuristic)
    # We'll use the ratio of *total* unique matching words relative to job description length 
    # but we exclude common stopwords (implied by just splitting)
    # Ideally we'd use the extracted skills list, but for this function we use a simple set overlap
    common_matches = resume_words.intersection(job_words)
    # Naive metric: (matches / total_unique_job_words) * 100 * booster
    tech_score = round((len(common_matches) / len(job_words)) * 100, 2)
    
    return {
        'Technical': min(tech_score + 20, 100), # Boost slightly as direct match is harsh
        'Soft Skills': soft_score,
        'Experience': exp_score
    }

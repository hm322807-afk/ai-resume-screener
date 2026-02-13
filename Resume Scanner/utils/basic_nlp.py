import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Ensure NLTK data is downloaded
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    """
    Cleans text: lowercase, remove special characters, simple lemmatization.
    """
    # Lowercase
    text = text.lower()
    
    # Remove special characters and numbers
    text = re.sub(r'[^a-z\s]', ' ', text)
    
    # Tokenize (simple split for speed, or use nltk.word_tokenize)
    tokens = text.split()
    
    # Remove stopwords and lemmatize
    cleaned_tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    
    return " ".join(cleaned_tokens)

# Basic list of common technical skills for extraction
COMMON_SKILLS = {
    'python', 'java', 'c++', 'javascript', 'html', 'css', 'react', 'node', 'flask', 'django',
    'sql', 'nosql', 'mongodb', 'postgresql', 'aws', 'azure', 'docker', 'kubernetes', 'git',
    'machine learning', 'deep learning', 'nlp', 'tensorflow', 'pytorch', 'scikit-learn',
    'pandas', 'numpy', 'data analysis', 'statistics', 'communication', 'leadership', 'agile'
}

def extract_skills_from_text(text):
    """
    Extracts skills from text based on a predefined list.
    """
    text = text.lower()
    found_skills = set()
    for skill in COMMON_SKILLS:
        # Simple string matching, improving with regex for word boundaries
        if re.search(r'\b' + re.escape(skill) + r'\b', text):
            found_skills.add(skill)
    return list(found_skills)

import unittest
from utils.basic_nlp import clean_text, extract_skills_from_text
from utils.matchers import calculate_tfidf_similarity, calculate_bert_similarity

class TestResumeMatcher(unittest.TestCase):
    def setUp(self):
        self.resume = "I am a skilled software engineer with experience in Python, Flask, and SQL."
        self.job = "We are looking for a software engineer who knows Python, Flask, and SQL."
        self.cleaned_resume = clean_text(self.resume)
        self.cleaned_job = clean_text(self.job)

    def test_cleaning(self):
        print(f"Original: {self.resume}")
        print(f"Cleaned: {self.cleaned_resume}")
        self.assertTrue(len(self.cleaned_resume) > 0)

    def test_skill_extraction(self):
        skills = extract_skills_from_text(self.resume)
        print(f"Extracted Skills: {skills}")
        self.assertIn('python', skills)
        self.assertIn('flask', skills)
        self.assertIn('sql', skills)

    def test_tfidf_matcher(self):
        score = calculate_tfidf_similarity(self.cleaned_resume, self.cleaned_job)
        print(f"TF-IDF Score: {score}")
        self.assertTrue(0 <= score <= 1)

    def test_bert_matcher(self):
        # This might take a moment to download the model on first run
        print("Testing BERT matcher (may download model)...")
        score = calculate_bert_similarity(self.cleaned_resume, self.cleaned_job)
        print(f"BERT Score: {score}")
        self.assertTrue(0 <= score <= 1)

if __name__ == '__main__':
    unittest.main()

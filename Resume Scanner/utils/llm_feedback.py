import os

# Placeholder for a real LLM client (e.g., OpenAI, Google Gemini)
# from google.generativeai import ...

def generate_feedback(candidate_name, match_score, matching_skills, missing_skills, resume_text):
    """
    Generates a qualitative feedback summary. 
    Uses a rule-based template if no LLM API key is explicitly configured.
    """
    
    # Logic for a "rule-based" smart summary (simulating an LLM)
    
    # 1. Analyze Fit
    if match_score >= 75:
        fit_level = "strong"
        action = "Highly recommended for an interview."
    elif match_score >= 50:
        fit_level = "moderate"
        action = "Worth considering, but may require training."
    else:
        fit_level = "low"
        action = "Likely not a good fit for this specific role."

    # 2. Analyze Skills
    strong_points = ", ".join(list(matching_skills)[:3]) if matching_skills else "general adaptability"
    weak_points = ", ".join(list(missing_skills)[:3]) if missing_skills else "specific domain expertise"

    # 3. Analyze Experience (Simple keyword heuristic)
    experience_keywords = ['senior', 'lead', 'manager', 'years', 'architect']
    experience_level = "Senior/Lead" if any(k in resume_text.lower() for k in experience_keywords) else "Junior/Mid-level"

    # 4. Construct the Narrative
    feedback_text = (
        f"The candidate, {candidate_name}, shows a {fit_level} alignment ({match_score}%) with the job requirements. "
        f"They demonstrate competence in {strong_points}, which are key for this position. "
        f"However, there are gaps in {weak_points} that should be probed during screening. "
        f"Based on the text, they appear to be a {experience_level} candidate. {action}"
    )

    return feedback_text

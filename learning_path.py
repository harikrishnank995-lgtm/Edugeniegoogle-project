from ai_client import generate_text


def recommend_learning_path(goal: str) -> str:
    return generate_text("Create a beginner-friendly learning path for this subject or goal. Organize it into ordered stages; for each stage include what to learn, one practice activity, and a simple way to check understanding. End with a realistic next step.\n\nStudent goal:\n" + goal)

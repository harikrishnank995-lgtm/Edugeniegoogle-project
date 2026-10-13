import json
from ai_client import generate_text


def create_quiz(topic: str):
    prompt = ("Create exactly 3 multiple-choice questions for a student based on the topic below. "
              "Return ONLY valid JSON in this shape: {\"questions\":[{\"question\":\"...\",\"options\":[\"A. ...\",\"B. ...\",\"C. ...\",\"D. ...\"],\"answer\":\"A. ...\",\"explanation\":\"...\"}]}. "
              "Each question must have exactly four options and one correct answer.\n\nTopic:\n" + topic)
    raw = generate_text(prompt, json_mode=True)
    try:
        data = json.loads(raw)
        questions = data.get("questions", [])
        if len(questions) != 3 or any(len(q.get("options", [])) != 4 for q in questions):
            raise ValueError("Quiz format did not contain 3 questions with 4 options each.")
        return data
    except (json.JSONDecodeError, AttributeError, TypeError) as exc:
        raise RuntimeError("Could not read the quiz response. Please click Generate Quiz again.") from exc

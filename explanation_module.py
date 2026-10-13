from ai_client import generate_text


def explain_concept(concept: str) -> str:
    prompt = ("Explain the topic to a beginner in simple, student-friendly language. "
              "Use: 1) short definition, 2) how it works, 3) a practical example, "
              "4) a brief recap. Avoid unnecessary jargon.\n\nTopic or text:\n" + concept)
    return generate_text(prompt)

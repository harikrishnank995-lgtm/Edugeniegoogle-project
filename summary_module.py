from ai_client import generate_text


def summarize_text(text: str) -> str:
    return generate_text("Summarize the following material for a student. Give the main idea, key points, and important terms. Keep it concise and do not add facts that are not in the source.\n\nMaterial:\n" + text)

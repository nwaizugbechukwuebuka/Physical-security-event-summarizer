import re

def clean_text(text: str) -> str:
    # Remove unwanted characters and all punctuation, normalize whitespace
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

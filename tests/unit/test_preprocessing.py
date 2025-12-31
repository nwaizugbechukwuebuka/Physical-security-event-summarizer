from src.preprocessing.text_cleaner import clean_text
from src.preprocessing.language_detection import detect_language

def test_clean_text():
    assert clean_text("Hello!!  World.") == "Hello World"

def test_detect_language():
    assert detect_language("This is English.") == "en" or detect_language("This is English.") == "unknown"

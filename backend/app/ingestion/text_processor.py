import re

def clean_text(text):
    try:
        if not text:
            return None

        text = re.sub(r'\n{3,}', '\n\n', text)
        text = re.sub(r'[ \t]+', ' ', text)

        return text.strip()

    except Exception as e:
        print(f"Error cleaning text: {e}")
        return None
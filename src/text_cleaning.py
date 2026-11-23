
import re


def clean_text(text: str) -> str:
    """
    Clean common OCR formatting issues while preserving the text's meaning.

    Current operations:
    - Remove unnecessary spaces before punctuation.
    - Remove unnecessary spaces after opening brackets.
    - Remove unnecessary spaces before closing brackets.
    - Collapse repeated spaces and tabs.
    - Preserve paragraph and line breaks.
    """

    if not isinstance(text, str):
        raise TypeError("clean_text() expects a string.")

    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    cleaned_lines = []

    for line in text.split("\n"):
        # Remove spaces before punctuation
        line = re.sub(r"[ \t]+([,.;:!?])", r"\1", line)

        # Remove spaces immediately after opening brackets
        line = re.sub(r"([(\[{])[ \t]+", r"\1", line)

        # Remove spaces immediately before closing brackets
        line = re.sub(r"[ \t]+([)\]}])", r"\1", line)

        # Collapse repeated spaces and tabs
        line = re.sub(r"[ \t]+", " ", line)

        # Remove leading and trailing spaces
        line = line.strip()

        cleaned_lines.append(line)

    return "\n".join(cleaned_lines)

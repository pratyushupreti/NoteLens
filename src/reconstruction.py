
from statistics import median


def reconstruct_paragraphs(lines):
    if not lines:
        return []

    # Sort lines from top to bottom
    lines = sorted(lines, key=lambda line: line["y"])

    # Calculate median text height
    heights = [line["height"] for line in lines]
    median_height = median(heights)

    # Calculate paragraph separation threshold
    gap_threshold = median_height * 1.25

    paragraphs = []
    current_paragraph = [lines[0]]

    for previous, current in zip(lines, lines[1:]):
        vertical_gap = (
            current["y"] -
            (previous["y"] + previous["height"])
        )

        is_new_paragraph = vertical_gap > gap_threshold

        if is_new_paragraph:
            paragraphs.append(current_paragraph)
            current_paragraph = [current]
        else:
            current_paragraph.append(current)

    paragraphs.append(current_paragraph)

    # Convert groups into text
    reconstructed = []

    for paragraph in paragraphs:
        text = " ".join(
            line["text"].strip()
            for line in paragraph
        )

        reconstructed.append(text)

    return reconstructed

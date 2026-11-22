
from pathlib import Path

from reconstruction import reconstruct_paragraphs
from segmentation import segment_lines
from ocr import recognize_handwriting


def process_document(image_path):
    image_path = Path(image_path)

    if not image_path.exists():
        raise FileNotFoundError(
            f"Document not found: {image_path}"
        )

    line_images = segment_lines(str(image_path))

    if not line_images:
        print("No text lines detected.")
        return

    recognized_lines = []

    for line in line_images:
        text = recognize_handwriting(line["path"])

        recognized_lines.append({
            "text": text,
            "x": line["x"],
            "y": line["y"],
            "width": line["width"],
            "height": line["height"]
        })

    paragraphs = reconstruct_paragraphs(recognized_lines)

    output_dir = Path("data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "recognized.txt"

    document_text = "\n\n".join(paragraphs)

    output_file.write_text(
        document_text,
        encoding="utf-8"
    )

    print(f"Document successfully processed: {output_file}")


if __name__ == "__main__":
    process_document("data/input/test_line.png")

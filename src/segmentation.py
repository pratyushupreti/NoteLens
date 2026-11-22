
import cv2
import numpy as np
from pathlib import Path


def segment_lines(
    image_path,
    output_dir="data/processed/lines"
):
    # 1. Load image
    image = cv2.imread(str(image_path))

    if image is None:
        raise FileNotFoundError(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 2. Adaptive thresholding
    binary = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        31,
        15
    )

    # 3. Calculate horizontal projection
    projection = np.sum(binary > 0, axis=1)

    # 4. Smooth projection
    kernel = np.ones(5) / 5

    smoothed = np.convolve(
        projection,
        kernel,
        mode="same"
    )

    # 5. Dynamic threshold
    row_threshold = max(
        8,
        int(smoothed.max() * 0.12)
    )

    active_rows = np.where(
        smoothed > row_threshold
    )[0]

    if len(active_rows) == 0:
        return []

    # 6. Group active rows
    groups = []

    start = active_rows[0]
    previous = active_rows[0]

    merge_gap = 2

    for row in active_rows[1:]:
        if row - previous > merge_gap:
            groups.append((start, previous))
            start = row

        previous = row

    groups.append((start, previous))

    # 7. Remove very small regions
    min_height = 8

    groups = [
        (y1, y2)
        for y1, y2 in groups
        if y2 - y1 >= min_height
    ]

    # 8. Prepare output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Remove old crops to avoid confusion
    for old_file in output_path.glob("line_*.png"):
        old_file.unlink()

    # 9. Crop individual lines
    detected_lines = []
    padding = 8

    for index, (y1, y2) in enumerate(groups):

        text_y1 = y1
        text_y2 = y2

        crop_y1 = max(0, text_y1 - padding)
        crop_y2 = min(
            image.shape[0],
            text_y2 + padding + 1
        )

        region = binary[crop_y1:crop_y2, :]
        points = cv2.findNonZero(region)

        if points is None:
            continue

        x, _, w, _ = cv2.boundingRect(points)

        text_x = x
        text_width = w

        crop_x1 = max(0, x - padding)
        crop_x2 = min(
            image.shape[1],
            x + w + padding
        )

        cropped_line = image[
            crop_y1:crop_y2,
            crop_x1:crop_x2
        ]

        filename = output_path / f"line_{index + 1:02d}.png"

        cv2.imwrite(str(filename), cropped_line)

        detected_lines.append({
            "path": str(filename),
            "x": text_x,
            "y": text_y1,
            "width": text_width,
            "height": text_y2 - text_y1 + 1
        })

    return detected_lines

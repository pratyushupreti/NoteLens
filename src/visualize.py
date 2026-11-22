
import cv2
import matplotlib.pyplot as plt

from segmentation import segment_lines


def visualize_bounding_boxes(image_path):

    image = cv2.imread(str(image_path))

    if image is None:
        raise FileNotFoundError(
            f"Could not load image: {image_path}"
        )

    lines = segment_lines(str(image_path))

    for index, line in enumerate(lines, 1):

        x = line["x"]
        y = line["y"]
        width = line["width"]
        height = line["height"]

        x2 = x + width
        y2 = y + height

        cv2.rectangle(
            image,
            (x, y),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            image,
            str(index),
            (x, max(y - 5, 15)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 255),
            2
        )

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(14, 10))
    plt.imshow(image)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

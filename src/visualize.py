
import cv2
import matplotlib.pyplot as plt
from pathlib import Path

folder = Path("data/processed/lines")

files = sorted(folder.glob("line_*.png"))

if not files:
    raise FileNotFoundError("No segmented lines found!")

fig, axes = plt.subplots(
    len(files), 1,
    figsize=(12, 3 * len(files))
)

if len(files) == 1:
    axes = [axes]

for ax, file in zip(axes, files):

    image = cv2.imread(str(file))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    ax.imshow(image)
    ax.set_title(file.name)
    ax.axis("off")

plt.tight_layout()
plt.show()

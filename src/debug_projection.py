
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load original image
image = cv2.imread("data/input/test_line.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding
binary = cv2.adaptiveThreshold(
    gray,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV,
    31,
    15
)

# Calculate horizontal projection
projection = np.sum(binary > 0, axis=1)

# Smooth the projection to reduce small fluctuations
kernel = np.ones(5) / 5
smoothed = np.convolve(projection, kernel, mode="same")

# Display results
fig, axes = plt.subplots(1, 2, figsize=(14, 7))

axes[0].imshow(binary, cmap="gray")
axes[0].set_title("Binary Image")
axes[0].axis("off")

axes[1].plot(smoothed, np.arange(len(smoothed)))
axes[1].invert_yaxis()
axes[1].set_title("Horizontal Projection Profile")
axes[1].set_xlabel("Ink Pixel Count")
axes[1].set_ylabel("Image Row")
axes[1].grid(True)

plt.tight_layout()
plt.show()

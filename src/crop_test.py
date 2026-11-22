from PIL import Image

# Load original notebook image
image = Image.open("data/input/test_line.png")

# Crop one handwritten line
cropped = image.crop((30, 400, 280, 465))

# Save the cropped line
cropped.save("data/input/test_crop.png")

print("Crop saved successfully!")

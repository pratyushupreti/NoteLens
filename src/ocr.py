
import torch
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image

MODEL_NAME = "microsoft/trocr-base-handwritten"

# Select GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"

print(f"Using device: {device}")

# Load processor and pretrained model
processor = TrOCRProcessor.from_pretrained(MODEL_NAME)

model = VisionEncoderDecoderModel.from_pretrained(
    MODEL_NAME
)

model.to(device)
model.eval()

def recognize_handwriting(image_path):

    # Load image
    image = Image.open(image_path).convert("RGB")

    # Convert image into model inputs
    pixel_values = processor(
        images=image,
        return_tensors="pt"
    ).pixel_values.to(device)

    # Generate predicted text
    with torch.no_grad():
        generated_ids = model.generate(
            pixel_values,
            max_new_tokens=128,
            num_beams=4
        )

    # Decode predictions
    text = processor.batch_decode(
        generated_ids,
        skip_special_tokens=True
    )[0]

    return text


if __name__ == "__main__":

    image_path = "data/input/test_crop.png"

    result = recognize_handwriting(image_path)

    print("\nRecognized text:")
    print(result)

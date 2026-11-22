
# NoteLens

**AI-powered handwritten document digitization using computer vision and transformer-based handwriting recognition.**

NoteLens is a Python-based project that converts handwritten documents into digital text. It uses OpenCV for image preprocessing and line segmentation, followed by Microsoft's TrOCR model to recognize handwritten text.

The goal is to build a complete document digitization pipeline that can process handwritten pages and produce machine-readable text.

---

## Features

### Implemented

- Image preprocessing using OpenCV.
- Grayscale conversion and image thresholding.
- Noise reduction and projection-based line detection.
- Automatic segmentation of handwritten documents into individual lines.
- Visualization and saving of segmented line images.
- Handwriting recognition using Microsoft's TrOCR model.
- Integrated pipeline for processing a document and recognizing its text.
- Saving recognized text to an output file.

### In Development

- Improved text reconstruction and paragraph formatting.
- Recognition accuracy evaluation.
- Better handling of different handwriting styles and document layouts.
- More robust document preprocessing.

---

## How It Works

NoteLens currently follows this processing pipeline:

```text
Handwritten Document
        |
        v
Image Preprocessing
        |
        v
Grayscale Conversion
        |
        v
Thresholding & Noise Reduction
        |
        v
Horizontal Projection
        |
        v
Handwritten Line Detection
        |
        v
Line Segmentation
        |
        v
TrOCR Handwriting Recognition
        |
        v
Recognized Text
        |
        v
Output File
```

### 1. Image Preprocessing

The input document is processed using OpenCV to prepare it for segmentation.

### 2. Line Detection and Segmentation

Horizontal projection is used to identify handwritten text regions. The document is divided into individual line images, which are saved for further processing.

### 3. Handwriting Recognition

Each segmented line is passed to Microsoft's TrOCR model:

`microsoft/trocr-base-handwritten`

The model generates a text prediction for each line.

### 4. Text Output

Recognized lines are combined in reading order and saved to:

`data/processed/recognized.txt`

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OpenCV | Image processing and segmentation |
| NumPy | Numerical operations |
| PyTorch | Deep learning framework |
| Hugging Face Transformers | TrOCR model integration |
| Pillow | Image handling |
| TrOCR | Handwriting recognition |

---

## Project Structure

```text
NoteLens/
│
├── data/
│   └── input/
│
├── src/
│   ├── ocr.py
│   ├── pipeline.py
│   ├── reconstruction.py
│   ├── segmentation.py
│   └── visualize.py
│
├── requirements.txt
├── README.md
└── .gitignore

**Note:** The `data/processed/` directory is generated automatically when the pipeline runs. It stores segmented line images, recognized text, and reconstructed document output. This directory is excluded from version control.

```

---

## Getting Started

### Prerequisites

- Python 3.10 or later
- pip
- Git

A CUDA-compatible GPU is optional. The pipeline can also run using a CPU, although recognition may be slower.

### 1. Clone the Repository

```bash
git clone https://github.com/pratyushupreti/NoteLens.git
cd NoteLens
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Pipeline

```bash
python src/pipeline.py
```

The first execution may take longer because the pretrained TrOCR model needs to be downloaded.

---

## Current Progress

### Milestone 1 — Core Document Processing

**Completed work**

- Implemented image preprocessing.
- Implemented projection-based handwritten line detection.
- Developed automatic line segmentation.
- Integrated TrOCR handwriting recognition.
- Connected segmentation and recognition into a processing pipeline.
- Tested the pipeline on a sample handwritten document.

**Latest test result:**

- 9 handwritten lines detected.
- All 9 segmented lines passed through the recognition stage.
- Recognized text reached the output-saving stage.

### Milestone 2 — Recognition Quality and Text Reconstruction

- [ ] Evaluate OCR output against manually transcribed text.
- [ ] Calculate Character Error Rate (CER).
- [ ] Calculate Word Error Rate (WER).
- [ ] Improve recognition quality.
- [ ] Reconstruct paragraphs and document structure.
- [ ] Handle headings, signatures, and other layout elements.

### Milestone 3 — Robustness and Testing

- [ ] Test on multiple handwritten documents.
- [ ] Handle different handwriting styles.
- [ ] Improve performance on noisy and low-quality images.
- [ ] Add automated tests.
- [ ] Improve error handling and logging.

### Milestone 4 — Application Development

- [ ] Build a user-friendly interface.
- [ ] Support document uploads.
- [ ] Display extracted text.
- [ ] Allow users to download recognized text.
- [ ] Add document history and processing status.

### Milestone 5 — Deployment

- [ ] Build an API for document processing.
- [ ] Containerize the application.
- [ ] Deploy the application.
- [ ] Add performance monitoring.

---

## Future Improvements

Potential future directions include:

- Better document layout analysis.
- Improved paragraph and formatting reconstruction.
- Support for multiple languages.
- Batch document processing.
- Confidence scores for recognized text.
- A scalable document-processing API.

---

## Contributing

Contributions, suggestions, and feedback are welcome.

If you find a bug or have an idea for improvement, feel free to open an issue or submit a pull request.

---

## Author

**Pratyush Upreti**

GitHub: [@pratyushupreti](https://github.com/pratyushupreti)

---

*NoteLens is an ongoing project focused on exploring computer vision, deep learning, and applied AI through handwritten document digitization.*

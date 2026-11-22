
# NoteLens

**An intelligent handwritten document digitization system using computer vision and deep learning.**

NoteLens is an experimental document-processing project designed to convert handwritten documents into machine-readable text. It combines traditional computer vision techniques with transformer-based handwriting recognition to process handwritten document images.

The project focuses on image preprocessing, text-line detection, line segmentation, and handwriting recognition.

---

## Overview

Extracting text from handwritten documents is challenging due to variations in handwriting styles, inconsistent spacing, image noise, and document layouts.

NoteLens aims to address these challenges through a modular processing pipeline that prepares document images, identifies individual handwritten text lines, and applies deep learning-based handwriting recognition.

## Features

### Implemented

- **Image preprocessing:** Prepare document images for further processing.
- **Grayscale conversion:** Simplify image representation.
- **Image thresholding:** Separate foreground text from the background.
- **Noise reduction:** Improve image quality for segmentation.
- **Horizontal projection analysis:** Identify handwritten text-line boundaries.
- **Line segmentation:** Extract individual handwritten lines as separate images.
- **Visualization:** Inspect intermediate image-processing results.

### In Development

- **Handwriting recognition:** Integrate Microsoft's TrOCR transformer model.
- **Text reconstruction:** Combine recognized lines into complete documents.
- **Recognition evaluation:** Evaluate OCR performance using standard metrics.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| OpenCV | Image processing and computer vision |
| NumPy | Numerical computation |
| PyTorch | Deep learning framework |
| Hugging Face Transformers | TrOCR model integration |
| Pillow | Image handling |

## Project Architecture

NoteLens follows a document-processing pipeline:

```text
Handwritten Document
        |
        v
Image Preprocessing
        |
        v
Noise Reduction
        |
        v
Image Thresholding
        |
        v
Horizontal Projection
        |
        v
Text Line Detection
        |
        v
Line Segmentation
        |
        v
Handwriting Recognition
        |
        v
Structured Text Output
```

## Project Structure

```text
NoteLens/
│
├── data/
│   ├── raw/
│   └── processed/
│       └── lines/
│
├── src/
│   ├── crop_test.py
│   ├── debug_projection.py
│   ├── ocr.py
│   ├── segmentation.py
│   └── visualize.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/pratyushupreti/NoteLens.git
cd NoteLens
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

On Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

For GPU-specific PyTorch installation, refer to:

https://pytorch.org/get-started/locally/

## Usage

The project is currently under active development.

The main processing workflow involves:

1. Providing a handwritten document image.
2. Preprocessing the image.
3. Applying horizontal projection analysis.
4. Detecting handwritten text lines.
5. Extracting individual lines into separate images.
6. Passing segmented lines to the handwriting recognition model as recognition integration is completed.

The source files are currently organized as individual Python scripts. Execution commands and a unified entry point will be documented as the pipeline is consolidated.

## Current Progress

| Component | Status |
|---|---|
| Image loading | Implemented |
| Image preprocessing | Implemented |
| Noise reduction | Implemented |
| Horizontal projection analysis | Implemented |
| Text-line detection | Implemented |
| Line segmentation | Implemented |
| Visualization utilities | Implemented |
| TrOCR integration | In development |
| Full-document text reconstruction | Planned |
| Automated testing | Planned |
| OCR performance evaluation | Planned |

### Initial Segmentation Results

The initial segmentation test successfully detected **9 handwritten text lines** from a sample document.

Each detected line was extracted and saved as an individual image.

This demonstrates the functionality of the initial line-segmentation pipeline. It is not a general accuracy benchmark.

## Roadmap

- [x] Implement image preprocessing.
- [x] Implement horizontal projection-based line detection.
- [x] Extract individual handwritten text lines.
- [x] Visualize segmentation results.
- [ ] Complete TrOCR integration.
- [ ] Implement full-document text reconstruction.
- [ ] Add automated unit tests.
- [ ] Evaluate recognition using Character Error Rate (CER) and Word Error Rate (WER).
- [ ] Improve segmentation for complex handwriting layouts.
- [ ] Build a unified document-processing pipeline.
- [ ] Develop a user-friendly interface.

## Future Improvements

Potential improvements include:

- Handling skewed and rotated documents.
- Supporting different handwriting styles.
- Improving segmentation for overlapping text lines.
- Supporting multi-page document processing.
- Comparing different handwriting recognition models.
- Adding confidence scores to recognized text.
- Building an interactive document digitization interface.

## Contributing

Contributions, suggestions, and bug reports are welcome.

If you encounter an issue or have an improvement idea, feel free to open a GitHub issue.

## Author

**Pratyush Upreti**

GitHub: [@pratyushupreti](https://github.com/pratyushupreti)

Project: [NoteLens](https://github.com/pratyushupreti/NoteLens)

---

**Note:** NoteLens is an experimental project under active development. Features, architecture, and implementation details may evolve as development progresses.

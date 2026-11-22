# NoteLens — AI-Powered Handwritten Notes Digitizer

**Turning handwritten notes into structured, searchable digital documents using Computer Vision and Deep Learning.**

NoteLens is an AI-powered document digitization project that aims to transform handwritten notes into machine-readable digital text. It combines computer vision techniques with transformer-based handwriting recognition to process handwritten documents at the page level.

The project currently focuses on building a reliable handwriting recognition pipeline, with intelligent document understanding and AI-powered note processing planned for future development.

---

## Overview

Digitizing handwritten notes is more complicated than simply recognizing individual characters. A complete system needs to identify text regions, separate individual lines, recognize handwriting, and reconstruct the original document in the correct reading order.

NoteLens approaches this problem through a modular pipeline combining:

- **Computer Vision:** Image preprocessing and handwritten line segmentation.
- **Deep Learning:** Transformer-based handwriting recognition.
- **Document Processing:** Combining recognized text into readable digital documents.
- **Applied AI:** Future capabilities for summarization, information extraction, and semantic search.

## Core Features

### Implemented

- [x] Handwriting recognition using pretrained TrOCR.
- [x] Image loading and preprocessing using OpenCV.
- [x] Adaptive image thresholding.
- [x] Horizontal projection profile analysis.
- [x] Projection smoothing for improved line detection.
- [x] Automatic handwritten line segmentation.
- [x] Individual text-line extraction and cropping.
- [x] GPU-compatible inference using PyTorch.

### In Development

- [ ] Complete page-to-text pipeline integration and testing.
- [ ] OCR accuracy evaluation using CER and WER.
- [ ] Improved segmentation across different handwriting styles.
- [ ] Document reading-order reconstruction.
- [ ] Paragraph and formatting reconstruction.

### Planned Features

- [ ] AI-powered note summarization.
- [ ] Automatic heading and bullet-point detection.
- [ ] Important concept extraction.
- [ ] Automatic flashcard generation.
- [ ] Semantic search across digitized notes.
- [ ] PDF and DOCX export.
- [ ] Web-based document upload and management interface.

---

## System Architecture

NoteLens follows a modular document-processing architecture.

```text
                 INPUT
                   |
                   v
          Handwritten Document
                   |
                   v
          IMAGE PREPROCESSING
             (OpenCV)
                   |
                   v
          IMAGE BINARIZATION
        Adaptive Thresholding
                   |
                   v
          LINE SEGMENTATION
        Horizontal Projection
                   |
                   v
          INDIVIDUAL LINE CROPS
                   |
                   v
        HANDWRITING RECOGNITION
                TrOCR
                   |
                   v
           TEXT RECONSTRUCTION
                   |
                   v
            DIGITAL DOCUMENT
```

### Pipeline Components

**1. Image Preprocessing**

OpenCV is used to load handwritten document images and convert them into representations suitable for further processing.

Current techniques include:
- Grayscale conversion.
- Adaptive thresholding.
- Foreground and background separation.

**2. Handwritten Line Segmentation**

The segmentation module identifies individual handwritten text lines using horizontal projection profiles.

The current implementation uses:
- Horizontal pixel projection.
- Projection smoothing.
- Dynamic thresholding.
- Row grouping.
- Bounding-box extraction.

This allows the system to extract individual lines from a handwritten page before recognition.

**3. Handwriting Recognition**

NoteLens uses Microsoft's pretrained TrOCR model:

`microsoft/trocr-base-handwritten`

TrOCR is a transformer-based encoder-decoder model designed for handwritten text recognition.

The model processes individual line images and generates corresponding text predictions.

**4. Text Reconstruction**

Recognized text from individual lines is combined in their original detected order to produce a digital text document.

This component is currently undergoing integration and testing.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| PyTorch | Deep learning framework |
| Hugging Face Transformers | Model integration |
| TrOCR | Handwriting recognition |
| OpenCV | Image processing |
| NumPy | Numerical computation |
| Pillow | Image handling |
| Matplotlib | Image and projection visualization |

---

## Project Structure

```text
NoteLens/
│
├── data/
│   ├── input/
│   │
│   └── processed/
│       └── lines/
│
├── docs/
│   └── experiments.md
│
├── notebooks/
│
├── src/
│   ├── ocr.py
│   ├── segmentation.py
│   ├── visualize.py
│   ├── debug_projection.py
│   └── pipeline.py
│
├── tests/
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Installation and Setup

### Prerequisites

- Python 3.11
- Git
- NVIDIA GPU (recommended for GPU acceleration)
- CUDA-compatible PyTorch installation (if using an NVIDIA GPU)

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd NoteLens
```

### 2. Create a virtual environment

Windows:

```powershell
py -3.11 -m venv .venv
.venv\Scripts\activate
```

Linux / macOS:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

Install PyTorch using the official installation selector:

https://pytorch.org/get-started/locally/

Then install the remaining dependencies:

```bash
pip install -r requirements.txt
```

### 4. Verify GPU availability

```python
import torch

print("CUDA available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
```

### 5. Add a handwritten image

Place your handwritten document inside:

```text
data/input/
```

Supported input formats currently include PNG and JPG images.

---

## Usage

### Run handwriting recognition

```bash
python src/ocr.py
```

### Run handwritten line segmentation

```bash
python src/segmentation.py
```

### Visualize extracted lines

```bash
python src/visualize.py
```

### Debug the horizontal projection profile

```bash
python src/debug_projection.py
```

### Run the integrated pipeline

```bash
python src/pipeline.py
```

The integrated pipeline is intended to:

1. Load a handwritten document.
2. Segment individual text lines.
3. Recognize each line using TrOCR.
4. Combine the recognized text.
5. Save the extracted document under `data/processed/recognized.txt`.

---

## Experiments and Development

NoteLens is being developed incrementally, with experiments used to evaluate and improve individual components.

### Handwritten Line Segmentation

The initial implementation used horizontal projection profiles to identify handwritten regions.

Early experiments resulted in multiple text lines being grouped into a single region.

The algorithm was subsequently improved using:

- Projection smoothing.
- Dynamic row thresholds.
- Reduced row-merging gaps.
- Minimum region-height filtering.

**Current experimental result:** The segmentation algorithm successfully identifies nine individual text regions in the initial handwritten sample.

This is an initial sample-specific result, not a general segmentation accuracy benchmark.

Further testing across different handwriting styles and document layouts is required.

### Handwriting Recognition

The project uses pretrained TrOCR rather than training a recognition model from scratch.

Initial experiments demonstrated that recognizing individual handwritten lines produces better results than directly passing an entire handwritten page to the model.

Formal recognition accuracy evaluation is planned using:

- Character Error Rate (CER).
- Word Error Rate (WER).

---

## Development Roadmap

| Phase | Objective | Status |
|---|---|---|
| 1 | OCR engine and line segmentation | In progress |
| 2 | Intelligent document reconstruction | Planned |
| 3 | AI-powered note understanding | Planned |
| 4 | Backend and frontend development | Planned |
| 5 | Testing, optimization and deployment | Planned |

### Future AI Capabilities

The long-term goal is to develop NoteLens into an intelligent note-processing system rather than just an OCR application.

Potential capabilities include:

- **AI Summarization:** Convert lengthy handwritten notes into concise summaries.
- **Concept Extraction:** Identify important topics, definitions, and concepts.
- **Flashcard Generation:** Automatically generate study flashcards from digitized notes.
- **Semantic Search:** Find relevant information across a collection of handwritten documents.
- **Document Understanding:** Identify headings, paragraphs, lists, and other document structures.

---

## Project Goals

NoteLens is being developed to explore practical applications of:

- Computer Vision.
- Deep Learning.
- Transformer architectures.
- Optical Character Recognition.
- Document Intelligence.
- Applied Artificial Intelligence.

The emphasis is on understanding and engineering the complete pipeline, from raw image input to meaningful digital output.

---

## License

License not yet specified.

---

**NoteLens — Making handwritten knowledge digital.**
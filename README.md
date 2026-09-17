# Smart Document Scanner and Image Enhancement System Using OpenCV

## 1. Project Overview

The Smart Document Scanner and Image Enhancement System is a Python-based computer vision project developed using OpenCV. It processes photographs of documents and converts them into clearer, scanned-style outputs.

The system performs image preprocessing, document boundary detection, perspective correction, and image enhancement.

## 2. Problem Statement

Photographs of documents may contain perspective distortion, uneven lighting, noise, and unclear text. Manually correcting these problems can be time-consuming.

This project aims to automate basic document scanning and image enhancement using computer vision techniques.

## 3. Objectives

- Detect document boundaries in images.
- Reduce image noise during preprocessing.
- Correct perspective distortion.
- Improve document readability.
- Provide command-line execution.
- Save scanned and enhanced outputs.

## 4. Technologies Used

- Python
- OpenCV
- NumPy
- Matplotlib
- argparse

## 5. Features

### 5.1 Image Preprocessing

- Grayscale conversion
- Gaussian Blur
- Canny Edge Detection

### 5.2 Document Boundary Detection

- Contour detection
- Contour approximation
- Four-sided document boundary identification

### 5.3 Perspective Correction

- Document corner ordering
- Projective transformation
- Perspective correction

### 5.4 Image Enhancement

- Grayscale conversion
- CLAHE contrast enhancement
- Adaptive thresholding

### 5.5 Output Export

- Save perspective-corrected document
- Save enhanced document
- Specify output directory through command-line arguments

## 6. Project Structure

    Smart-Document-Scanner/
    │
    ├── main.py
    ├── requirements.txt
    │
    ├── input_images/
    │   └── document.jpg
    │
    ├── output_images/
    │   ├── scanned_document.jpg
    │   └── enhanced_document.jpg
    │
    └── src/
        ├── perspective_transform.py
        └── enhancement.py

## 7. Installation Instructions

### Step 1: Clone the Repository

    git clone https://github.com/<your-github-username>/<your-repository-name>.git

    cd Smart-Document-Scanner

### Step 2: Create a Virtual Environment

    py -m venv venv

### Step 3: Activate the Virtual Environment

For Windows PowerShell:

    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

    venv\Scripts\activate

### Step 4: Install Dependencies

    py -m pip install -r requirements.txt

## 8. How to Run the Project

Place your document image inside the input_images folder.

Example:

    input_images/document.jpg

Run the following command:

    py main.py --input input_images/document.jpg --output output_images

Replace the filename with the actual name of your image if required.

## 9. Expected Output

The system generates the following files:

### scanned_document.jpg

Contains the document after perspective correction.

### enhanced_document.jpg

Contains the perspective-corrected document after image enhancement and adaptive thresholding.

## 10. Computer Vision Concepts Used

| Concept | Purpose |
|---|---|
| Grayscale Conversion | Converts images into intensity values |
| Gaussian Blur | Reduces image noise |
| Canny Edge Detection | Detects image edges |
| Contour Detection | Identifies object boundaries |
| Contour Approximation | Approximates contours using fewer points |
| Projective Transformation | Corrects document perspective |
| CLAHE | Improves local contrast |
| Adaptive Thresholding | Creates a binary document image |

## 11. Limitations

- Document detection depends on image quality.
- Complex backgrounds may cause incorrect contour selection.
- Blurry or partially hidden documents may not be detected.
- The project does not include OCR or text extraction.
- Output quality depends on lighting and camera angle.

## 12. Testing Approach

The project can be tested using document images with different conditions:

- Angled document images
- Uneven lighting
- Simple backgrounds
- Moderate image noise
- Images without documents

Testing checks whether the system can:

1. Load the input image.
2. Detect the document boundary.
3. Correct perspective.
4. Generate enhanced output.
5. Save the results successfully.

## 13. Future Enhancements

- Improved document boundary detection
- Shadow removal
- Automatic document orientation correction
- OCR-based text extraction
- PDF export
- Graphical user interface

## 14. Author

Name: Srishti Manav

Course: Computer Vision

Project Type: Individual Project

Institution: VIT Bhopal University

## 15. License

This project is developed for academic and educational purposes.

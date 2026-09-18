# Smart Document Scanner and Image Enhancement System

## 1. Project Overview

The **Smart Document Scanner and Image Enhancement System** is a Python-based computer vision project developed using OpenCV. It converts a photograph of a physical document into a scanned-style digital document.

The system detects the document boundary, corrects perspective distortion, enhances the image, and saves the processed outputs in a selected folder. The project is executable through the command line and does not require a graphical user interface.

## 2. Features

- Accepts an input image through command-line arguments.
- Validates whether the input image can be loaded.
- Converts the image into grayscale.
- Applies Gaussian blur to reduce noise.
- Detects edges using the Canny edge detector.
- Detects possible document boundaries using contours.
- Identifies a four-corner contour.
- Corrects perspective distortion using projective transformation.
- Enhances the corrected image using CLAHE.
- Applies adaptive thresholding to create a scanned-style output.
- Saves the corrected and enhanced images to the output directory.
- Displays status and error messages in the terminal.

## 3. Technologies and Tools Used

- **Programming Language:** Python 3
- **Computer Vision Library:** OpenCV
- **Numerical Processing:** NumPy
- **Image Visualization/Analysis:** Matplotlib (optional dependency)
- **Development Environment:** Visual Studio Code
- **Version Control:** Git and GitHub

## 4. Project Structure

```text
Smart-Document-Scanner/
│
├── main.py
├── requirements.txt
├── README.md
├── statement.md
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
```

## 5. Installation Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/srishtii-20/Smart-Document-Scanner.git
```

### Step 2: Create a Virtual Environment

On Windows:

```powershell
py -m venv venv
```

### Step 3: Activate the Virtual Environment

For PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
venv\Scripts\activate
```

### Step 4: Install Dependencies

```powershell
py -m pip install -r requirements.txt
```

If the requirements file has not been created yet, install the dependencies manually:

```powershell
py -m pip install opencv-python numpy matplotlib
```

## 6. Input Image Preparation

1. Create an `input_images` folder in the project root.
2. Add a clear photograph of a document to this folder.
3. Use the exact image filename in the command.
4. For better results, use an image in which the document has visible edges and limited background obstruction.

Example:

```text
input_images/document.jpg
```

## 7. How to Run the Project

Run the following command from the project root:

```powershell
py main.py --input input_images/document.jpg --output output_images
```

Replace `document.jpg` with the actual input filename if required.

### Expected Terminal Output

```text
Image loaded successfully
Document detected successfully
Perspective correction completed
Image enhancement completed
Project completed successfully
```

The output folder will contain:

- `scanned_document.jpg`: Perspective-corrected document image.
- `enhanced_document.jpg`: Enhanced, thresholded document image.

## 8. Testing Instructions

### Test Case 1: Valid Document Image

**Input:** A clear image containing a document with visible boundaries.

**Command:**

```powershell
py main.py --input input_images/document.jpg --output output_images
```

**Expected Result:**

- The image loads successfully.
- A document boundary is detected.
- Perspective correction is performed.
- Enhanced output images are saved.

### Test Case 2: Missing Input File

**Command:**

```powershell
py main.py --input input_images/missing.jpg --output output_images
```

**Expected Result:**

```text
Error: Image not found
```

### Test Case 3: Image Without a Detectable Document Boundary

**Input:** An image without a clear rectangular document.

**Expected Result:**

```text
Document boundary not detected
```

The system should stop processing without generating an invalid scanned output.

## 9. Computer Vision Techniques Used

| Technique | Purpose |
|---|---|
| Grayscale Conversion | Simplifies the image into intensity values |
| Gaussian Blur | Reduces image noise |
| Canny Edge Detection | Detects strong edges |
| Contour Detection | Finds boundaries of connected regions |
| Polygon Approximation | Approximates contours using fewer points |
| Perspective Transformation | Converts an angled document into a rectangular view |
| CLAHE | Improves local image contrast |
| Adaptive Thresholding | Produces a high-contrast scanned-style image |

## 10. Limitations

- The system works best when the document has a clear rectangular boundary.
- Shadows, complex backgrounds, and overlapping objects may affect detection.
- A four-sided contour is treated as a possible document boundary, so incorrect contours may occasionally be selected.
- The current implementation is designed for single-document images.
- Extremely low-quality or heavily blurred images may not produce reliable results.

## 11. Future Enhancements

- Add automatic contour filtering based on document area.
- Add support for multiple document pages.
- Include image rotation correction.
- Add a graphical user interface or web interface.
- Add OCR to extract text from scanned documents.
- Add automated image-quality metrics such as sharpness and contrast comparison.

## 12. Author

**Name:** Srishti Manav 
**Course:** Computer Vision  
**Institution:** VIT Bhopal University  
**Project Type:** Individual Project

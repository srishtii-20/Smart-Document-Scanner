import cv2
import argparse
import os

from src.perspective_transform import perspective_transform
from src.enhancement import enhance_document


def main():

    # Command-line arguments
    parser = argparse.ArgumentParser(
        description="Smart Document Scanner"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to input document image"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Output folder path"
    )

    args = parser.parse_args()

    # Create output directory
    os.makedirs(args.output, exist_ok=True)

    # Load image
    image = cv2.imread(args.input)

    if image is None:
        print("Error: Image not found")
        return

    print("Image loaded successfully")

    # Preprocessing
    gray_image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    blurred_image = cv2.GaussianBlur(
        gray_image,
        (5, 5),
        0
    )

    edges = cv2.Canny(
        blurred_image,
        50,
        150
    )

    # Find contours
    contours, hierarchy = cv2.findContours(
        edges,
        cv2.RETR_LIST,
        cv2.CHAIN_APPROX_SIMPLE
    )

    contours = sorted(
        contours,
        key=cv2.contourArea,
        reverse=True
    )

    document_contour = None

    for contour in contours:

        perimeter = cv2.arcLength(
            contour,
            True
        )

        approximation = cv2.approxPolyDP(
            contour,
            0.02 * perimeter,
            True
        )

        if len(approximation) == 4:

            document_contour = approximation
            break

    if document_contour is None:

        print("Document boundary not detected")
        return

    print("Document detected successfully")

    # Perspective correction
    scanned_document = perspective_transform(
        image,
        document_contour
    )

    scanned_path = os.path.join(
        args.output,
        "scanned_document.jpg"
    )

    cv2.imwrite(
        scanned_path,
        scanned_document
    )

    print("Perspective correction completed")

    # Image enhancement
    enhanced_document = enhance_document(
        scanned_document
    )

    enhanced_path = os.path.join(
        args.output,
        "enhanced_document.jpg"
    )

    cv2.imwrite(
        enhanced_path,
        enhanced_document
    )

    print("Image enhancement completed")

    print("Project completed successfully")


if __name__ == "__main__":
    main()
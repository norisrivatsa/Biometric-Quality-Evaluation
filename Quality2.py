import cv2
import numpy as np
import os

def calculate_blur_score(image):
    laplacian_var = cv2.Laplacian(image, cv2.CV_64F).var()
    return laplacian_var

def calculate_minutiae_points(image):
    fingerprint_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresholded_image = cv2.threshold(fingerprint_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    kernel = np.ones((3, 3), np.uint8)
    processed_image = cv2.morphologyEx(thresholded_image, cv2.MORPH_OPEN, kernel)
    edges = cv2.Canny(processed_image, 50, 150)
    lsd = cv2.createLineSegmentDetector(0)
    lines, _, _, _ = lsd.detect(edges)
    minutiae_count = len(lines)
    return minutiae_count

def calculate_score(image_path):
    image = cv2.imread(image_path)
    blur_score = calculate_blur_score(image)
    minutiae_points = calculate_minutiae_points(image)
    fin_blur = 0
    fin_min = 0

    # Blur rating
    if blur_score in range(0, 1000):
        fin_blur = 1
    elif blur_score in range(1000, 2000):
        fin_blur = 2
    elif blur_score in range(2000, 3000):
        fin_blur = 3
    elif blur_score in range(3000, 4000):
        fin_blur = 4
    elif blur_score in range(4000, 5000):
        fin_blur = 5
    elif blur_score in range(5000, 6000):
        fin_blur = 6

    # Min rating
    if minutiae_points in range(0, 200):
        fin_min = 1
    elif minutiae_points in range(200, 400):
        fin_min = 2
    elif minutiae_points in range(400, 600):
        fin_min = 3
    elif minutiae_points in range(600, 800):
        fin_min = 4
    
    score = fin_blur * 10 + fin_min * 10
    return score

database_dir = input("Path of the database directory: ")
image_files = os.listdir(database_dir)

for image_file in image_files:
    image_path = os.path.join(database_dir, image_file)
    score = calculate_score(image_path)
    print("Image:", image_file)
    print("Blur Score:", calculate_blur_score(cv2.imread(image_path)))
    print("Minutiae Points:", calculate_minutiae_points(cv2.imread(image_path)))
    print("Total Score:", score)
    print()

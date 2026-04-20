import cv2
import numpy as np
import os

def perform_segmentation(image_path, threshold_val, output_prefix="result"):
    img = cv2.imread(image_path)

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray_img, threshold_val, 255, cv2.THRESH_BINARY)

    kernel = np.ones((5, 5), np.uint8)
    morph_img = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    contours, hierarchy = cv2.findContours(morph_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    segmented_img = img.copy()
    cv2.drawContours(segmented_img, contours, -1, (0, 255, 0), 2)

    window_name = f"{output_prefix}_Thresh{threshold_val}"
    cv2.imshow(window_name, segmented_img)


images = {
    "people": "people.jpg",
    "objects": "objects.jpg"
}

thresholds = [200, 20]

for img_name, img_path in images.items():
    if not os.path.exists(img_path):
        print(f"File {img_path} not found. Skipping.")
        continue

    for threshold in thresholds:
        perform_segmentation(img_path, threshold, output_prefix=img_name)

cv2.waitKey(0)
cv2.destroyAllWindows()
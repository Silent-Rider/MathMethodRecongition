import cv2
import numpy as np
import os

def perform_kmeans_segmentation(image_path, k_value, output_prefix="result"):
    img = cv2.imread(image_path)

    original_shape = img.shape

    pixel_vals = img.reshape((-1, 3))
    pixel_vals = np.float32(pixel_vals)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85)
    attempts = 10
    flags = cv2.KMEANS_RANDOM_CENTERS

    compactness, labels, centers = cv2.kmeans(
        pixel_vals,
        k_value,
        None,
        criteria,
        attempts,
        flags
    )

    centers = np.uint8(centers)
    segmented_data = centers[labels.flatten()]
    segmented_img = segmented_data.reshape((original_shape))

    window_name = f"{output_prefix}_K{k_value}"
    cv2.imshow(window_name, segmented_img)


images = {
    # "people": "people.jpg",
    "stationery": "stationery.jpg"
}

k_values = [3, 5, 8]

for img_name, img_path in images.items():
    if not os.path.exists(img_path):
        print(f"File {img_path} not found. Skipping.")
        continue

    for k in k_values:
        perform_kmeans_segmentation(img_path, k, output_prefix=img_name)

cv2.waitKey(0)
cv2.destroyAllWindows()
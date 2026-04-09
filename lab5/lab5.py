import cv2
import sys
img = cv2.imread('image.jpg', 0)

if img is None:
    print("Ошибка: изображение 'image.jpg' не найдено!")
    sys.exit()
edges = cv2.Canny(img, threshold1=30, threshold2=300)

cv2.imshow('Original Image', img)
cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

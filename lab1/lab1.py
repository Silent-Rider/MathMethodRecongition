# 1. Установка библиотек OpenCV-Python, Numpy и Matplotlib

import cv2
import numpy as np

# print(cv2.__version__)

# 2. Работа с файлами изображений

# img = cv2.imread("sprite.png", cv2.IMREAD_COLOR)
# print(img)
#
# img = cv2.imread("sprite.png", cv2.IMREAD_COLOR)
# cv2.imshow("Sprite", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 3. Сохранение изображений

# img = cv2.imread('sprite.png')
# filename = 'savedImage.jpg'
# cv2.imwrite(filename, img)
# img = cv2.imread(filename)
# cv2.imshow("Sprite", img)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 4. Вращение изображений

# path = 'sprite.png'
# src = cv2.imread(path)
# window_name = 'Image'
# image = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)
#
# cv2.imshow(window_name, image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
#
# FILE_NAME = 'sprite.png'
#
# img = cv2.imread(FILE_NAME)
#
# (rows, cols) = img.shape[:2]
# M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
# res = cv2.warpAffine(img, M, (cols, rows))
#
# cv2.imshow("Sprite", res)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 5. Изменение размера изображения

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# image = cv2.imread("sprite.png", 1)
#
# half = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1)
# bigger = cv2.resize(image, (1050, 1610))
#
# stretch_near = cv2.resize(image, (780, 540),
#  interpolation = cv2.INTER_NEAREST)
#
# Titles =["Original", "Half", "Bigger", "Interpolation Nearest"]
# images =[image, half, bigger, stretch_near]
# count = 4
#
# for i in range(count):
#  plt.subplot(2, 3, i + 1)
#  plt.title(Titles[i])
#  plt.imshow(images[i])
#
# plt.show()

# 6. Цветовые пространства

# import cv2
#
# path = 'sprite.png'
# src = cv2.imread(path)
# window_name = 'Sprite'
#
# image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY )
# cv2.imshow(window_name, image)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Арифметические операции
# 7. Добавление изображения

# leaf = cv2.imread('leaf_mask.png')
# spot = cv2.imread('spot_mask.png')
#
# weightedSum = cv2.addWeighted(leaf, 0.5, spot, 0.4, 0)
#
# cv2.imshow('Weighted Image', weightedSum)
#
# if cv2.waitKey(0) & 0xff == 27:
#     cv2.destroyAllWindows()

# 8. Вычитание изображения
# leaf = cv2.imread('leaf_mask.png')
# spot = cv2.imread('spot_mask.png')
#
# sub = cv2.subtract(leaf, spot)
# cv2.imshow('Subtracted Image', sub)
#
# if cv2.waitKey(0) & 0xff == 27:
#  cv2.destroyAllWindows()

# Побитовые операции над двоичным изображением
# star = cv2.imread('star.png')
# squares = cv2.imread('squares.png')
#
# squares = cv2.resize(squares, (star.shape[1], star.shape[0]),
#                      interpolation=cv2.INTER_NEAREST)
# cv2.imwrite('squares.png', squares)
# cv2.imshow('star', star)
# cv2.imshow('squares', squares)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 9. Побитовая обработка и операция
# star = cv2.imread('star.png')
# squares = cv2.imread('squares.png')
# dest_and = cv2.bitwise_and(star, squares, mask = None)
# cv2.imshow('Bitwise And', dest_and)
# if cv2.waitKey(0) & 0xff == 27:
#     cv2.destroyAllWindows()
#
# # 10. Побитовая операция ИЛИ
# star = cv2.imread('star.png')
# squares = cv2.imread('squares.png')
# dest_or = cv2.bitwise_or(star, squares, mask = None)
#
# cv2.imshow('Bitwise OR', dest_or)
#
# if cv2.waitKey(0) & 0xff == 27:
#  cv2.destroyAllWindows()
#
# # 11. Побитовая операция XOR
# star = cv2.imread('star.png')
# squares = cv2.imread('squares.png')
# dest_not1 = cv2.bitwise_not(star, mask = None)
# dest_not2 = cv2.bitwise_not(squares, mask = None)
# cv2.imshow('Bitwise NOT on image 1', dest_not1)
# cv2.imshow('Bitwise NOT on image 2', dest_not2)
#
# if cv2.waitKey(0) & 0xff == 27:
#  cv2.destroyAllWindows()

# 12 Смещение изображений Python OpenCV
# import cv2
# import numpy as np
#
# image = cv2.imread('sprite.png')
#
# height, width = image.shape[:2]
# quarter_height, quarter_width = height / 4, width / 4
#
# T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])
# img_translation = cv2.warpAffine(image, T, (width, height))
#
# cv2.imshow('Translation', img_translation)
# cv2.waitKey(0)
#
# cv2.destroyAllWindows()

# 13 Обнаружение границ

# import cv2
#
# FILE_NAME = 'sprite.png'
#
# img = cv2.imread(FILE_NAME)
# edges = cv2.Canny(img, 100, 200)
#
# cv2.imshow('Edges', edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 14 Простое определение порога
# image1 = cv2.imread('sprite.png')
# img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
#
# _, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
# _, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
# _, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
# _, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
# _, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)
#
# cv2.imshow('Binary Threshold', thresh1)
# cv2.imshow('Binary Threshold Inverted', thresh2)
# cv2.imshow('Truncated Threshold', thresh3)
# cv2.imshow('Set to 0', thresh4)
# cv2.imshow('Set to 0 Inverted', thresh5)
#
#
# if cv2.waitKey(0) & 0xff == 27:
#  cv2.destroyAllWindows()

# 15 Адаптивное пороговое значение
# image1 = cv2.imread('sprite.png')
# img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
#
# thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
#  cv2.THRESH_BINARY, 199, 5)
# thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#  cv2.THRESH_BINARY, 199, 5)
#
# cv2.imshow('Adaptive Mean', thresh1)
# cv2.imshow('Adaptive Gaussian', thresh2)
# if cv2.waitKey(0) & 0xff == 27:
#  cv2.destroyAllWindows()

# 16 Пороговое значение Otsu
# image1 = cv2.imread('sprite.png')
#
# img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
# ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY +
#                              cv2.THRESH_OTSU)
#
# cv2.imshow('Otsu Threshold', thresh1)
#
#
# if cv2.waitKey(0) & 0xff == 27:
#  cv2.destroyAllWindows()

# 17 Размытие изображения
# image = cv2.imread('sprite.png')
# cv2.imshow('Original Image', image)
#
# Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
# cv2.imshow('Gaussian Blurring', Gaussian)
#
# median = cv2.medianBlur(image, 5)
# cv2.imshow('Median Blurring', median)
#
# bilateral = cv2.bilateralFilter(image, 9, 75, 75)
# cv2.imshow('Bilateral Blurring', bilateral)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 18 Двусторонняя фильтрация

# img = cv2.imread('sprite.png')
#
# bilateral = cv2.bilateralFilter(img, 15, 100, 100)
#
# cv2.imshow('Bilateral', bilateral)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 19 Контуры изображения

# image = cv2.imread('sprite.png')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# edged = cv2.Canny(gray, 30, 200)
# contours, hierarchy = cv2.findContours(edged,
#  cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#
# cv2.imshow('Canny Edges After Contouring', edged)
#
# print("Number of Contours found = " + str(len(contours)))
# cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
#
# cv2.imshow('Contours', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 20 Размывание и расширение
# img = cv2.imread('sprite.png', 0)
#
# kernel = np.ones((5,5), np.uint8)
#
# img_erosion = cv2.erode(img, kernel, iterations=1)
# img_dilation = cv2.dilate(img, kernel, iterations=1)
#
# cv2.imshow('Input', img)
# cv2.imshow('Erosion', img_erosion)
# cv2.imshow('Dilation', img_dilation)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 21 Сопоставление функций

# query_img = cv2.imread('sprite.png')
# train_img = cv2.imread('sprite.png')
#
# query_img_bw = cv2.cvtColor(query_img,cv2.COLOR_BGR2GRAY)
# train_img_bw = cv2.cvtColor(train_img, cv2.COLOR_BGR2GRAY)
#
# orb = cv2.ORB().create()
#
# queryKeypoints, queryDescriptors = orb.detectAndCompute(query_img_bw,None)
# trainKeypoints, trainDescriptors = orb.detectAndCompute(train_img_bw,None)
#
# matcher = cv2.BFMatcher()
# matches = matcher.match(queryDescriptors,trainDescriptors)
#
# final_img = cv2.drawMatches(query_img, queryKeypoints,
# train_img, trainKeypoints, matches[:20],None)
#
# final_img = cv2.resize(final_img, (1000,650))
#
# cv2.imshow("Matches", final_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 22 Рисование на изображениях

# img = np.zeros((400, 400, 3), dtype = "uint8")
# cv2.rectangle(img, (30, 30), (250, 250), (0, 110, 255), 5)
#
# cv2.imshow('dark', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import cv2
#
# laptop = cv2.imread('laptop.jpg')
# cathedral = cv2.imread('cathedral.jpg')
#
# images = [laptop, cathedral]
# for img in images:
#     sift = cv2.xfeatures2d.SIFT_create(contrastThreshold=0.05)
#     keypoints, descriptors = sift.detectAndCompute(img, None)
#
#     img_keypoints = cv2.drawKeypoints(img, keypoints, None)
#
#     cv2.imshow("Image with keypoints", img_keypoints)
#
#     print("Found %d keypoints" % len(keypoints))
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# import cv2
#
# laptop = cv2.imread('laptop.jpg')
# cathedral = cv2.imread('cathedral.jpg')
#
# images = [laptop, cathedral]
# for img in images:
#     orb = cv2.ORB_create()
#     keypoints, descriptors = orb.detectAndCompute(img, None)
#     img_keypoints = cv2.drawKeypoints(img, keypoints, None)
#     cv2.imshow("Image with keypoints", img_keypoints)
#     print("Found %d keypoints" % len(keypoints))
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

import cv2
import numpy as np

imgL = cv2.imread("bottle1.jpg", 0)
imgR = cv2.imread("bottle2.jpg", 0)

if imgL is None or imgR is None:
    print("Ошибка: Не удалось загрузить изображения im0.png и/или im1.png")
    print("Убедитесь, что файлы лежат в одной папке со скриптом.")
else:
    minDisparity = 0
    numDisparities = 96
    blockSize = 15
    disp12MaxDiff = 2
    uniquenessRatio = 13
    speckleWindowSize = 120
    speckleRange = 32

    stereo = cv2.StereoSGBM_create(
        minDisparity=minDisparity,
        numDisparities=numDisparities,
        blockSize=blockSize,
        disp12MaxDiff=disp12MaxDiff,
        uniquenessRatio=uniquenessRatio,
        speckleWindowSize=speckleWindowSize,
        speckleRange=speckleRange
    )
    disp = stereo.compute(imgL, imgR).astype(np.float32)
    disp = cv2.normalize(disp, 0, 255, cv2.NORM_MINMAX)

    cv2.imshow("Left Image", imgL)
    cv2.imshow("Right Image", imgR)
    cv2.imshow("Disparity Map", disp)

    print("Карта диспаратности построена. Нажмите любую клавишу для выхода.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
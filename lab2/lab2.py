import cv2
import numpy as np
import glob

CHECKERBOARD = (6, 9)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

threeD_points = []
twoD_points = []

object_points_3d = np.zeros((1, CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
object_points_3d[0, :, :2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)

images = glob.glob("*.jpg")

for filename in images:
    image = cv2.imread(filename)
    grayColor = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(grayColor, CHECKERBOARD,
        cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE)

    if ret:
        threeD_points.append(object_points_3d)
        corners2 = cv2.cornerSubPix(grayColor, corners, (11, 11), (-1, -1), criteria)
        twoD_points.append(corners2)
        image = cv2.drawChessboardCorners(image, CHECKERBOARD, corners2, ret)
    else: continue

    cv2.imshow(filename, image)
    cv2.waitKey(0)

cv2.destroyAllWindows()

ret, matrix, distortion, r_vecs, t_vecs = cv2.calibrateCamera(
    threeD_points, twoD_points, grayColor.shape[::-1], None, None)

print("Матрица камеры:")
print(matrix)
print("Коэффициент искажения:")
print(distortion)
print("Векторы вращения:")
print(r_vecs)
print("Векторы перевода:")
print(t_vecs)

for filename in images:
    img = cv2.imread(filename)
    h, w = img.shape[:2]
    new_camera_matrix, roi = cv2.getOptimalNewCameraMatrix(
        matrix, distortion,(w, h), 1, (w, h))

    dst = cv2.undistort(img, matrix, distortion, None, new_camera_matrix)

    x, y, w, h = roi
    dst = dst[y:y + h, x:x + w]

    save_name = "corrected_" + filename
    cv2.imwrite(save_name, dst)
    print(f"Сохранено исправленное фото: {save_name}")
    cv2.imshow(save_name, dst)
    cv2.waitKey(0)

cv2.destroyAllWindows()
import cv2

def main():
    video_path = 'cars.mp4'

    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        print(f"Ошибка: Не удалось открыть видео '{video_path}'")
        return

    fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)

    while True:
        ret, frame = video.read()
        if not ret:
            break

        fgmask = fgbg.apply(frame)
        _, fgmask_clean = cv2.threshold(fgmask, 250, 255, cv2.THRESH_BINARY)

        contours, hierarchy = cv2.findContours(fgmask_clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) > 0:
            max_contour = max(contours, key=cv2.contourArea)

            if cv2.contourArea(max_contour) > 500:
                x, y, w, h = cv2.boundingRect(max_contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('Frame', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
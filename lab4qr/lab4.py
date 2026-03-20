import qrcode

# data = "https://www.youtube.com/@SilentRider"
# QRCodefile = "SilentRider-Channel.png"
# QRimage = qrcode.make(data)
# QRimage.save(QRCodefile)

# import qrcode
# import numpy as np
# data = "https://www.youtube.com/@SilentRider"
# QRCodefile = "CustomisedImgBoxQRCode.png"
# qrObject = qrcode.QRCode(version=1, box_size=15)
# qrObject.add_data(data)
# qrObject.make()
# image = qrObject.make_image()
# image.save(QRCodefile)
# print("Размер QR изображения:")
# print(np.array(qrObject.get_matrix()).shape)

# import qrcode
# data = "https://www.youtube.com/@SilentRider"
# QRCodefile = "CustomisedFillColorQRCode.png"
# qrObject = qrcode.QRCode()
# qrObject.add_data(data)
# qrObject.make()
# image = qrObject.make_image(fill_color="orange")
# image.save(QRCodefile)

# Importing library
# import qrcode
#
# data = "https://www.youtube.com/@SilentRider"
# QRCodefile = "CustomisedBGColorQRCode.png"
# qrObject = qrcode.QRCode()
# qrObject.add_data(data)
# qrObject.make()
# image = qrObject.make_image(back_color="cyan")
# image.save(QRCodefile)

# Importing libraries
# import qrcode
# data = "https://www.youtube.com/@SilentRider"
# QRCodefile = "CustomisedBorderQRCode.png"
# qrObject = qrcode.QRCode(border=15)
# qrObject.add_data(data)
# qrObject.make()
# image = qrObject.make_image()
# image.save(QRCodefile)

# Import Library
# import cv2
# filename = "SilentRider-Channel.png"
# image = cv2.imread(filename)
# detector = cv2.QRCodeDetector()
# data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
# if vertices_array is not None:
#     print("QRCode data:")
#     print(data)
# else:
#     print("There was some error")

import cv2
cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
while True:
    _, img = cap.read()
    data, vertices_array, _ = detector.detectAndDecode(img)
    if vertices_array is not None:
        if data:
            print("QR Code detected, data:", data)
    cv2.imshow("img", img)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()


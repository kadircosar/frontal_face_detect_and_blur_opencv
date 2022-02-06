import cv2
import math
import numpy as np

#  face classifier
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# video capture
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    if ret:
        face_rectangle = face_cascade.detectMultiScale(frame, minNeighbors=6)
        mask_img = np.zeros(frame.shape, dtype='uint8')

        for x, y, w, h in face_rectangle:
            circle_center = ((x + x + w) // 2, (y + y + h) // 2)
            circle_radius = int(math.sqrt(w * w + h * h) // 2)
            cv2.circle(mask_img, circle_center, circle_radius, (255, 255, 255), -1)
            img_all_blurred = cv2.medianBlur(frame, 99)
            img_face_blurred = np.where(mask_img > 0, img_all_blurred, frame)

        cv2.imshow("face detect", img_face_blurred)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


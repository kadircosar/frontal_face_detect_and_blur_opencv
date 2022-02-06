import cv2
import matplotlib.pyplot as plt
import math
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", help="path to the images", default="barcelona.jpg")

args = vars(ap.parse_args())
PATH = args["path"]


class Config:
    path: str = PATH


# read image
barca = cv2.imread(f"{Config.path}")
barca = cv2.cvtColor(barca, cv2.COLOR_BGR2RGB)

# visualize image
plt.imshow(barca)
plt.axis("off")
plt.title("original image")
plt.show()

#  face classifier
barca_gray = cv2.imread("barcelona.jpg", 0)  # we use gray scale for better results of face detection
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# u need to change this minNeighbors parameter according to output for better results for this image 6 was the best
face_rectangle = face_cascade.detectMultiScale(barca_gray, minNeighbors=6)

# creating rectangle for detected face
for x, y, w, h in face_rectangle:
    cv2.rectangle(barca, (x, y), (x + w, y + h), (255, 255, 255), 10)

plt.imshow(barca)
plt.axis("off")
plt.title("Face detected image")
plt.show()

# create mask
mask_img = np.zeros(barca.shape, dtype='uint8')

circle_center = []  # list of circle center
circle_radius = []  # list of circle radius
for i in range(len(face_rectangle)):
    for x, y, w, h in face_rectangle:
        circle_center.append(((x + x + w) // 2, (y + y + h) // 2))
        circle_radius.append(int(math.sqrt(w * w + h * h) // 2))
        cv2.circle(mask_img, circle_center[i], circle_radius[i], (255, 255, 255), -1)


img_all_blurred = cv2.medianBlur(barca, 99)
img_face_blurred = np.where(mask_img > 0, img_all_blurred, barca)

plt.imshow(img_face_blurred)
plt.axis("off")
plt.title("blurred face")
plt.show()

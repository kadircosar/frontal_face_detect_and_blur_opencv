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
img = cv2.imread(f"{Config.path}")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# visualize image
plt.imshow(img)
plt.axis("off")
plt.title("original image")
plt.show()

#  face classifier
img_gray = cv2.imread(f"{Config.path}", 0)  # we use gray scale for better results of face detection
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# u need to change this minNeighbors parameter according to output for better results for this image 6 was the best
face_rectangle = face_cascade.detectMultiScale(img_gray, minNeighbors=6)

# creating rectangle for detected face
for x, y, w, h in face_rectangle:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 10)

plt.imshow(img)
plt.axis("off")
plt.title("Face detected image")
plt.show()

# create mask
mask_img = np.zeros(img.shape, dtype='uint8')


for x, y, w, h in face_rectangle:
    circle_center = ((x + x + w) // 2, (y + y + h) // 2)
    circle_radius = int(math.sqrt(w * w + h * h) // 2)
    cv2.circle(mask_img, circle_center, circle_radius, (255, 255, 255), -1)
    img_all_blurred = cv2.medianBlur(img, 99)
    img_face_blurred = np.where(mask_img > 0, img_all_blurred, img)

plt.imshow(img_face_blurred)
plt.axis("off")
plt.title("blurred face")
plt.show()

# Frontal Face Detection and blurring with opencv

This project for detectting frontal faces and blurring them all.There is a two scripts one is for images, another one is for webcam.

This is frontal face detect and blur on image:

   <img width="600" src=images/1.png></a>
   <img width="600" src=images/2.png></a>

   
# Clone 
Run this code in terminal in the path  where you want it to be cloned :

```bash
git clone https://github.com/kadircosar/frontal_face_detect_and_blur_opencv.git
```

# Install requirements
I recommend you create a new conda or a virtualenv environment to run your open-cv experiments as to not mess up dependencies of any existing project. Once you have activated the new environment, install the dependencies using pip.
before running this code in terminal make sure activate your venv that you created for this project and run this code in path that you cloned frontal_face_detect_and_blur_opencv.
```bash
pip install -r frontal_face_detect_and_blur_opencv/requirements.txt
```

# Face detect and blur on a image 
You need to choose an image and download it or just simply use barcelona.jpeg.
İf you want to use diffrent image u just need to copy your image path with tag end of it.But your image must be had only frontal face because we are using frontal face cascade otherwise it won't detect faces.Then make sure you are in frontal_face_detect_and_blur_opencv folder and run this code in terminal.

For example:

this is your image path: home/users/hat.png
```bash
python3 blurring_face_image.py --path home/users/hat.png
```
or use barcelona.jpg

```bash
python3 blurring_face_image.py --path barcelona.jpg
```
# Face detect and blur with webcam
 Make sure you are in face_detect_and_blur_opencv folder and run this code in terminal.
```bash
python3 blurring_face_webcam.py
```


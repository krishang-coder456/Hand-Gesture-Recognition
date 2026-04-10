# **Hand-Gesture-Recognition**

I have created a hand recognition project which recognizes the gesture that the user has made on the live camera. I have used hand landmarks to recognize various types of gestures. The libraries used in this project are 'opencv' and mediapipe. 

## **Libraies Used**
```
import cv2
import mediapipe as mp
```
### **Mediapipe**

_Mediapipe_ is an open-source library designed by _Google-AI-Edge_. It provides ready-to-use solutions so that coders can design ML models such as hand detection system.

### **OpenCV**

Next, I have used _OpenCV_ library which is also an open-source library which features computer vision and image processing which help coders to create projects which include computer cameras and image processing.

## **How It Works**

The project uses Mediapipe to draw identify the landmarks on a user's hand using Mediapipe. By using the coordinates of the landmarks, it has to figure out what the gesture is. It has a function defined which identifies the open figure, stores '0' in `finger` list if the finger is closed or '1' if the finger is open. 
Example:- If the thumb finger is the only finger open and total fingers open is one, the gesture is a thumbs up.
```
if fingers[0] == 1 and total_fingers == 1:
    gesture = 'thumbs up'
```


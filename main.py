from lib2to3.pytree import _Results
import cv2 
import time
import mediapipe as mp

cap = cv2.VideoCapture(0)


mp_hands = mp.solutions.hands
hands = mp_hands.Hands()



while True:
    success, img = cap.read()# returns video/image

    img_rgb = cv2.cvtColor(img,cv2.COLOR_BAYER_BGR2RGB)
    results = hands.process(img_rgb)


    cv2.imshow("image",img)#creates the window to display the vid/image
    if cv2.waitKey(1) == ord('q'):#if the asci key is of q then we breka out of the loop
        break
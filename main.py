
import cv2 
import time
import mediapipe as mp

cap = cv2.VideoCapture(0)


mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

prev_time = 0
curr_time = 0

while True:
    success, img = cap.read()# returns video/image

    img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    #print(results.multi_hand_landmarks)q

    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:
            #get id and landmarks for a hand
            for id,lm in enumerate(hand_lms.landmark):

                #print(id,lm)
                h,w,c = img.shape
                cx, cy = int(lm.x*w),int(lm.y*h)
                print(cx,cy)
        
            mp_draw.draw_landmarks(img,hand_lms,mp_hands.HAND_CONNECTIONS)#how to draw on the screen
            
            
    curr_time = time.time()
    fps = 1/(curr_time - prev_time)
    prev_time = curr_time

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,160),3)#draw text on the screen

    cv2.imshow("image",img)#creates the window to display the vid/image
    if cv2.waitKey(1) == ord('q'):#if the asci key is of q then we breka out of the loop
        break
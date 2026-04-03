import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands # getting the solution from mediapipe
mp_drawing = mp.solutions.drawing_utils # setting to draw landmarks

cap = cv2.VideoCapture(0) # capturing the video through computer camera

def count_fingers(landmarks):
    fingers = []
    if landmarks[4].x < landmarks[3].x:
        fingers.append(1)
    else:
        fingers.append(0)
    tips = [8, 12, 16, 20]
    for tip in tips:
        if landmarks[tip].y < landmarks[tip-2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers

with mp_hands.Hands(max_num_hands = 1, min_detection_confidence = 0.7, min_tracking_confidence = 0.7) as hands: # this detects 1 hand at a time
    while True:
        ret, frame = cap.read() # reading the cap
        if not ret:
            break

        h,w,c = frame.shape # h-heigjht, w-width, c-color channels
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # converting the frame to gray color
        results = hands.process(rgb) # processing using hands
        gesture = ''
        if results.multi_hand_landmarks: # if hands are detected
            for hand_landmarks in results.multi_hand_landmarks: # this loops through each detected hand
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS) # draws the landmarks on the frame
                landmarks = hand_landmarks.landmark # gives the coordinates of the landmarks
                fingers = count_fingers(landmarks)
                total_fingers = sum(fingers)
                if total_fingers == 0:
                    gesture = 'fist'
                elif total_fingers == 5:
                    gesture = 'open palm'
                elif fingers[0] == 1 and total_fingers == 1:
                    gesture = 'thumbs up'
                elif fingers[1] == 1 and fingers[2] == 1 and total_fingers == 2:
                    gesture = 'victory'
                elif fingers[1] == 1 and total_fingers == 1:
                    gesture = 'pointing up'
                else:
                    gesture = 'unkown'
        cv2.putText(frame, gesture, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
        cv2.imshow('hand gesture recogonizion', frame)
        if cv2.waitKey(1) & 0xFF == 27: # when escape button is pressed it breaks the loop
            break

cap.release()
cv2.destroyAllWindows()
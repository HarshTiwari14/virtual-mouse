import cv2
import mediapipe as mp
import pyautogui

pyautogui.FAILSAFE = False

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()

index_x = 0
index_y = 0

clicked = False   # <<< NEW — to stop continuous clicking

while True:
    success, frame = cap.read()
    if not success:
        continue

    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

            for id, lm in enumerate(hand.landmark):
                x = int(lm.x * frame_width)
                y = int(lm.y * frame_height)

                if id == 8:
                    cv2.circle(frame, (x, y), 10, (0,255,255), -1)
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y

                if id == 4:
                    cv2.circle(frame, (x, y), 10, (0,255,255), -1)
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y

                    # SINGLE CLICK logic
                    if abs(index_y - thumb_y) < 30:
                        if not clicked:            # <<< NEW
                            pyautogui.click()
                            clicked = True         # <<< NEW
                    else:
                        clicked = False            # <<< NEW

    pyautogui.moveTo(index_x, index_y)

    cv2.imshow("Virtual Mouse", frame)

    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:   # <<< NEW — press Q or ESC to stop
        break

cap.release()
cv2.destroyAllWindows()

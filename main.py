import cv2      #import opencv-python
import mediapipe as mp      #import mediapipe to detect landmarks of the hand
import pyautogui        #import pyautogui
import time     #import time

#implement logic
def count_fingers(lst):
    cnt = 0
    thresh = (lst.landmark[0].y * 100 - lst.landmark[9].y * 100) / 2

    if (lst.landmark[5].y * 100 - lst.landmark[8].y * 100) > thresh:
        cnt += 1

    if (lst.landmark[9].y * 100 - lst.landmark[12].y * 100) > thresh:
        cnt += 1

    if (lst.landmark[13].y * 100 - lst.landmark[16].y * 100) > thresh:
        cnt += 1

    if (lst.landmark[17].y * 100 - lst.landmark[20].y * 100) > thresh:
        cnt += 1

    if (lst.landmark[5].x * 100 - lst.landmark[4].x * 100) > 6:
        cnt += 1

    return cnt

cap = cv2.VideoCapture(0)
        if prev != cnt:
            if not start_init:
                start_time = time.time()
                start_init = True
            elif end_time - start_time > 0.2:
                if cnt == 1:
                    pyautogui.press("right")
                elif cnt == 2:
                    pyautogui.press("left")
                elif cnt == 3:
                    pyautogui.press("up")
                elif cnt == 4:
                    pyautogui.press("down")
                elif cnt == 5:
                    pyautogui.press("space")
                elif cnt == 0:  # Assuming a fist for volume down
                    pyautogui.press("volumeup")
                elif cnt == 6:  # Adding a hypothetical case for volume up
                    pyautogui.press("volumedown")

                prev = cnt
                start_init = False

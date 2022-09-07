import cv2
import mediapipe as mp
import LeftArm

cap = cv2.VideoCapture(0)
detector = LeftArm.ArmDector(False, 1, True, False, True, 0.5, 0.5)
count = 0
move = 0
sets = 0
while True:
    ret, img = cap.read()
    if ret:
        height, width, c = img.shape
        img = detector.find_arm(img, draw=True)
        armPoint = detector.find_armPoint(img)
    if armPoint:
        angle = detector.find_angle(img, 11, 13, 15, draw=True)
        if angle <= 45:
            if move == 0:
                count += 0.5
                move = 1
        if angle >= 90:
            if move == 1:
                count += 0.5
                move = 0
                if count == 15:
                    count = 0
                    sets += 1
        cv2.putText(img,f"Reps: {str(int(count))}",(30, 83), cv2.FONT_HERSHEY_SIMPLEX, 1,  (0, 0, 255), 2)
        cv2.putText(img, f"Sets: {str(int(sets))}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (140, 199, 0), 2)
        if cv2.waitKey(1) == ord('r'):
            count = 0
            move = 0
            sets = 0
        if cv2.waitKey(5) == ord('q'):
            break
    cv2.imshow('img', img)



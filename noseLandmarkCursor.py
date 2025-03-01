import cv2
import dlib
import pyautogui

Eye_x = -1
Eye_y = -1

cap = cv2.VideoCapture(0)

hog_face_detector = dlib.get_frontal_face_detector()

dlib_facelandmark = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
frame_counter = 0



while True:
    _, frame = cap.read() 
    frame_counter+=1

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = hog_face_detector(gray)
    for face in faces:
        face_landmarks = dlib_facelandmark(gray, face)

        for n in range(42, 48):
            x,y = face_landmarks.part(n).x,face_landmarks.part(n).y
            cv2.circle(frame, (x, y), 1, (0, 255, 255), 2)
        x = (face_landmarks.part(44).x + face_landmarks.part(45).x)//2
        y = (face_landmarks.part(45).y + face_landmarks.part(47).y)//2

        if(Eye_x == -1 and Eye_y == -1):
            Eye_x,Eye_y = x,y

        mouse_x,mouse_y = pyautogui.position()
        distance = 20
        if(x < (Eye_x - 25)):
            pyautogui.moveTo(mouse_x-distance, mouse_y)
            print("moving to :",mouse_x-distance, mouse_y)
        elif(x > (Eye_x + 25)):
            pyautogui.moveTo(mouse_x+distance, mouse_y)
            print("moving to :",mouse_x+distance, mouse_y)

        if(y < (Eye_y - 25)):
            pyautogui.moveTo(mouse_x, mouse_y-distance)
            print("moving to :",mouse_x, mouse_y-distance)
        elif(y > (Eye_y + 25)):
            pyautogui.moveTo(mouse_x, mouse_y+distance)
            print("moving to :",mouse_x, mouse_y+distance)
    rectangle = cv2.rectangle(frame,(Eye_x-25,Eye_y-25),(Eye_x+25,Eye_y+25),(255,0,0),2)
    cv2.imshow("auto_cursor", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()

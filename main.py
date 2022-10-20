import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mediapipeHands = mp.solutions.hands
hands = mediapipeHands.Hands()
mediapipeDrawing = mp.solutions.drawing_utils

while True:
    ret, img = cap.read() #create and open the camera window
    img = cv2.flip(img, 1) #flip the image so it is like a miror
    #create a list of all the different fingertips from 0 to 20
    fingerTips = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    #create an empty list for the future hand's landmarks
    landMarkList = []
    results = hands.process(img)

    #if there is a hand on the screen
    if results.multi_hand_landmarks :
        for hand_landmark in results.multi_hand_landmarks:
            #draw the landmarks as connections (lines)
            #draw the fingertips as connectors (cercles)
            mediapipeDrawing.draw_landmarks(img, hand_landmark, mediapipeHands.HAND_CONNECTIONS,
                                            mediapipeDrawing.DrawingSpec((9, 52, 28), 2, 2), mediapipeDrawing.DrawingSpec((9, 52, 28), 2, 2))
        #for each landmark add it to the list and create and id
        for id, landMark in enumerate(hand_landmark.landmark):
            landMarkList.append(landMark)
        #for each fingertip collect the coordinates x, y, z
        for tip in fingerTips:
            x, y, z = int(landMarkList[tip].x), int(landMarkList[tip].y), int(landMarkList[tip].z)
        #print the coordinates for each fingertip/landmark
        for id in enumerate(hand_landmark.landmark):
            print(id, ":", x, y, z)
        #create a method to add all the coordinates in a csv file
            #when a selected key from the key board is pushed, take a picture of the hand
            #create a csv file that is going to collect all the coordinates from the taken picture
            #/!\ don't forget to write down all the sources you use !

    cv2.imshow("Hand Tracking", img)
    cv2.waitKey(1)

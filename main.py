import csv

import cv2
import keyboard as keyboard
import mediapipe as mp

cap = cv2.VideoCapture(0)

mediapipeHands = mp.solutions.hands
hands = mediapipeHands.Hands()
mediapipeDrawing = mp.solutions.drawing_utils
coordinates = []
for i in range (21) :
    coordinates.append("x"+str(i))
    coordinates.append("y"+str(i))
    coordinates.append("z"+str(i))


def getCoordinatesForCSV(number):
    csvFile = 0
    match number:
        case 0:
            csvFile = './dataZero.csv'
        case 1 :
            csvFile = './dataOne.csv'
        case 2 :
            csvFile = './dataTwo.csv'
        case 3:
            csvFile = './dataThree.csv'
        case 4:
            csvFile = './dataFour.csv'
        case 5:
            csvFile = './dataFive.csv'
        case 6:
            csvFile = './dataSix.csv'
        case 7:
            csvFile = './dataSeven.csv'
        case 8:
            csvFile = './dataEight.csv'
        case 9:
            csvFile = './dataNine.csv'
    if keyboard.read_key():
        # print the coordinates for each fingertip/landmark
        data = []
        for id in hand_landmark.landmark:
            data.append({
                id.x,
                id.y,
                id.z,
            })
        print(data)
        # open the file in the write mode
        with open(csvFile, 'a') as file:
            # create the csv writer
            writer = csv.writer(file)
            # write rows in the csv file
            writer.writerow(data)


while True:
    ret, img = cap.read() #create and open the camera window
    img = cv2.flip(img, 1) #flip the image so it is like a miror
    #create a list of all the different fingertips from 0 to 20
    fingerTips = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    #create coordinates for the csv file

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

        #getCoordinatesForCSV(keyboard.read_key())



    cv2.imshow("Hand Tracking", img)
    cv2.waitKey(1)

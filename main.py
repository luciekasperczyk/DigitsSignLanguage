import csv
import cv2
import keyboard as keyboard
import mediapipe as mp
import xlsxwriter

cap = cv2.VideoCapture(0)
mediapipeHands = mp.solutions.hands
hands = mediapipeHands.Hands()
mediapipeDrawing = mp.solutions.drawing_utils
coordinates = []
for i in range(21):
    coordinates.append("x" + str(i))
    coordinates.append("y" + str(i))
    coordinates.append("z" + str(i))

#with open("data.csv", 'a') as file:
#     # create the csv writer
#     writer = csv.writer(file)
#     # write rows in the csv file
#     writer.writerow(coordinates)


def getCoordinatesForCSV():
    # print the coordinates for each fingertip/landmark
    write = False
    data = [""]
    if keyboard.is_pressed("0"):
        data.append("digit_zero")
        write = not write
    elif keyboard.is_pressed("1"):
        data.append("digit_one")
        write = not write
    elif keyboard.is_pressed("2"):
        data.append("digit_two")
        write = not write
    elif keyboard.is_pressed("3"):
        data.append("digit_three")
        write = not write
    elif keyboard.is_pressed("4"):
        data.append("digit_four")
        write = not write
    elif keyboard.is_pressed("5"):
        data.append("digit_five")
        write = not write
    elif keyboard.is_pressed("6"):
        data.append("digit_six")
        write = not write
    elif keyboard.is_pressed("7"):
        data.append("digit_seven")
        write = not write
    elif keyboard.is_pressed("8"):
        data.append("digit_eight")
        write = not write
    elif keyboard.is_pressed("9"):
        data.append("digit_nine")
        write = not write
    if write:
        for id in hand_landmark.landmark:
            data.append(id.x)
            data.append(id.y)
            data.append(id.z)
        print(data)
        # open the file in the write mode
        with open("data.csv", 'a') as file:
            # create the csv writer
            writer = csv.writer(file)
            # write rows in the csv file
            writer.writerow(data)

while True:
    ret, img = cap.read()  # create and open the camera window
    img = cv2.flip(img, 1)  # flip the image so it is like a mirror
    # create a list of all the different fingertips from 0 to 20
    fingerTips = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    # create coordinates for the csv file

    # create an empty list for the future hand's landmarks
    landMarkList = []
    results = hands.process(img)

    # if there is a hand on the screen
    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            # draw the landmarks as connections (lines)
            # draw the fingertips as connectors (circles)
            mediapipeDrawing.draw_landmarks(img, hand_landmark, mediapipeHands.HAND_CONNECTIONS,
                                            mediapipeDrawing.DrawingSpec((9, 52, 28), 2, 2),
                                            mediapipeDrawing.DrawingSpec((9, 52, 28), 2, 2))
        # for each landmark add it to the list and create an id
        for id, landMark in enumerate(hand_landmark.landmark):
            landMarkList.append(landMark)

        getCoordinatesForCSV()

main()

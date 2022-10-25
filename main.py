import cv2
import keyboard
import mediapipe as mp
import xlsxwriter

cap = cv2.VideoCapture(0)
mediapipeHands = mp.solutions.hands
hands = mediapipeHands.Hands()
mediapipeDrawing = mp.solutions.drawing_utils


def main():
    workbook = xlsxwriter.Workbook("Coordinates.xlsx")
    worksheet = workbook.add_worksheet("sheet")
    worksheet.write(0, 0, "#")
    j = 0
    for i in range(1, 63, 3):
        worksheet.write(0, i, "x"+str(j))
        worksheet.write(0, i+1, "y" + str(j))
        worksheet.write(0, i+2, "z" + str(j))
        j += 1
    while True:
        ret, img = cap.read()  # create and open the camera window
        img = cv2.flip(img, 1)  # flip the image so it is like a mirror
        # create a list of all the different fingertips from 0 to 20
        fingerTips = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
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
            # for each fingertip collect the coordinates x, y, z
            for tip in fingerTips:
                x, y, z = int(landMarkList[tip].x), int(landMarkList[tip].y), int(landMarkList[tip].z)
            # print the coordinates for each fingertip/landmark
            if keyboard.is_pressed("l"):
                    print(id, ":", x, y, z)
            elif keyboard.is_pressed("d"):
                workbook.close()

            # create a method to add all the coordinates in an Excel file
        cv2.imshow("Hand Tracking", img)
        cv2.waitKey(1)


main()

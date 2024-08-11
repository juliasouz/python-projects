import cv2
from cvzone.HandTrackingModule import HandDetector

#Initialize the webcam
webcam = cv2.VideoCapture(0)

#Initialize the Hand Tracker
hand_detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    #Capture the image from the webcam
    success, img = webcam.read()

    #Detect hands in the frame
    hands, img_hands = hand_detector.findHands(img)

    #Display the frame with annotations
    cv2.imshow("Hand Tracking - AI", img_hands)

    #Exit the application when any key is pressed
    if cv2.waitKey(1) != -1:
        break

#Release the webcam and close the windows
webcam.release()
cv2.destroyAllWindows()
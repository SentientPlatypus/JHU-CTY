import cv2
from yolov7_package import Yolov7Detector

cap = cv2.VideoCapture(0)

if __name__ == "__main__":
    while 1:
        success, frame = cap.read()
        phones_detected = 0


        phone_cascade = cv2.CascadeClassifier('6. Real anti text\Phone_Cascade.xml')


        # Convert the image to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform phone detection
        phones = phone_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around the detected phones
        for (x, y, w, h) in phones:
            phones_detected += 1
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.putText(frame, f"phones: {phones_detected}", (100, 100), cv2.FONT_HERSHEY_COMPLEX,1, (0, 255, 0), 2)
        cv2.imshow("image", frame)
        cv2.waitKey(1)

import cv2
import numpy as np

#Setup classifier


phone_cascade=cv2.CascadeClassifier('Phone_Cascade.xml')
                                    
cap=cv2.VideoCapture(0)

while True:
    ret, img=cap.read()

    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Use classifier to detect faces

    phones=phone_cascade.detectMultiScale(gray, 3, 9)


    for (x,y,w,h) in phones:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,255), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'Phone',(x-w,y-h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
    
    cv2.imshow('img', img)
    if (cv2.waitKey(30) & 0xff)==27:
        break

cap.release()
cv2.destroyAllWindows()
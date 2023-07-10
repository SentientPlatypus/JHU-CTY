import cv2
import numpy as np

#Setup classifier


phone_cascade=cv2.CascadeClassifier('6. Real anti text\Phone_Cascade.xml')
                                    
cap=cv2.VideoCapture(0)

while True:
    ret, img=cap.read()
    phonenumber = 0
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Use classifier to detect faces

    phones=phone_cascade.detectMultiScale(gray, 1.3, 10)


    for (x,y,w,h) in phones:
        phonenumber += 1
        cv2.rectangle(gray, (x,y), (x+w, y+h), (255,0,255), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(gray,'Phone',(x-w,y-h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
    
    cv2.putText(gray, f"Phones: {phonenumber}", (100, 100), cv2.FONT_HERSHEY_COMPLEX,1, (0, 255, 0), 2)

    cv2.imshow('gray', gray)
    if (cv2.waitKey(30) & 0xff)==27:
        break

cap.release()
cv2.destroyAllWindows()
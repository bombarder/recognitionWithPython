import cv2
import os
from gtts import gTTS

pedestrian_cascade = cv2.CascadeClassifier('pedestrianSign.xml')
stop_cascade = cv2.CascadeClassifier('stopSign.xml')
redLight_cascade = cv2.CascadeClassifier('redLight.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    pedestrian = pedestrian_cascade.detectMultiScale(gray, 2, 5)
    stop = stop_cascade.detectMultiScale(gray, 2, 5)
    redLight = redLight_cascade.detectMultiScale(gray, 2, 5)

    # for (x, y, w, h) in stop:
    #     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    #     tts = gTTS(text="внимание, впереди знак", lang='ru')
    #     tts.save("sign.mp3")
    #     os.system("sign.mp3")

    for (x, y, w, h) in pedestrian:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        tts = gTTS(text="внимание, впереди пешеходный переход", lang='ru')
        tts.save("pedestrian.mp3")
        os.system("pedestrian.mp3")
    #
    # for (x, y, w, h) in redLight:
    #     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    #     tts = gTTS(text="внимание, красный свет светофора", lang='ru')
    #     tts.save("redLight.mp3")
    #     os.system("redLight.mp3")

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

from cv2 import cv2
import cvzone
cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
overlay = cv2.imread('pirate.png', cv2.IMREAD_UNCHANGED)
while True:
    _, frame  = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_scale)
    for(s,e,w,h) in faces:
       # cv2.rectangle(frame,(s,e),(s+w, e+h), (0, 255, 0), 2)
        overlay_resize = cv2.resize(overlay, (int(w*1.5),int(h*1.5)))
        frame = cvzone.overlayPNG(frame, overlay_resize, [s-45,e-75])
    cv2.imshow('snap', frame)
    if cv2.waitKey(10) == ord('q'):
        break























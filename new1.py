import cv2
from pygame import mixer
from time import sleep

mixer.init()

cam = cv2.VideoCapture(0)

findface = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 

findeye = cv2.CascadeClassifier("haarcascade_eye.xml")

mixer.music.load("beepsound.mp3")

sec = 1

def findEye(img):
    global sec
    eyes = findeye.detectMultiScale(img, minNeighbors=2, scaleFactor= 1.1)
    #sleep(1)
    if len(eyes) > 0:
        print("Continue Driving!!")
        mixer.music.pause()
        sec = 0
    elif sec > 7:
        print("Wake up!!")
        mixer.music.unpause()
    else:
        sec+= 1
        
mixer.music.play()
while True:
    ret, img = cam.read()
    if not ret:
        break
    
    img = cv2.flip(img, 1)

    grey = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    faces = findface.detectMultiScale(grey, scaleFactor= 1.1, minNeighbors = 1)

    if len(faces) > 0:
        for (x,y,w,h) in faces:
            crop = img[y:y+h, x:x+w]
            findEye(crop)
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
            break

    cv2.imshow("Drowsiness Detector", img)
    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()
mixer.music.pause()

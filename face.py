import cv2

# Load pre-trained data on frontal face from opencv
trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Choose an image to detect faces
webcam = cv2.VideoCapture(0)

while True:

    success_frame_read, frame = webcam.read()
    grayscaled_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    face_coordinates=trained_face_data.detectMultiScale(grayscaled_img,scaleFactor=1.5,minNeighbors=5)
     
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h) , (0,255,0),10)
    cv2.imshow('Lokesh',frame)
    stop=cv2.waitKey(1)

    if stop==49:
        break



import cv2
import numpy as np
import paho.mqtt.client as mqtt

def on_publish(mosq, userdata, mid):
  # Disconnect after our message has been sent.
  mqtt.disconnect()

exit=False
#faceCascade = cv2.CascadeClassifier('/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')
faceCascade = cv2.CascadeClassifier('/home/jjparikh/w251/hw3/haarcascade_frontalface_default.xml')


#video_capture = cv2.VideoCapture(1, cv2.CAP_V4L)
video_capture = cv2.VideoCapture(1)
#ret, frame = video_capture.read()
#face = np.empty(frame.shape)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    #face = np.empty(frame.shape)
    #print(type(frame))
    #print(frame.shape)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = faceCascade.detectMultiScale(
               gray,
               scaleFactor=1.3,
               minNeighbors=5,
               minSize=(30, 30)
            )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)
        face = gray[y: y + h, x: x + w] 
        cv2.imwrite(str(w) + str(h) + '_faces.jpg', face)

        # Display the resulting frame
        cv2.imshow('Video', gray)

        rc,jpg = cv2.imencode('.jpg', face)
        msg = jpg.tobytes()

        # Specifying a client id here could lead to collisions if you have multiple
        # clients sending. Either generate a random id, or use:
        #client = mosquitto.Mosquitto()
        client = mqtt.Client("image-send")
        client.on_publish = on_publish
        client.connect("0.0.0.0")

        #f = open("./face.jpg")
        #imagestring = f.read()
        #byteArray = bytes(imagestring)

        client.publish("photo", msg ,0)

        k = cv2.waitKey(1)
        if k%256 == 27:
           # ESC pressed
           print("Escape hit, closing...")
           cv2.imwrite("face.jpg", face)
           exit=True
           break
       
       # elif k%256 == 32:
       #    SPACE pressed
       #    print("writing...")
       #    cv2.imwrite("face.jpg", face)

       #    client = mqtt.Client("image-send")
       #    client.on_publish = on_publish
       #    client.connect("0.0.0.0")

           #f = open("./face.jpg")
           #imagestring = f.read()
           #byteArray = bytes(imagestring)

       #    client.publish("photo", msg ,0)
           # If the image is large, just calling publish() won't guarantee that all 
           # of the message is sent. You should call one of the mosquitto.loop*()
           # functions to ensure that happens. loop_forever() does this for you in a
           # blocking call. It will automatically reconnect if disconnected by accident
           # and will return after we call disconnect() above.
           # client.loop_forevere)

    if exit:
       break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

from dotenv import load_dotenv
import thingspeak
import os
import cv2
from camera import FPS, WebcamVideoStream
from ultralytics import YOLO
from PIL import Image
import numpy as np
from threading import Thread

ip_address = '192.168.255.79:8080'
number_of_labels = 0
chn = None
def updateToThingSpeak():
    global number_of_labels, chn
    print(number_of_labels)
    if number_of_labels == 0:
        chn.update({
            'api_key': chn.api_key,
            'field1': 0
        })
    else:
        chn.update({
            'api_key': chn.api_key,
            'field1': 1
        })
def detect():
    global number_of_labels, chn
    onnx_model = YOLO(model = '../trained_model/train23/weights/best.onnx', task = 'detect')

    load_dotenv(dotenv_path=".env")
    CHANNEL_ID = os.getenv("CHANNEL_ID")
    API_WRITE_KEY = os.getenv("API_WRITE_KEY")
    urlCamera = f'rtsp://{ip_address}/h264_opus.sdp'
    vs = WebcamVideoStream(src = urlCamera).start()
    fps = FPS().start()
    chn = thingspeak.Channel(CHANNEL_ID, API_WRITE_KEY)
    while True:
        frame = vs.read()
        predicted = onnx_model(frame)
        for r in predicted:
            im_array = r.plot()  # plot a BGR numpy array of predictions
            im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
            labels = r.boxes.cls
        converted = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
        cv2.imshow('Predicted', converted)
        number_of_labels = len(labels)
        tsThread = Thread(target = updateToThingSpeak)
        tsThread.start()
        fps.update()
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
    fps.stop()
    cv2.destroyAllWindows()
    vs.stop()
if __name__ == '__main__':
    detect()
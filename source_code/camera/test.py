from dotenv import load_dotenv
import thingspeak
import os
import cv2
from camera import FPS, WebcamVideoStream
from ultralytics import YOLO
from PIL import Image
import numpy as np
from threading import Thread

ip_address = '192.168.166.5:8080'
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
    # onnx_model = YOLO(model = '../trained_model/train23/weights/best.onnx', task = 'detect')

    load_dotenv(dotenv_path=".env")
    CHANNEL_ID = os.getenv("CHANNEL_ID")
    API_WRITE_KEY = os.getenv("API_WRITE_KEY")
    chn = thingspeak.Channel(CHANNEL_ID, API_WRITE_KEY)
    img = cv2.imread('sample.png')
    while True:
        cv2.imshow('Sample', img)
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            number_of_labels = 1 - number_of_labels
            updateToThingSpeak()
        if (cv2.waitKey(1) & 0xFF) == ord('p'):
            break
if __name__ == '__main__':
    detect()
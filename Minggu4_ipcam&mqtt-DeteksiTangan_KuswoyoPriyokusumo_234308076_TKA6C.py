import cv2
import mediapipe as mp
import paho.mqtt.client as mqtt

mqttbroker = "mqtt-dashboard.com"
client = mqtt.Client()
client.connect(mqttbroker)
kirim = "tanganku"

cap = cv2.VideoCapture(0)
mphand = mp.solutions.hands
hands = mphand.Hands()
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        client.publish(kirim, "ada tangan")
        print("ada tangan")
    else:
        client.publish(kirim, "tidak ada tangan")
        print("tidak ada tangan")

    cv2.imshow("camera", img)
    cv2.waitKey(1)

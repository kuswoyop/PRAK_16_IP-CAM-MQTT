import paho.mqtt.client as mqtt
subscribe = "p16"
def on_message(client, userdata, msg):
    data=str(msg.payload.decode())
    print(data)
    return
client = mqtt.Client()
client.on_message = on_message
server = "mqtt-dashboard.com"
client.connect(server, 1883)
client.subscribe(subscribe)
while True:
    client.loop_start()
    client.loop_stop()

import json
import paho.mqtt.client as mqtt
BROKER = "broker.hivemq.com"
TOPIC = "iot/student/demo/dht22"
def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected:", reason_code)
    client.subscribe(TOPIC)
def on_message(client, userdata, message):
    print("Received:", json.loads(message.payload.decode()))
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, 1883)
client.loop_forever()

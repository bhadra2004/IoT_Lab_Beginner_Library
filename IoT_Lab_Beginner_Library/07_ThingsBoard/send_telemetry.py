import json, random, time
import paho.mqtt.client as mqtt
HOST="thingsboard.cloud"
TOKEN="YOUR_DEVICE_ACCESS_TOKEN"
c=mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
c.username_pw_set(TOKEN)
c.connect(HOST,1883)
c.loop_start()
while True:
    data={"temperature":round(random.uniform(27,32),2),"humidity":round(random.uniform(60,75),2)}
    c.publish("v1/devices/me/telemetry",json.dumps(data))
    print("Sent:",data)
    time.sleep(5)

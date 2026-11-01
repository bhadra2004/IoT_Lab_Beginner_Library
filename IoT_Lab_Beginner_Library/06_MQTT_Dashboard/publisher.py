import json, random, time
import paho.mqtt.client as mqtt
c = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
c.connect("broker.hivemq.com", 1883)
c.loop_start()
while True:
    data={"temperature":round(random.uniform(25,32),2),"humidity":round(random.uniform(50,80),2)}
    c.publish("iot/student/demo/dashboard",json.dumps(data))
    print(data)
    time.sleep(5)

import time
import paho.mqtt.client as mqtt
for broker, topic, value in [("broker.hivemq.com","iot/student/demo/temp","28.5"),("localhost","iot/student/demo/humidity","65.0")]:
    c=mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    c.connect(broker,1883);c.loop_start()
    c.publish(topic,value).wait_for_publish()
    print("Published",value,"to",broker)
    c.loop_stop();c.disconnect()

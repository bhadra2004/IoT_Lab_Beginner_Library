import paho.mqtt.client as mqtt
import threading
def listen(host,topic):
    c=mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    c.on_connect=lambda client,u,f,rc,p: client.subscribe(topic)
    c.on_message=lambda client,u,msg: print(host, msg.payload.decode())
    c.connect(host,1883);c.loop_forever()
for host,topic in [("broker.hivemq.com","iot/student/demo/temp"),("localhost","iot/student/demo/humidity")]:
    threading.Thread(target=listen,args=(host,topic),daemon=True).start()
input("Press Enter to stop... ")

import json, threading
from flask import Flask, render_template
import paho.mqtt.client as mqtt
app=Flask(__name__)
records=[]
def on_connect(c,u,f,rc,p): c.subscribe("iot/student/demo/dashboard")
def on_message(c,u,msg):
    records.append(json.loads(msg.payload.decode()))
    del records[:-10]
def listen():
    c=mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    c.on_connect=on_connect;c.on_message=on_message
    c.connect("broker.hivemq.com",1883);c.loop_forever()
threading.Thread(target=listen,daemon=True).start()
@app.get("/")
def home(): return render_template("dashboard.html",records=records[::-1])
if __name__=="__main__": app.run(debug=False)

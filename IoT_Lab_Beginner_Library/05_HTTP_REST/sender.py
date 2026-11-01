import random, time, requests
while True:
    data = {"temperature": round(random.uniform(27, 31), 2), "humidity": round(random.uniform(60, 75), 2)}
    print(requests.post("http://127.0.0.1:5000/api/sensor", json=data, timeout=10).json())
    time.sleep(5)

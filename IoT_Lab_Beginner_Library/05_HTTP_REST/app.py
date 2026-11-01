from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
readings = []
@app.get("/")
def home():
    return render_template("dashboard.html", readings=list(reversed(readings[-10:])))
@app.post("/api/sensor")
def sensor():
    data = request.get_json()
    reading = {"temperature": float(data["temperature"]), "humidity": float(data["humidity"])}
    readings.append(reading)
    return jsonify(status="saved", data=reading)
if __name__ == "__main__":
    app.run(debug=True)

# IoT Lab Beginner Library — Programs 1–18

These are **simplified teaching implementations** based on the uploaded 69-page lab manual, not exact copies. Each numbered folder contains runnable source files and its own README with steps.

## Getting started on Windows
1. Install Python 3.10+ and VS Code. Open this root folder in VS Code.
2. Open Terminal > New Terminal. Run: `py -m venv .venv`
3. Activate with `.venv\Scripts\activate` (PowerShell may require `Set-ExecutionPolicy -Scope Process Bypass`).
4. Run: `python -m pip install -r requirements.txt`
5. Enter the numbered program folder and follow its README.
6. For Programs 1–4, install Arduino IDE, ESP32 board support and required Arduino libraries (DHT sensor library and PubSubClient).

## Important notes
- Programs 5 and 6 use **local memory** instead of the Supabase cloud database in the manual.
- Programs 8 and 10 use a terminal client instead of a web dashboard; Program 14 uses a plot instead of a dashboard.
- Programs 11–14 require public APIs and internet access; API availability can change.
- Programs 15–17 require you to download datasets yourself from the URLs in their READMEs.
- Program 18 is a simplified browser simulator and optional four-LED ESP32 demo, not the manual's complete twelve-LED circuit.
- Do not commit passwords, API keys, or device tokens to public repositories.
- Public MQTT topics are shared; use a unique topic if you see other people's data.
- Arduino sketches must be opened from the matching `.ino` folder.

## Programs
- 01_DHT22: # Program 1: ESP32 DHT22 sensor
- 02_LDR: # Program 2: ESP32 light sensing
- 03_PIR: # Program 3: ESP32 motion detection
- 04_MQTT_ESP32: # Program 4: ESP32 MQTT publisher and Python subscriber
- 05_HTTP_REST: # Program 5: HTTP REST API and local dashboard
- 06_MQTT_Dashboard: # Program 6: MQTT publisher and Flask dashboard
- 07_ThingsBoard: # Program 7: ThingsBoard MQTT telemetry
- 08_CoAP: # Program 8: CoAP sensor server and client
- 09_HiveMQ_Mosquitto: # Program 9: Online and offline MQTT brokers
- 10_CoAP_Weather: # Program 10: CoAP weather and air quality API
- 11_ISS_Tracker: # Program 11: ISS tracking with CSV and graphs
- 12_Earthquake_Analysis: # Program 12: USGS earthquakes and visualization
- 13_Weather_Analysis: # Program 13: Open-Meteo temperature and humidity charts
- 14_Air_Quality: # Program 14: Kochi air quality analysis
- 15_Decision_Tree: # Program 15: Room occupancy decision tree
- 16_Linear_Regression: # Program 16: Temperature prediction with linear regression
- 17_Random_Forest: # Program 17: Air quality category classification
- 18_Smart_Traffic: # Program 18: Smart traffic signal simulation with emergency priority

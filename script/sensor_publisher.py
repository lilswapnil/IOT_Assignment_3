import paho.mqtt.client as mqtt
import random
import time
import socket

# ThingSpeak MQTT Configuration
MQTT_BROKER = "mqtt3.thingspeak.com"
MQTT_PORT = 1883
CHANNEL_ID = "2894369"  
WRITE_API_KEY = "SZMLPHQYAJU4XZFO"  
TOPIC = f"channels/{CHANNEL_ID}/publish/{WRITE_API_KEY}"

# Create MQTT client
client = mqtt.Client()

try:
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    print(f"Connected to {MQTT_BROKER}")
except socket.gaierror:
    print(f"Error: Could not resolve hostname '{MQTT_BROKER}'")
    print("Check your internet connection and DNS settings")
    exit(1)
except Exception as e:
    print(f"Connection error: {e}")
    exit(1)

while True:
    try:
        temperature = round(random.uniform(-50, 50), 2)
        humidity = round(random.uniform(0, 100), 2)
        co2 = random.randint(300, 2000)

        # Publish sensor values to ThingSpeak
        payload = f"field1={temperature}&field2={humidity}&field3={co2}"
        client.publish(TOPIC, payload)
        
        print(f"Published: {payload}")
        time.sleep(15) 
    except Exception as e:
        print(f"Error publishing: {e}")
        # Try to reconnect
        try:
            client.reconnect()
        except:
            print("Reconnection failed. Will retry in 15 seconds.")
        time.sleep(15)

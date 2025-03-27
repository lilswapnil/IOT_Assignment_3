import paho.mqtt.client as mqtt
import socket

# ThingSpeak MQTT Configuration
MQTT_BROKER = "mqtt3.thingspeak.com"  
MQTT_PORT = 1883
CHANNEL_ID = "2894369"
READ_API_KEY = "EO812OHAKC4XMUHU" 

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to all fields
    client.subscribe(f"channels/{CHANNEL_ID}/subscribe/fields/+/{READ_API_KEY}")

def on_message(client, userdata, message):
    print(f"Topic: {message.topic}")
    print(f"Received: {message.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Add error handling
try:
    print(f"Attempting to connect to {MQTT_BROKER}...")
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    print("Connected successfully!")
    client.loop_forever()
except socket.gaierror as e:
    print(f"DNS resolution error: {e}")
    print("Possible causes:")
    print("1. Check your internet connection")
    print("2. Verify the hostname is correct")
    print("3. Try using the IP address instead of hostname")
    
    # Try to ping to check connectivity
    print("\nAttempting to ping google.com to verify internet connectivity...")
    import os
    exit_code = os.system("ping -c 1 google.com > /dev/null 2>&1")
    if exit_code == 0:
        print("Internet connection appears to be working.")
    else:
        print("Internet connection may be down or restricted.")
except Exception as e:
    print(f"Connection error: {e}")

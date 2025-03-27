import requests
import random
import time
import json

# ThingSpeak credentials
THINGSPEAK_URL = 'https://api.thingspeak.com/update'
API_KEY = 'SZMLPHQYAJU4XZFO' 

while True:
    # Generate sensor data
    temperature = round(random.uniform(-50, 50), 2)
    humidity = round(random.uniform(0, 100), 2)
    co2 = random.randint(300, 2000)
    timestamp = time.time()
    
    # Prepare data payload
    payload = {
        'api_key': API_KEY,
        'field1': temperature,
        'field2': humidity,
        'field3': co2
    }
    
    # Send data to ThingSpeak
    try:
        response = requests.post(THINGSPEAK_URL, params=payload)
        if response.status_code == 200:
            print(f"Published: Temperature={temperature}, Humidity={humidity}, CO2={co2}")
        else:
            print(f"Failed to publish. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
    
    # ThingSpeak's free account has a minimum update interval of 15 seconds
    time.sleep(15)
Environmental Monitoring IoT System
Overview
This project implements an IoT-based environmental monitoring system that collects temperature, humidity, and CO₂ data from simulated sensors and transmits it to ThingSpeak for storage and visualization. The system demonstrates fundamental IoT concepts including data generation, MQTT/HTTP communication protocols, and cloud integration.

Features
Sensor Simulation: Generates realistic environmental data (temperature, humidity, CO₂)
Dual Communication Protocols: Supports both MQTT and HTTP
Real-time Data Visualization: Automatic graphing through ThingSpeak
Robust Error Handling: Comprehensive error detection and recovery
Modular Design: Easy to extend with physical sensors
Prerequisites
Python 3.6 or higher
Internet connection
ThingSpeak account
Installation
Clone the repository:

Install required dependencies:

ThingSpeak Setup:

Create a free account at ThingSpeak.com
Create a new channel with three fields:
Field 1: Temperature (°C)
Field 2: Humidity (%)
Field 3: CO₂ (ppm)
Note your Channel ID, Write API Key, and Read API Key
Configure the scripts:

Update the CHANNEL_ID, WRITE_API_KEY, and READ_API_KEY in the scripts with your ThingSpeak credentials
Usage
Publishing Sensor Data via MQTT
This script simulates temperature, humidity, and CO₂ readings, then publishes them to ThingSpeak using MQTT protocol.

Subscribing to Sensor Data via MQTT
This script connects to ThingSpeak and subscribes to the published sensor data, displaying it in the terminal.

Publishing Sensor Data via HTTP (Alternative)
This alternative script uses HTTP instead of MQTT to publish sensor data to ThingSpeak.

Project Structure
How It Works
System Architecture
Data Generation: The system simulates environmental data within realistic ranges
Data Transmission: Data is sent to ThingSpeak using either MQTT or HTTP
Data Storage: ThingSpeak stores the time-series data
Data Visualization: ThingSpeak automatically generates graphs for analysis
MQTT Communication Flow
Publisher connects to the ThingSpeak MQTT broker
Publisher sends data to a specific topic based on the channel ID and write API key
ThingSpeak processes and stores the data
Subscriber connects to the same broker and listens for updates
Subscriber receives published data through its subscription
ThingSpeak Channel Setup
Create Channel:

Go to Channels → New Channel
Enter channel name: "Environmental Monitoring"
Enable three fields: Temperature, Humidity, CO₂
Save Channel
Get API Keys:

Go to the API Keys tab
Note your Write API Key and Read API Key
Update these values in the Python scripts
View Data:

Go to your channel's Private View to see the graphs updating in real-time
Troubleshooting
MQTT Connection Issues
If you encounter "nodename not known" errors:

Verify the MQTT broker hostname (mqtt3.thingspeak.com)
Check your internet connection
Ensure your network allows MQTT traffic (port 1883)
Rate Limiting
ThingSpeak limits free accounts to one update every 15 seconds. The scripts already include this delay, but if you see errors like "rate limit exceeded":

Ensure you're respecting the 15-second minimum between updates
Consider using the bulk update API for multiple data points
Future Improvements
Physical Sensors: Integrate real sensors (DHT22, MQ-135) via Raspberry Pi or Arduino
Data Analytics: Implement anomaly detection and predictive analytics
Notifications: Add alert system for extreme environmental conditions
Local Storage: Implement edge computing and local caching during connectivity issues
Multi-location Monitoring: Scale to multiple sensor nodes in different locations
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
ThingSpeak for providing a free IoT analytics platform
The paho-mqtt project for the MQTT client library
For questions or support, please open an issue on the GitHub repository.


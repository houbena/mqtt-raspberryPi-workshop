# This Python script was written by Stefan Braicu for the Cisco IoT Workshop.
# This code gets data from Temperature/Humedity Sensor then sends it to a Online-Dashboard, as well as controlling a relay using RaspberryPi.

# Importing:
# Python library to control GPIO pins onRaspberryPi.
import RPi.GPIO as GPIO
# Python Library to communicate with "add the sensor model"
import dht11
# Import time
import time
# Import Paho library (Python library to communicate with the MQTT Broker)
import paho.mqtt.client as mqtt

# Enter you MQTT Broker details here.
mqtt_broker = "Enter your MQTT Broker address as a string here"
mqtt_broker_port = "Enter the port as a number here"

# initialize GPIO, First we stop the warnings which is a feature in this Python GPIO library.
GPIO.setwarnings(False)
# We also set the GPIO mode to BCM which is kind of standret RaspberryPi GPIO mapping scheme.
GPIO.setmode(GPIO.BCM)
# Funally we do a cleanup() this means that we set all GPIO pins to its default state.
GPIO.cleanup()

# Setting GPIO pin no. 14 as an output. 
GPIO.setup(14, GPIO.OUT)
# then we set it's state to one which equivalent to "OFF"
GPIO.output(14,1)

client = mqtt.Client()
# deifining on_message function that controls the GPIO pin to turn ON/OFF the light and prints received messages. 
def on_message(client, userdata, msg):
	if (msg.payload == "on"): 
		GPIO.output(14,0) 
	if (msg.payload == "off"): 
		GPIO.output(14,1)
	print(msg.payload)

# creating the MQTT client and establishing MQTT connection with the broker.
# paho Python Client - documentation: http://www.eclipse.org/paho/clients/python/docs/
client.on_message = on_message
client.connect(mqtt_broker, mqtt_broker_port, 60) 
client.subscribe("cisco/light")
client.loop_start()

# Reading data from the sensor.
instance = dht11.DHT11(pin = 4)
temperature = 0
humidity = 0
while True:
    result = instance.read()
    if result.is_valid():

	if (result.temperature != temperature):
		client.publish("cisco/t", result.temperature, qos=0, retain=True)
		temperature = result.temperature
	if (result.humidity != humidity):
		client.publish("cisco/h", result.humidity, qos=0, retain=True)
		humidity = result.humidity
	
	print("Temperature: %d C" % result.temperature)
	print("Humidity: %d %%" % result.humidity)
    time.sleep(1)
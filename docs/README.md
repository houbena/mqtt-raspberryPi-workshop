# MQTT and RaspberryPi

## What is our workshop about?
This workshop is about applying MQTT protocol to turn ON/OFF a light, and to get Temperature and Humidity data and view it on an online dashboard. 

## What is RaspberryPi?
RaspberryPi is an open-source, low cost computer on a chip, in other words it is a cheap and small computer.
The affordable price, the small size and the powerful hardware make RaspberryPi a perfect core for lots of IoT Projects.
You can find more about RaspberryPi [here](https://www.raspberrypi.org/)

## What is MQTT?
MQTT is a machine-to-machine (M2M)/"Internet of Things" connectivity protocol.
Further reading can be found [here](http://mqtt.org/)

## How we will do it?

The idea is to use a Dashboard to control light and to monitor the data received form the Temperature/Humidity sensor.
What really happens behind the scenes when we move the button on the dashboard, is that a function will be triggered to send an MQTT message with a specific topic, on the other hand the python code that runs on the RaspberryPi is connected  to the same MQTT Broker and subscribed to the same topic, and we have already specified in out code that if we received an MQTT message with "ON" we turn on the light (we send a signal to the relay that is connected to the RaspberryPi) and vice versa.

In the same way, the python script on the RaspberryPi is sending Temperature/Humidity as MQTT messages and the dashboard s connected  to the same MQTT Broker and subscribed to the same topic, and after receiving the messages, a function is responsible about converting these messages to a user-friendly gauge.

## How to run it?
After installing all the python packages needed and connecting the relay and the sensor properly, you can start run.py, then you have to put the dashboard code on a webserver (you can install a local webserver on you machine), and by visiting the dashboard page you can control the light and read the Temperature/Humidity data.

### Please make sure to refer to RaspberryPi GPIO layout, and sensor/rely data sheet (Google it!). Connections may differ due to different GPIO and sensor pins layouts.
# Home Automation IoT Project

## Martim Oliveira - mo223tz
An IoT Project focused on building a basic Home Monitoring System, using temperature and humidity sensor, obstacle sensor, and microphone sensor.  The chosen microcontroller was RPI Pi Pico W. The aim of the project is to test the use of this sensors in day-to-day. 


## Time Spent

- **Project Design** - 8 hours
- **Hardware Installation** - 1 hour
- **Software Development** - 6 hours
- **Testing** - 2 hours
- **Project Report** - 3 hours


## Objective 

The aim of this project is to try some sensors that might be implementede on several home automation solutions. The goal is to retrieve accurate information about air quality and temperature inside home, build an obstacle sensor for a automatic vaccum and use a microphone sensor to use inside a baby's room. The devices can help users to automate some utilities inside their houses, which can improve and help users on their daily routines. 

## Material

|  **Device**     |            **Description**           |      **Price/Store**          |
| --------------- | -------------------------------------|-------------------------------|          
|  Breadboard     | Connects the circuits                |  Kit 83.99€ / [Link](https://www.amazon.com/SunFounder-Raspberry-Beginners-Software-Engineer/dp/B093B9R6NL)  |
|  RPI Pi Pico W  | Microcontroller                      |  7.49€ / [Link](https://www.electrokit.com/en/raspberry-pi-pico-w) |
|  Jump Wires     | Connects RPI to sensors              |  Kit 83.99€ / [Link](https://www.amazon.com/SunFounder-Raspberry-Beginners-Software-Engineer/dp/B093B9R6NL)
|  Red Led        | Flashes red light                    |  Kit 83.99€ / [Link](https://www.amazon.com/SunFounder-Raspberry-Beginners-Software-Engineer/dp/B093B9R6NL)
|  1K Resistor    | Electrical resistance                |  Kit 83.99€ / [Link](https://www.amazon.com/SunFounder-Raspberry-Beginners-Software-Engineer/dp/B093B9R6NL)
|  KY-015         | Temp + Humidity Sensor               |  Kit 50.38€ / [Link](https://www.electrokit.com/en/sensor-kit-40-moduler)  |
|  KY-038         | Noise detection sensor               |  Kit 50.38€ / [Link](https://www.electrokit.com/en/sensor-kit-40-moduler)  |
|  KY-032         | Infra red obstacle detector          |  Kit 50.38€ / [Link](https://www.electrokit.com/en/sensor-kit-40-moduler)  |
|  KY-053         | Converts analog signal to digital    |  Kit 50.38€ / [Link](https://www.electrokit.com/en/sensor-kit-40-moduler)  |

## Computer setup

The chosen IDE was Thonny, which is a user-friendly IDE with Python built-in. [Download Thonny here](https://thonny.org/)
1. Download Thonny [Download](https://thonny.org/)
2. Connect RPI Pi Pico W to your computer (hold the button on the hardware) until you see the device appearing on your computer.
3. Download the latest Firmware to run MicroPython [Latest Firmware](https://micropython.org/download/RPI_PICO_W/)
4. Drag and Drop the Firmware onto RPI Pi Pico W.
5. Disconnect and Connect again (not holding the button) the RPI.

#### Thonny IDE
1. Open Thonny, click on View >> Files >> and open File manager panel
2. Click on Run >> Configure Interpreter

   ![Configure Interpreter](/HomeAutomation/Images/configInterp)
3. Click on Interpreter >> add Micropython as interpreter >> choose your RPI Port

   ![Choose RPI](/HomeAutomation/Images/chooseRPI)
4. You will see your board on the Shell. Try a print("Hello World") !

   ![Last Step](/HomeAutomation/Images/helloWorld)

## Putting everything together

   #### KY-015 (tempSensor)
      GND connected to GND on Raspberry.
      +V connected to Raspberry 3V3.
      Signal(S) connected to GP13 on Raspberry.
   #### KY-032 (obstacle_sensor)
      GND connected to GND on Raspberry.
      +V connected to RPI 3V3.
      Signal connected to GP18 on Raspberry.
   #### KY-038 (sound_sensor) + KY-053
      GND connected to GND on RPI.
      +V connected to Raspberry 3V3.
      Digital Signal(DO) to GP15 on RPI.
      Analog Signal(AO) to KY-053 AO.
   #### KY-053 
      VDD connected to 3V3 on RPI.
      GND connected to GND on Raspberry.
      SCL connected to GP01 on Raspberry.
      SDA connected to GPIO0 on Raspberry.

   #### Circuit Diagram hand drawn

   ![Circuit](/HomeAutomation/Images/circuit)

## Platform

For this project, I chose Adafruit as the platform due to its feature set, ease touse, and scalability. Adafruit, is a cloud-based solution which simplifies the process of receiving and sending data over IoT devices. Moreover, it provides intuitive dashboards for data visualization. 
Adafruit allows an easy creation and management of feeds, intuitive tools to custom dashboards, real-time data visualization, and it also has a comprehensive number of client libraries. 

## The Code

- machine module: interacts with hardware components.
- time: module to create time-related funtions.
- network module: manages network connectivity.
- umqtt.simple: MQTT communication.
- ADS1115: library used to interface with the ADS1115 analog-to-digital converter (ADC). 

```python
#MQTT Connection
mqtt_server = 'io.adafruit.com'
port = 1883
mqtt_username = 'your_username'
mqtt_key = 'your_mqtt_key'
mqtt_feed_temperature = 'your_user/feeds/picow.temperature'
mqtt_feed_humidity = 'your_user/feeds/picow.humidity'
mqtt_feed_obstacle = 'your_user/feeds/picow.obstacle'
mqtt_feed_sound_volt = 'your_user/feeds/picow.sound-voltage'
mqtt_feed_sound_analog = 'your_user/feeds/picow.sound-analog'
```

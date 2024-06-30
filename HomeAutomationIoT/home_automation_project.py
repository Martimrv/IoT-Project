import dht
import machine
from machine import Pin
import time
import network
from umqtt.simple import MQTTClient
import ADS1115

#Wi-Fi configuration
ssid = 'your_wifi'
password = 'wifi_password'

#wi-fi connection
station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

#Wait until the device is connected
while station.isconnected() == False:
    pass

print("Connection Successful")
print(station.ifconfig())

#MQTT Connection
mqtt_server = 'io.adafruit.com'
port = 1883
mqtt_username = 'your_username'
mqtt_key = 'your_mqtt_key'
mqtt_feed_temperature = 'your_username/feeds/picow.temperature'
mqtt_feed_humidity = 'your_username/feeds/picow.humidity'
mqtt_feed_obstacle = 'your_username/feeds/picow.obstacle'
mqtt_feed_sound_volt = 'your_username/feeds/picow.sound-voltage'
mqtt_feed_sound_analog = 'your_username/feeds/picow.sound-analog'

#Creats MQTT client instance and connect.
client = MQTTClient(mqtt_username, mqtt_server, port=port, user=mqtt_username, password=mqtt_key)
client.connect()

print("Connected to MQTT")

#ADC Input
ADS1115.init(0x48, 1, 4, False)

#Sensors Init
tempSensor = dht.DHT11(machine.Pin(13))
obstacle_sensor = Pin(18, Pin.IN, Pin.PULL_DOWN)
sound_sensor = Pin(15,Pin.IN,Pin.PULL_UP)
#Led
led = machine.Pin(14, Pin.OUT)

def read_obstacle_sensor():
    """
    Reads obstacle sensor data.
    
    :returns 0, if obstacle detected.
    """
    return obstacle_sensor.value()

def sound_detection_analog():
    """
    Reads Microphone sound sensor.
    
    :returns the analog value
    """
    analog_value = ADS1115.read(0)
    return analog_value

def sound_detection_volts():
    """
    Reads Microphone sound sensor.
    Converts the analog value to volts.
    
    :returns the volts value.
    """
    volt = ADS1115.raw_to_v(ADS1115.read(0))
    return volt

def blink_led(times, duration):
    """
    Output function to blink led.
    
    :param times - used to determine the number of times the led blinks.
    :param duration - time that led will pause.
    
    """
    for i in range(times):
        led.on()
        time.sleep(duration)
        led.off()
        time.sleep(duration)

def read_publish():
    """
    Reads each sensor data and publishes it to MQTT.
    Checks if obstacle is detected, and blinks led.
    Checks some temperature limits and blinks led as a warning.
    """
    obstacle_status = read_obstacle_sensor()
    
    if obstacle_status == 0:
        client.publish(mqtt_feed_obstacle, "Obstacle detected")
        print("Obstacle detected")
        blink_led(4, 0.5)
    else:
        client.publish(mqtt_feed_obstacle, "No obstacle detected")
        print("There is no obstacles")

    # Temperature Information
    tempSensor.measure()
    temperature = tempSensor.temperature()
    humidity = tempSensor.humidity()
    client.publish(mqtt_feed_temperature, str(temperature))
    print(f"Published Temperature value: {temperature}ºC")
    #Humidity        
    client.publish(mqtt_feed_humidity, str(humidity))
    print(f"Published Humidity value: {humidity}%")
    
    #Sound Information
    sound_volts = sound_detection_volts()
    sound_analog = sound_detection_analog()
    digital_value = sound_sensor.value()
    client.publish(mqtt_feed_sound_volt, str(sound_volts))
    print(f"Analog voltage value: " + str(sound_volts) + " V")
    client.publish(mqtt_feed_sound_analog, str(sound_analog))
    print(f"Analog value: " + str(sound_analog))
    
    #Alert conditions
    if temperature > 26 or temperature < 12:
        blink_led(3, 0.5)
    else:
        led.off()
        
# Infinite loop
# Calls read_publish() to retrieve the data and publish it.
# Pauses for 10s.
try:
    while True:
        read_publish()
        time.sleep(10)
except KeyboardInterrupt:
    pass

client.disconnect()





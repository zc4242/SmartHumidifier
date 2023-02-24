from wireless import connect
import dht
import time
from update import update
from machine import Pin

led = Pin('LED', Pin.OUT)

wlan = connect()
while True:
    if not wlan.isconnected():  # reconnect if not connected
        print('lost connection')
        wlan = connect()
    try:
        led.on()
        sensor = dht.DHT22(Pin(2))
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Temperature: {}°C   Humidity: {:.0f}% ".format(temp, hum))
        update(temp, hum)
        time.sleep(15)
    except:
        for i in range(4):
            time.sleep(0.5)
            led.toggle()
        led.off()

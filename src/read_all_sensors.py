"""
Read temperature, humidity, and light from the Enviro Mini pHAT and print the values.
"""

from enviroplus import weather, light

def read_temperature():
    return weather.temperature

def read_humidity():
    return weather.humidity

def read_light():
    return light.light()

if __name__ == "__main__":
    temp = read_temperature()
    humidity = read_humidity()
    lux = read_light()
    print(f"Temperature: {temp:.2f} °C")
    print(f"Humidity: {humidity:.2f} %")
    print(f"Light: {lux:.2f} Lux")

"""
Read humidity from the Enviro Mini pHAT and print the value.
"""

from enviroplus import weather

def read_humidity():
    """Returns the current humidity percentage."""
    return weather.humidity

if __name__ == "__main__":
    humidity = read_humidity()
    print(f"Humidity: {humidity:.2f} %")

"""
Read temperature from the Enviro Mini pHAT and print the value.
"""

from enviroplus import weather

def read_temperature():
    """Returns the current temperature in Celsius."""
    return weather.temperature

if __name__ == "__main__":
    temp = read_temperature()
    print(f"Temperature: {temp:.2f} °C")

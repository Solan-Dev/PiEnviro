"""
Read light level from the Enviro Mini pHAT and print the value.
"""

from enviroplus import light

def read_light():
    """Returns the current light level in Lux."""
    return light.light()

if __name__ == "__main__":
    lux = read_light()
    print(f"Light: {lux:.2f} Lux")

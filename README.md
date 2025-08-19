
## Raspberry Pi Setup

### Recommended OS
- **Raspberry Pi OS Lite (32-bit)** is recommended for the Raspberry Pi Zero W v1. Download from: https://www.raspberrypi.com/software/operating-systems/

### Setup Steps
1. **Flash Raspberry Pi OS Lite to SD card**
   - Use the [Raspberry Pi Imager](https://www.raspberrypi.com/software/) to write Raspberry Pi OS Lite (32-bit) to your microSD card.
2. **Boot and connect to WiFi**
   - Insert the SD card, power on the Pi, and connect to your WiFi network.
3. **Enable SSH (optional but recommended)**
   - Place an empty file named `ssh` (no extension) in the boot partition of the SD card before first boot, or enable via `sudo raspi-config` > Interfacing Options > SSH.
4. **Enable I2C and SPI interfaces**
   - Run `sudo raspi-config` > Interface Options > I2C and SPI > Enable both.
5. **Update the system**
   ```sh
   sudo apt update && sudo apt upgrade -y
   ```
6. **Install Python and pip**
   ```sh
   sudo apt install python3 python3-pip git
   ```
7. **Clone this repository**
   ```sh
   git clone https://github.com/Solan-Dev/PiEnviro.git
   cd PiEnviro
   ```
8. **Install Python dependencies**
   ```sh
   pip3 install enviroplus
   pip3 install -r requirements.txt
   ```
9. **Attach the Enviro Mini pHAT**
   - Carefully connect the Enviro Mini pHAT to the Pi’s GPIO header.
10. **Test sensor scripts**
   ```sh
   python3 src/read_all_sensors.py
   ```

## Project Setup (Development)

1. **Hardware**
   - Raspberry Pi Zero W v1
   - Pimoroni Enviro Mini pHAT

2. **Prepare the Pi**
   - See Raspberry Pi Setup section above.

3. **Install dependencies**
   ```sh
   pip3 install enviroplus
   pip3 install -r requirements.txt
   ```

4. **Run the sensor script**
   ```sh
   python3 src/read_sensors.py
   ```

5. **Integrate with Home Assistant**
   - Configure Home Assistant to receive sensor data (see `homeassistant/integration.md`).
   - Attach Enviro HAT.

3. **Install dependencies**
   ```sh
   sudo apt update
   sudo apt install python3 python3-pip
   pip3 install -r requirements.txt
   ```

4. **Run the main script**
   ```sh
   python3 src/main.py
   ```

5. **Integrate with Home Assistant**
   - Configure Home Assistant to receive sensor data (see `homeassistant/integration.md`).

## Documentation
- [Setup instructions](docs/setup.md)
- [DevOps process](devops/process.md)
- [Epics, features, and user stories](devops/epics-features-stories.md)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENSE)

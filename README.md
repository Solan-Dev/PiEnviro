# PiEnviro

A Raspberry Pi Zero W v1 project using the Pimoroni Enviro HAT to record temperature, humidity, and light, with integration to Home Assistant.

## Project Goals
- Collect temperature, humidity, and light data using the Enviro HAT.
- Send sensor data to Home Assistant for automation and monitoring.
- Document the development and DevOps process.

## Features
- Read temperature, humidity, and light from Enviro HAT sensors.
- Log or display sensor data.
- Transmit sensor data to Home Assistant (via MQTT or REST API).

## Epics & User Stories
See [`devops/epics-features-stories.md`](devops/epics-features-stories.md) for detailed epics, features, and user stories.

## Setup

1. **Hardware**
   - Raspberry Pi Zero W v1
   - Pimoroni Enviro HAT

2. **Prepare the Pi**
   - Flash Raspberry Pi OS Lite to SD card.
   - Boot and connect to WiFi.
   - Enable I2C and SPI via `raspi-config`.
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

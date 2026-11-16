# The Dawgs — AI-Powered mmWave Radar Detection System

> **IT 254 Group Project | Status: In development**

## Project Overview

The Dawgs are developing a Raspberry Pi 5–based radar sensing system using an **HLK-LD2450 24 GHz mmWave sensor** and an AI model. The project's goals are to distinguish between human and pet detections, identify potential falls, and provide appropriate alerts.

The team is experimenting with a **Closed-Form Continuous-Time (CfC) neural network** rather than a LiquidAI LFM, with the aim of using Raspberry Pi resources efficiently. These detection and alert capabilities are **project goals, not yet demonstrated completed features** in the project notes.

## Project Goals

- Collect radar sensor readings using a Raspberry Pi 5.
- Convert raw hexadecimal sensor output into readable information.
- Present detected-object location data in a clear format.
- Collect training data for an AI model.
- Develop a model to distinguish people from pets.
- Explore fall detection and corresponding alerts.

## Hardware

| Component | Purpose / status |
| --- | --- |
| Raspberry Pi 5 | Main computing platform |
| HLK-LD2450 24 GHz mmWave radar sensor | Radar sensing and target data |
| Display | Planned output interface |
| Arduino | Listed in the initial hardware plan; specific role not yet documented |
| Custom 3D-printed sensor stand | Holds the HLK-LD2450 upright |

### Radar-to-Raspberry Pi 5 wiring

The following wiring is recorded in the project notes:

| HLK-LD2450 pin | Function | Raspberry Pi 5 connection | Physical pin |
| --- | --- | --- | --- |
| 5V | Power | 5V | 2 or 4 |
| GND | Ground | GND | 6, 9, 14, or 20 |
| TX | Sensor transmit | GPIO 15 (RXD) | 10 |
| RX | Sensor receive | GPIO 14 (TXD) | 8 |

**Important:** Power down the Raspberry Pi before making wiring changes. Verify the sensor's electrical requirements and UART signal levels against the hardware documentation before connecting it.

## Software and Tools

The team has used or explored:

- **Python scripts** for sensor connectivity checks, readable radar output, and training-data collection.
- **PyTorch (`torch`)** for AI development.
- **CfC neural networks** as the selected model direction.
- **Homebrew and llama** during model/runtime exploration.
- **Ollama**, which was installed and subsequently uninstalled.
- **`i2c-tools`**, installed during early setup.

The project notes do not provide a complete dependency list, the source scripts, or confirmed commands for running the final system.

## Initial Setup and Testing

The team documented the following commands:

```bash
sudo apt install i2c-tools
i2cdetect -y 1
```

These are **I²C diagnostic commands**, not commands for reading the HLK-LD2450's UART data. The sensor wiring documented above uses TX/RX serial communication.

### Sensor data workflow

1. Connect the HLK-LD2450 to the Raspberry Pi using the documented pin mapping.
2. Verify communication between the radar and the Pi.
3. Use a Python script to turn the raw hexadecimal output into readable sensor data.
4. Refine the display of detected-object locations.
5. Run a data-collection script to gather examples for model training.
6. Use the collected data in future AI training and validation.

**Note:** These are documented development activities, not a verified end-to-end installation or usage procedure. Add the actual script filenames and invocation commands once they are available.

## Development Progress

### First Group Meeting: Aaron Bestler (myself), Jack Curless, Owen McGrath (due to other commitments Uriah was not able to attend and because of us texting the wrong phone number John was not present) 

- Tested connectivity between the HLK-LD2450 and Raspberry Pi.
- Created an initial sensor communication verification script with AI assistance.
- Developed a script to convert hexadecimal readings into human-readable output.
- Iterated through four versions to improve clarity and conciseness.

### Second Group Meeting: Aaron Bestler (myself), Jack Curless, Owen McGrath, John (Uriah had a scheduling conflict but he delivered the sensor stand displayed below to the group) 

- Installed and later removed Ollama.
- Installed Homebrew and llama while exploring local AI tools.
- Selected a CfC network approach instead of LiquidAI LFM models, based on expected resource efficiency.
- Installed PyTorch and tested an initial AI script.
- Improved how object locations were presented for demonstrations.
- Created a sensor-data collection script for future AI training.
- Found that the first collection attempt produced no data because of a wiring issue.
- Corrected the sensor connections and ran two further collection iterations.

**Current documented milestone:** Sensor connectivity and readable output have been tested; the team has begun collecting data for AI development. The notes do not yet report model accuracy, successful pet/human classification, or fall-detection results.

## Sensor Stand

A team member designed a **3D-printed stand** to hold the HLK-LD2450 upright. The project document includes photographs of the stand and a sensor dimension diagram.

The notes mention a sensor body diagram of approximately **40 mm × 15 mm**, as well as a proposed stand-related measurement of **45 mm tall × 20 mm wide** and a slot thickness of at least **2 mm**. These stand measurements were recorded as questions and should be verified against the final design before fabrication.

To include the images in this README, add them to the repository (for example, under `images/`) and link them here.

## Team

The project notes identify the following contributors:

- Aaron 
- Jack 
- Owen 
- John 
- Uriah 

## Documentation Notes

This README describes the documented design and development progress, rather than claiming that unfinished features are operational. Source code, full installation steps, training results, and a final license were not included in the supplied document.

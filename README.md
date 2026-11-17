# The Dawgs — AI-Powered mmWave Radar Detection System

> **IT 254 Group Project | Status: In development**

## Project Overview

The Dawgs are developing a Raspberry Pi 5–based radar sensing system using an **HLK-LD2450 24 GHz mmWave sensor** and an AI model. The project's goals are to identify if a human is running, walking, falling, or crawling and then have AI provide appropriate alerts.

The team is experimenting with a **Closed-Form Continuous-Time (CfC) neural network** rather than a LiquidAI LFM, with the aim of using Raspberry Pi resources efficiently. These detection and alert capabilities are **project goals, not yet demonstrated completed features** in the project notes.

## Project Goals

- Collect radar sensor readings using a Raspberry Pi 5.
- Convert raw hexadecimal sensor output into readable information.
- Present detected-object location data in a clear format.
- Collect training data for an AI model.
- Develop a model to distinguish human movements.
- Explore AI corresponding alerts.

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

## Software and Tools

The team has used or explored:

- **Python scripts** for sensor connectivity checks, readable radar output, and training-data collection.
- **PyTorch (`torch`)** for AI development.
- **CfC neural networks** as the selected model direction.
- **Homebrew and llama** during model/runtime exploration.
- **Ollama**, which was installed and subsequently uninstalled.
- **`i2c-tools`**, installed during early setup.

## Initial Setup and Testing

The team documented the following commands:

```bash
sudo apt install i2c-tools
i2cdetect -y 1
```

## Development Progress
Pre First Meeting: Aaron Bestler (myself), Jack Curless, Owen McGrath, Jon Hubal, Uriah Blair

- Discussed ideas for the project 
- Jack ordered the HLK-LD2450 
- Uriah researched the cable connections for the sensor and PI

First Group Meeting (10/24): Aaron Bestler (myself), Jack Curless, Owen McGrath (due to other commitments Uriah was not able to attend and because of us texting the wrong phone number Jon was not present) 

- Tested Connectivity to the HLK-LD2450. 
- Had Gemini create a script to verify the connectivity from the HLK with the PI
- After successfully verifying the connectivity to the PI, we had Gemini create a script to make the data human readable as otherwise its just outputted in hexadecimal values 
- Initial script was good for a start
- Went through 4 different variations of the script until arriving at one that presented the information in most concise and easy readable format
- Concluded first meeting 

Second Group Meeting (11/3): Aaron Bestler (myself), Jack Curless, Owen McGrath, Jon Hubal (Uriah had a scheduling conflict but he delivered the sensor stand displayed below to the group) 

- Connected the sensor to the Raspberry Pi 5
- Researched how to install LiquidAI on the Pi
- Found Ollama during research and installed Ollama
- Uninstalled Ollama after further research and concluding it wasn't what we needed 
- During further research landed on llama so we installed Homebrew to install llama
- Installed llama
- Using Closed-Form Continuous Time (CfC) network instead of LiquidAI LFM models because it is a more efficient use of resources
- Installed torch
- Tested first AI script
- Tweaked some parts of the AI script to make the location of the object more understandable and presentable for demo (around this point John and Owen had to leave)
- Used AI to create script that allows the sensor to collect data that the AI on the PI will be trained on
- Ran one iteration of the training data script. Ran into a problem and actually collected 0 data. Turned out the sensor connections to the PI had been messed up
- After fixing the cabling problem with the sensor, ran two iterations of the training data script
- Concluded this meeting

## Sensor Stand

A team member designed a **3D-printed stand** to hold the HLK-LD2450 upright. The project document includes photographs of the stand and a sensor dimension diagram.

The notes mention a sensor body diagram of approximately **40 mm × 15 mm**, as well as a proposed stand-related measurement of **45 mm tall × 20 mm wide** and a slot thickness of at least **2 mm**. These stand measurements were recorded as questions and should be verified against the final design before fabrication.

To include the images in this README, add them to the repository (for example, under `images/`) and link them here.

## Team

The project notes identify the following contributors:

- Aaron Bestler 
- Jack Curless
- Owen McGrath
- Jon Hubal
- Uriah Blair

## Documentation Notes

This README was created with the assistance of ChatGPT. It describes the documented design and development progress, rather than claiming that unfinished features are operational. Source code, full installation steps, training results, and a final license were not included in the supplied document.

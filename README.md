# Home Security using autoencoders and sensors

## Introduction

This project focuses on using artificial intelligence techniques to detect anomalies in sensor data. Specifically, it involves reading data from an HC-SR312 presence sensor connected to a Raspberry Pi, which logs each time someone passes by. The collected data is stored over a period and accessed through a simple Apache server. The data is then used to train an autoencoder, which is employed to detect anomalies in access patterns to the house. This work is both an exploration of machine learning methods and an application of hardware-software integration, showcasing the potential of AI in IoT environments.

## Materials Used

- Raspberry Pi 4 Model B: The core hardware platform for connecting and managing sensors.

- HC-SR312 Presence Sensor: Connected to the GPIO pin 17 for data collection.

![materials](img/raspberry.png)

## Steps

- Connect the sensor to the Raspberry Pi, create the motion.py program, and configure _crontab_ to launch it each time the Raspberry Pi starts.

- Wait for the sensor to collect data. The collected data can be accessed through a web interface using the Raspberry Pi's local IP address. (now here)

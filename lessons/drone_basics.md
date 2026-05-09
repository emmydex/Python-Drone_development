# Lesson 1: Drone Basics 🚁

## Objective
Understand the basic components of a drone and how drone programming works at a high level.

---

## What is a Drone?

A drone is an unmanned aerial vehicle (UAV) that can fly using onboard systems and software control.

Modern drones combine:
- hardware
- sensors
- firmware
- software
- communication systems

to perform autonomous or manual flight operations.

---

## Core Drone Components

### 1. Flight Controller
The flight controller is the brain of the drone.

Responsibilities:
- stabilizes the drone
- processes sensor data
- controls motor speed
- executes flight commands

Examples:
- Pixhawk
- DJI flight controllers

Common firmware:
- PX4
- ArduPilot

---

### 2. Motors and ESCs

#### Motors
Provide thrust for flight.

#### ESC (Electronic Speed Controller)
Controls motor speed based on commands from the flight controller.

---

### 3. Sensors

Drones use sensors to understand their environment and movement.

Common sensors:
- GPS → location tracking
- IMU → orientation and acceleration
- Barometer → altitude estimation
- Compass → heading direction

---

### 4. Battery
Provides electrical power to the drone system.

Most drones use lithium polymer (LiPo) batteries.

---

### 5. Communication System

Allows communication between:
- drone
- ground station
- software applications

Common communication protocol:
- MAVLink

---

## What is Drone Programming?

Drone programming means writing software that controls drone behavior.

Examples:
- takeoff
- landing
- waypoint navigation
- object tracking
- autonomous missions

Programming languages commonly used:
- Python
- C++

---

## High-Level vs Low-Level Programming

### High-Level Programming
Used for:
- automation scripts
- mission planning
- AI systems

Language:
- Python

Example:
```python
takeoff()
move_forward()
land()
```

---

### Low-Level Programming
Used for:
- firmware modification
- motor control
- sensor drivers

Language:
- C++

---

## How Drone Communication Works

Python scripts communicate with drones using MAVLink.

Workflow:
```text
Python Script → MAVLink → Flight Controller → Drone Movement
```

Example:
```text
Takeoff Command → Flight Controller → Motors Spin → Drone Lifts
```

---

## Drone Simulation

Before using a real drones, useing  simulators seemed practical.

Advantages:
- safer
- cheaper
- easier debugging
- no hardware damage risk

Simulator used:
- AirSim

---

## Key Concepts Learned

- A drone is a programmable flying robot.
- The flight controller acts as the drone's brain.
- Sensors provide environmental awareness.
- Python can automate drone missions.
- MAVLink enables communication with the drone.
- Simulators allow safe testing and development.

---

## Current Learning Stage

Completed:
- Drone architecture basics
- Understanding drone software 
- AirSim setup

Next:
- First autonomous drone mission
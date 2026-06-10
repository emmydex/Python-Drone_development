# Drone Programming Path 🚁

A hands-on drone programming journey focused on autonomous UAV development using Python, AirSim, telemetry systems, waypoint navigation, and intelligent flight behavior.

This repository documents my progression from beginner-level drone control to advanced autonomous drone systems.

---

# 🎯 Project Goals

This project is focused on learning:

- Drone programming fundamentals
- Autonomous flight systems
- Telemetry monitoring
- Waypoint navigation
- Real-time decision-making
- Robotics programming concepts
- UAV software engineering workflows

Long-term goals include:
- MAVLink communication
- ROS integration
- Computer vision for drones
- AI-powered navigation
- Multi-drone systems
- PX4/ArduPilot development

---

# 🛠️ Technologies Used

- Python 3.11
- AirSim
- Unreal Engine 5
- NumPy
- msgpack-rpc-python
- Git & GitHub

---

# 📚 Learning Progress

## Module 1 — Drone Basics ✅

- AirSim setup
- First drone connection
- Basic drone control
- Takeoff and landing
- Hover stabilization

---

## Module 2 — Drone Movement ✅

- Velocity-based movement
- Position-based movement
- Yaw rotation
- Coordinate systems
- Local vs world movement

---

## Module 3 — Telemetry & Monitoring ✅

- Reading drone telemetry
- Position tracking
- Altitude monitoring
- Autonomous correction systems
- Continuous feedback loops

---

## Module 4 — Autonomous Navigation ✅

- Waypoint navigation
- Waypoint loops
- Triangle and square missions
- Patrol-style movement
- Autonomous route execution

---

## Module 5 — Autonomous Decision Systems 🚧

Currently learning:
- Continuous monitoring systems
- Reactive drone behavior
- Telemetry-driven decisions
- Autonomous mission logic

Upcoming:
- Dynamic mission systems
- Obstacle avoidance
- Autonomous patrol AI

---

# 📂 Repository Structure

```text
Drone-Programming-Path/
│
├── challenge/
│   ├── drone_logger.py
│   ├── square_pattern.py
│   ├── triangle_waypoint_loop.py
│   ├── yaw_challenge.py
│   
├── lessons/
│   ├── Airsim_Setup.md
│   ├── drone_basics.md
│   ├── square_flight.md
│   ├── first_flight.md
│   ├── drone_movement.md
│   ├── yaw_control.md
│   ├── telemetry.md
│   ├── waypoint_loops.md
│   ├── continuous_monitoring.md
│
├── projects/
│   ├── autonomous_patrol_drone/
│   ├── mission_logger_drone/
│   ├── obstacle_avoidance_drone/
│   ├── telemetry_dashboard/
│   ├── return_to_home_system/
│   
├── screenshots/
├── scripts/
│   ├── first_flight.py
│   ├── drone_movement.py
│   ├── yaw_control.py
│   ├── telemetry.py
│   ├── waypoint_navigation.py
│   ├── waypoint_loop.py
│   ├── autonomous_decision.py
│   ├── continuous_monitoring.py
│
├── drone_logger.txt
├── flight_log.txt
├── setup_notes.md
├── README.md
└── .gitignore
```

---

# 🚀 Key Concepts Learned

## Velocity vs Position Control

### Velocity Control

```python
moveByVelocityAsync()
```

Focuses on:
```text
speed + duration
```

---

### Position Control

```python
moveToPositionAsync()
```

Focuses on:
```text
destination coordinates
```

---

## NED Coordinate System

AirSim uses:

```text
North
East
Down
```

Important observation:

```text
more negative Z = higher altitude
```

Examples:

| Z Value | Physical Height |
|---|---|
| 0 | ground |
| -5 | low altitude |
| -10 | higher altitude |
| -15 | even higher altitude |

---

## Autonomous Feedback Loops

The drone continuously:

```text
move
observe
decide
correct
repeat
```

This introduced:
- feedback systems
- reactive autonomy
- real-time monitoring

---

# 🧪 Engineering Observations

Some important discoveries during testing:

| Observation | Result |
|---|---|
| `time.sleep(0.5)` before landing | unstable landing |
| `time.sleep(2)` before landing | stable landing |
| negative yaw rotation | anticlockwise rotation |
| yaw rotation does not change world-axis movement | movement still follows global coordinates |

---

# 🛰️ Current Capabilities

The drone can currently:

✅ Take off and land  
✅ Hover and stabilize  
✅ Move using velocity control  
✅ Navigate to coordinates  
✅ Rotate using yaw control  
✅ Read telemetry data  
✅ Follow waypoint missions  
✅ Execute looped patrol routes  
✅ Perform autonomous altitude correction  
✅ Continuously monitor flight state  

---

# 📈 Future Learning Roadmap

Planned learning milestones:

- MAVLink protocol
- DroneKit
- PX4 firmware
- ROS integration
- Sensor fusion
- Computer vision
- AI object detection
- Reinforcement learning
- Swarm drones
- Real drone deployment

---

# 🧠 Learning Philosophy

This repository focuses on:
- hands-on experimentation
- engineering observations
- iterative testing
- debugging practice
- understanding drone behavior deeply

The goal is not only to run code, but to understand:
```text
how autonomous drone systems think and behave
```

---

# 🚁 Current Status

✅ AirSim operational  
✅ Drone control functional  
✅ Autonomous waypoint missions working  
✅ Telemetry systems integrated  
✅ Continuous monitoring implemented  
🚧 Expanding into intelligent autonomous systems  

---

# 📌 Notes

This repository is part of a long-term learning path toward becoming a drone software developer focused on:
- autonomous UAV systems
- robotics programming
- AI-driven drones
- intelligent flight software

---

## Goals

My goal is to become a drone software developer focused on:
- autonomous systems
- AI drone applications
- drone automation
- robotics programming

---

## Author
olúwáfẹ́mi🍀

Learning and building step-by-step 🚀
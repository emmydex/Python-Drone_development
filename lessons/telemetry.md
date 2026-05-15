# Drone Telemetry Monitoring 🚁

## Objective
Learning how to read and analyze real-time telemetry data from a drone using AirSim.

This lesson introduces:
- drone state monitoring
- telemetry systems
- live position tracking
- velocity analysis
- real-time UAV feedback

---

## Mission Goals

The drone should:
1. Connect to AirSim
2. Take off
3. Reach flight altitude
4. Move forward
5. Move right
6. Read live telemetry data
7. Display position and velocity values
8. Land safely

---

## Technologies Used

- Python 3.11
- AirSim
- NumPy
- msgpack-rpc-python

---

## Script File

```text
scripts/drone_telemetry.py
```


---

## What is Telemetry?

Telemetry means:
```text
data sent from the drone
```

The drone continuously reports information about itself.

Examples:
- position
- speed
- altitude
- orientation

---

## Important Telemetry Command

```python
state = client.getMultirotorState()
```

Meaning:
```text
request the drone's current state information
```

---

## Position Data

```python
position = state.kinematics_estimated.position
```

This provides:
```text
X position
Y position
Z position
```

---

## Velocity Data

```python
velocity = state.kinematics_estimated.linear_velocity
```

This provides:
```text
movement speed in each direction
```

---

## Coordinate System

```text
X = forward/backward
Y = left/right
Z = altitude
```

---

## Important Observations During Testing

### Forward Movement Observation

Telemetry values showed:

```text
x position increasing
```

Meaning:
- the drone moved forward successfully

---

### Right Movement Observation

Telemetry values showed:

```text
y velocity increasing
```

Example:
```text
y velocity: 4.79
```

Meaning:
- the drone was actively moving right

This correctly matched the movement command:

```python
client.moveByVelocityAsync(0, 5, 0, 3)
```

---

### Hover Stabilization Observation

During hover:
```text
velocity values moved closer to 0
```

Meaning:
- the drone stabilized itself
- movement momentum reduced

---

### Altitude Observation

Example:
```text
z position: -22.xx
```

Meaning:
- the drone climbed upward successfully

AirSim uses:
```text
negative Z values for upward altitude
```

---

## Important Lessons Learned

- Telemetry allows software to monitor drone behavior.
- Position data tracks where the drone is.
- Velocity data tracks how fast the drone moves.
- Telemetry updates in real time during flight.
- Autonomous systems rely heavily on telemetry feedback.

---

## Engineering Concepts Introduced

- telemetry systems
- state estimation
- real-time monitoring
- velocity analysis
- autonomous feedback systems

---

## Commands Used

Run script:
```bash
python scripts/drone_telemetry.py
```

---

## Current Status

✅ Real-time telemetry successful  
✅ Position tracking successful  
✅ Velocity monitoring successful  
✅ Forward movement telemetry validated  
✅ Right movement telemetry validated  
✅ Hover stabilization observed  

---

## Next Learning Goals

- waypoint navigation
- autonomous path planning
- local-frame movement
- drone orientation tracking
- MAVLink communication
- real-time drone dashboards
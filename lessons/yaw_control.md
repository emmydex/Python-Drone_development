# Yaw Control 🚁

## Objective
Learning how to rotate a drone using yaw commands and understand how orientation affects navigation.

This lesson introduced me to:
- yaw rotation
- heading control
- orientation systems
- world vs local coordinate frames

---

## Mission Goals

The drone should:
1. Connect to AirSim
2. Take off
3. Reach flight altitude
4. Rotate using yaw commands
5. Move after rotation
6. Rotate again
7. Move again
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
scripts/yaw_control.py
```

---


## Understanding Yaw

Yaw means:
```text
rotating left or right
```

Yaw changes the direction the drone faces.

---

## Drone Rotation Axes

Drones rotate on three axes:

```text
Roll  = tilt left/right
Pitch = tilt forward/backward
Yaw   = rotate left/right
```

---

## Yaw Command

```python
client.rotateToYawAsync(90)
```

Meaning:
- rotate drone to 90 degrees

---

## Rotation Direction Observations

### Positive Yaw

```python
client.rotateToYawAsync(90)
```

Result:
```text
clockwise rotation
```

---

### Negative Yaw

```python
client.rotateToYawAsync(-90)
```

Result:
```text
anticlockwise rotation
```

---

## Angle Direction System

```text
0°    = forward
90°   = right
180°  = backward
-90°  = left
```

---

## Important Discovery: World Coordinates

An important observation i made  during testing.

After rotating the drone:
```python
client.rotateToYawAsync(90)
```

the movement command:

```python
client.moveByVelocityAsync(5, 0, 0, 3)
```

still moved along the original global X direction.

---

## What This Means

`moveByVelocityAsync()` uses:
```text
world coordinates
```

NOT:
```text
drone local coordinates
```

---

## Coordinate Frame Concepts

### World Coordinates
Fixed directions in the environment.

Example:
```text
North/South/East/West
```

These directions do not change when the drone rotates.

---

### Local (Body) Coordinates
Movement relative to the drone's current facing direction.

Example:
```text
forward = wherever the drone is facing
```

This was the expected behavior, but AirSim velocity commands default to world-frame movement.

---

## Important Lessons Learned

- Yaw controls drone orientation.
- Positive and negative yaw determine rotation direction.
- Drone orientation and movement direction are separate systems.
- `moveByVelocityAsync()` uses world-frame coordinates.
- Coordinate frames are fundamental in robotics and drone navigation.

---

## Engineering Concepts Introduced

- heading control
- orientation systems
- coordinate frames
- world vs local movement
- spatial reasoning

---

## Commands Used

Run script:
```bash
python scripts/yaw_control.py
```

---

## Current Status

✅ Yaw rotation successful  
✅ Clockwise rotation tested  
✅ Anticlockwise rotation tested  
✅ World-coordinate movement behavior observed  
✅ Orientation system understood  

---

## Next Learning Goals

- waypoint navigation
- telemetry monitoring
- drone state data
- local-frame movement
- autonomous patrol systems
- MAVLink communication
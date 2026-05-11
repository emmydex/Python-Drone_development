# Lesson 4: Drone Movement Control 🚁

## Objective
Learning how to control the drone movement using velocity commands in AirSim.

This lesson introduces directional movement and hovering behavior.

---

## Mission Goals

The drone should:
1. Connect to AirSim
2. Take off
3. Fly upward
4. Move forward
5. Hover
6. Move right
7. Hover again
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
scripts/drone_movement.py
```
## New Concept: Velocity 
before:
```python
moveToZAsync() 
    which controlled altitude
```
Now i am using:
```python
moveByVelocityAsync() 
```
```
    which means:
    -move in a direction at a certain speed.
```

---

## Understanding Velocity Control

### Velocity Command

```python
client.moveByVelocityAsync(vx, vy, vz, duration)
```
```text
vx = forward speed
vy = sideways speed
vz = vertical speed
```

Purpose:
- moves the drone using directional speed values

---

## Coordinate System

AirSim uses this movement system:

```text
X = forward/backward
Y = left/right
Z = up/down
```

---

## Example Commands

### Move Forward

```python
client.moveByVelocityAsync(5, 0, 0, 3)
```

Meaning:
- move forward
- speed: 5 m/s
- duration: 3 seconds

---

### Move Right

```python
client.moveByVelocityAsync(0, 5, 0, 3)
```

Meaning:
- move right
- speed: 5 m/s
- duration: 3 seconds

---

## Hovering

```python
client.hoverAsync().join()
```

Purpose:
- keeps the drone stable in the air

---

## Commands Used

Run script:
```bash
python scripts/drone_movement.py
```

## Adding a quick coordinate cheat sheet

Forward  = +X
Backward = -X

Right    = +Y
Left     = -Y

Up       = -Z
Down     = +Z

---

## Lessons Learned

- Drones can move using velocity-based commands.
- Directional movement uses X, Y, and Z coordinates.
- Hovering stabilizes the drone during missions.
- Autonomous movement is controlled through programmable logic.

---

## Problems Encountered

### Problem
Understanding drone coordinate directions.

### Solution
Learned:
```text
X = forward/backward
Y = left/right
Z = altitude
```

---

## Current Status

✅ Drone takeoff successful  
✅ Forward movement successful  
✅ Right movement successful  
✅ Hover stabilization successful  
✅ Autonomous landing successful  

---

## Next Learning Goals

- square flight paths
- waypoint navigation
- drone rotation
- telemetry data
- automated patrol systems
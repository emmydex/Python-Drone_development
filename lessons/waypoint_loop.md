# Lesson 9: Waypoint Mission Loops 🚁

## Objective
Learning how to automate drone waypoint navigation using loops and waypoint arrays.

This lesson introduces:
- waypoint lists
- mission automation
- loop-based navigation
- autonomous patrol routes
- reusable flight logic

---

## Mission Goals

The drone should:
1. Connect to AirSim
2. Take off
3. Reach flight altitude
4. Visit multiple waypoints automatically
5. Hover briefly at each waypoint
6. Return close to home
7. Land safely

---

## Technologies Used

- Python 3.11
- AirSim
- NumPy
- msgpack-rpc-python

---

## Script File

```text
scripts/waypoint_loop.py
```

---


## What is a Waypoint?

A waypoint is:
```text
a destination coordinate
```

The drone navigates from one waypoint to another automatically.

---

## Waypoint Coordinate Structure

```python
(x, y, z)
```

Meaning:
```text
X = forward/backward position
Y = left/right position
Z = altitude
```

---

## Important Navigation Command

```python
client.moveToPositionAsync(x, y, z, speed)
```

Meaning:
```text
fly to an exact coordinate
```

Unlike velocity movement, the drone focuses on reaching a destination rather than moving for a fixed duration.

---

## Waypoint Array

```python
waypoints = [
    (20, 10, -10),
    (20, 20, -10),
    (0, 0, -10)
]
```

This stores multiple navigation targets inside a Python list.

Each tuple represents:
```text
(X position, Y position, Z altitude)
```

---

## Loop-Based Navigation

```python
for point in waypoints:
```

Meaning:
```text
visit each waypoint automatically
```

The drone no longer needs individually written movement commands.

This introduces:
```text
mission automation
```

---

## Coordinate Unpacking

```python
x, y, z = point
```

Meaning:
- extract X coordinate
- extract Y coordinate
- extract Z coordinate

from the current waypoint tuple.

---

## Triangle Mission Challenge (file in the challenge folder named triangle_waypoint_loop.py)

The original square route was modified into a triangle route by reducing the number of waypoint corners.

Example:

```python
#(0, 20, -10),
```

One waypoint was removed to create a triangle-like flight path.

This demonstrated:
- waypoint customization
- route experimentation
- mission redesign

---

## Important Observations

### Autonomous Route Execution

The drone:
- visited points automatically
- stopped at each destination
- followed the waypoint list sequentially

---

### Hover Stabilization

```python
client.hoverAsync().join()
```

allowed the drone to:
- stabilize after movement
- reduce drift
- pause before continuing

---

### Mission Automation Observation

Using loops made the mission:
- cleaner
- shorter
- easier to scale

New waypoints can be added without rewriting navigation code.

---

## Difference Between Velocity and Position Navigation

### Velocity Navigation

```python
moveByVelocityAsync()
```

Focuses on:
```text
speed + duration
```

---

### Position Navigation

```python
moveToPositionAsync()
```

Focuses on:
```text
destination coordinates
```

The drone automatically manages:
- acceleration
- slowing down
- stopping

---

## Engineering Concepts Introduced

- waypoint navigation
- mission automation
- loop-based flight systems
- coordinate routing
- autonomous patrol logic

---

## Commands Used

Run script:
```bash
python scripts/waypoint_loop.py
```

---

## Current Status

✅ Waypoint loops successful  
✅ Autonomous route execution successful  
✅ Triangle mission successful  
✅ Loop-based navigation understood  
✅ Position-based movement validated  

---

## Next Learning Goals

- decision-based flight logic
- telemetry-driven autonomy
- autonomous patrol AI
- local-frame navigation
- MAVLink communication
- dynamic mission systems
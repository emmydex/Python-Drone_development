# Lesson 5: Square Flight Pattern 🚁

## Objective
Program the drone to fly in a square flight path using velocity-based movement commands.

This lesson introduces:
- path planning
- movement sequencing
- directional control
- autonomous navigation structure

---

## Mission Goals

The drone should:
1. Connect to AirSim
2. Take off
3. Reach target altitude
4. Move forward
5. Move right
6. Move backward
7. Move left
8. Return close to starting position
9. Land safely

---

## Technologies Used

- Python 3.11
- AirSim
- NumPy
- msgpack-rpc-python

---

## Script File

```text
scripts/square_flight.py
```

---

## Understanding the Flight Path

The drone follows this movement pattern:

```text
Forward → Right → Backward → Left
```

This creates a square-shaped flight path.

---

## Coordinate System

AirSim movement directions:

```text
X = forward/backward
Y = left/right
Z = altitude
```

---

## Directional Movement Commands

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

### Move Backward

```python
client.moveByVelocityAsync(-5, 0, 0, 3)
```

Meaning:
- move backward
- speed: 5 m/s
- duration: 3 seconds

---

### Move Left

```python
client.moveByVelocityAsync(0, -5, 0, 3)
```

Meaning:
- move left
- speed: 5 m/s
- duration: 3 seconds

---

## Hover Stabilization

```python
client.hoverAsync().join()
```

Purpose:
- stabilizes the drone after movement

---

## Timing Experiments

Different hover delay values were tested before landing.

### `time.sleep(2)`
Result:
- smoother landing
- better stabilization
- slower descent behavior

### `time.sleep(0.5)`
Result:
- unstable landing
- increased crash risk

### No `time.sleep()`
Result:
- faster landing
- still stable in simulation

---

## Important Lessons Learned

- Timing affects drone stability.
- Hover stabilization helps reduce movement momentum.
- Velocity commands control directional movement.
- Autonomous flight paths are built from simple movement sequences.
- Small parameter changes can dramatically affect flight behavior.

---

## Commands Used

Run script:
```bash
python scripts/square_flight.py
```

---

## Current Status

✅ Square flight path successful  
✅ Autonomous navigation successful  
✅ Hover stabilization tested  
✅ Landing timing experiments completed  

---

## Engineering Concepts Introduced

- path planning
- velocity control
- movement sequencing
- stabilization timing
- parameter tuning

---

## Next Learning Goals

- waypoint navigation
- yaw/rotation control
- telemetry data
- drone orientation
- automated patrol missions
- MAVLink communication
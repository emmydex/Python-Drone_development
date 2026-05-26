# Lesson 11: Continuous Autonomous Monitoring 🚁

## Objective
Learnt how to continuously monitor drone telemetry and make autonomous decisions during flight.

This lesson introduces:
- continuous monitoring loops
- feedback systems
- telemetry-driven decisions
- autonomous correction behavior
- real-time drone autonomy

---

## Mission Goals

The drone should:
1. Take off
2. Move continuously
3. Read telemetry repeatedly
4. Detect unsafe altitude
5. Automatically correct altitude
6. Continue the mission safely
7. Hover
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
scripts/continuous_monitoring.py
```

---



## What Is Continuous Monitoring?

Continuous monitoring means:
```text
the drone repeatedly checks its condition during flight
```

instead of checking only once.

---

## Feedback Loop Concept

The drone follows this cycle:

```text
move
observe
decide
correct
repeat
```

This is called:
```text
a feedback loop
```

---

## Continuous Loop

```python
for i in range(5):
```

Meaning:
```text
repeat the mission cycle 5 times
```

The drone continuously:
- moves
- checks telemetry
- reacts

---

## Telemetry Monitoring

```python
state = client.getMultirotorState()
```

retrieves drone telemetry data.

This includes:
- altitude
- velocity
- orientation
- position

---

## Position Retrieval

```python
position = state.kinematics_estimated.position
```

extracts the drone’s current location.

---

## Altitude Retrieval

```python
current_altitude = position.z_val
```

retrieves the current Z-axis altitude.

Important AirSim observation:

```text
more negative Z = higher altitude
```

Example:
```text
-5  = lower altitude
-15 = higher altitude
```


---

## Understanding Negative Altitude in AirSim

A very important observation during this lesson was understanding why:

```python
if current_altitude > -10:
```

causes the drone to climb higher using:

```python
client.moveToZAsync(-15, 3).join()
```

At first this may seem confusing because:

```text
-15 is mathematically smaller than -10
```

However, AirSim uses the:

```text
NED coordinate system
```

Meaning:

```text
North
East
Down
```

In this coordinate system:

```text
positive Z = downward
negative Z = upward
```

---

## Ground Level Reference

Usually:

```text
z = 0
```

represents:
```text
ground level
```

Examples:

| Z Value | Physical Height |
|---|---|
| 0 | ground |
| -5 | slightly higher |
| -10 | higher |
| -15 | even higher |

---

## Important Observation

Although:

```text
-15 < -10
```

mathematically,

in AirSim:

```text
-15 is physically HIGHER
```

because the drone moved farther upward from ground level.

---

## Why The Condition Works

Example:

```python
current_altitude = -5
```

Then:

```python
if current_altitude > -10:
```

becomes:

```python
if -5 > -10:
```

which is:
```text
True
```

Meaning:
```text
the drone is flying lower than the desired safe altitude
```

So the drone reacts by climbing higher:

```python
client.moveToZAsync(-15, 3).join()
```

---

## Key Takeaway

In AirSim:

```text
more negative Z = higher altitude
```

This is one of the most important coordinate-system concepts in drone programming and robotics.
---

## Autonomous Decision Logic

```python
if current_altitude > -10:
```

Meaning:
```text
IF the drone is flying too low
```

then:
```python
client.moveToZAsync(-15, 3).join()
```

automatically climbs higher.

---

## Autonomous Correction

The drone:
- detects unsafe altitude
- reacts automatically
- corrects itself
- continues the mission

This introduces:
```text
reactive autonomy
```

---

## Hover Stabilization

```python
client.hoverAsync().join()
```

stabilizes the drone before landing.

---

## Important Observations

### Continuous Self-Checking

The drone repeatedly:
- monitored itself
- made decisions
- corrected unsafe conditions

during flight.

---

### Autonomous Correction Behavior

The drone successfully:
- detected low altitude
- climbed automatically
- resumed safe operation

without manual intervention.

---

### Feedback System Observation

This lesson introduced:
```text
continuous feedback-based autonomy
```

which is foundational in robotics systems.

---

## Engineering Concepts Introduced

- telemetry monitoring
- feedback loops
- reactive autonomy
- continuous decision systems
- real-time correction logic

---

## Commands Used

Run script:
```bash
python scripts/continuous_monitoring.py
```

---

## Current Status

✅ Continuous telemetry monitoring successful  
✅ Autonomous altitude correction successful  
✅ Feedback loop behavior understood  
✅ Real-time autonomy introduced  
✅ Continuous decision system validated  

---

## Next Learning Goals

- autonomous patrol AI
- waypoint + telemetry integration
- dynamic mission logic
- obstacle avoidance systems
- MAVLink communication
- intelligent navigation systems
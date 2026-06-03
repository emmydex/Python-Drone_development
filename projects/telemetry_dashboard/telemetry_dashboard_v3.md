# 📡 Telemetry Dashboard V3 — Mission Awareness System

## Project Overview

Telemetry Dashboard V3 extends the capabilities of previous telemetry systems by introducing mission awareness features.

While earlier versions focused on displaying raw flight data and interpreting drone behavior, Version 3 adds mission-related information that helps operators understand the progress and status of an autonomous flight.

The dashboard now functions more like a simplified Ground Control Station (GCS).

---

# 🎯 Project Objectives

The goals of this version are:

* Monitor drone position in real time
* Monitor drone velocity in real time
* Detect hover states
* Evaluate altitude safety
* Track mission progress
* Calculate distance from home
* Display mission information in a structured dashboard

---

# 📊 Features Implemented

## Position Monitoring

The dashboard continuously displays:

```text
X Position
Y Position
Z Position
```

This allows the operator to know the current location of the drone at any time.

---

## Velocity Monitoring

The dashboard continuously displays:

```text
X Velocity as vx
Y Velocity as vy
Z Velocity as vz
```

Velocity data helps determine whether the drone is moving or stationary.

---

## Altitude Safety Monitoring

The system evaluates altitude using predefined safety limits.

Example:

```text
Altitude Status: ✅ SAFE
```

or

```text
Altitude Status: ⚠️ TOO LOW
```

This introduces basic flight safety logic.

---

## Hover Detection

The dashboard determines whether the drone is moving or hovering.

Logic:

* Very small velocity values indicate hovering.
* Larger velocity values indicate active movement.

Example:

```text
Flight Status: 🟩 HOVERING
```

or

```text
Flight Status: 🚀 MOVING
```

This converts raw telemetry data into useful flight-state information.

---

## Mission Awareness

Version 3 introduces mission tracking information.

Example:

```text
Mission Status : PATROL
Waypoint : 2/4
Progress : 50%
```

This allows the operator to understand mission progress rather than only viewing drone position.

---

## Distance From Home

The dashboard calculates the distance between the drone's current position and its home position.

Home Position:

```python
home_position = airsim.Vector3r(0, 0, -15)
```

Distance is calculated using 3D coordinates.

Benefits:

* Mission supervision
* Return-to-home preparation
* Operational awareness

Example:

```text
Distance From Home : 10.32 m
```

---

# 🔍 Engineering Observations

## Observation 1 — Position Overshoot

Target position:

```text
X = 10
```

Observed positions:

```text
10.09
11.41
10.67
9.88
10.24
10.32
```

The drone did not stop exactly at the target coordinate.

Instead, it overshot and then corrected itself.

### Lesson

Flight controllers continuously adjust position and rarely stop at an exact coordinate.

---

## Observation 2 — Stabilization Behavior

After reaching the target area, the drone gradually reduced its velocity.

Example:

```text
2.63 m/s
1.09 m/s
0.31 m/s
0.06 m/s
```

Eventually:

```text
Flight Status: 🟩 HOVERING
```

### Lesson

The drone transitions through:

```text
MOVING
↓
CORRECTING
↓
STABILIZING
↓
HOVERING
```

This behavior is controlled by the flight controller.

---

## Observation 3 — Distance Tracking

Distance from home changed dynamically as the drone moved.

Examples:

```text
10.10 m
11.42 m
10.67 m
9.88 m
10.33 m
```

### Lesson

Mission data becomes more useful when telemetry is interpreted in context.

Raw coordinates alone are less informative than distance measurements.

---

## Observation 4 — Telemetry Enables Understanding

Without telemetry:

```text
The drone is flying.
```

With telemetry:

```text
The drone is flying.
The drone is moving.
The drone is safe.
The drone is 10 meters from home.
The drone is halfway through its mission.
```

### Lesson

Telemetry transforms data into situational awareness.

---

# 🧠 Concepts Learned

During this project the following concepts were reinforced:

* Drone telemetry
* Position monitoring
* Velocity monitoring
* Hover detection
* Flight-state interpretation
* Mission awareness
* Distance calculations
* Autonomous system monitoring
* Ground Control Station concepts

---

# 🚀 Future Improvements

Planned Version 4 features:

* Automatic waypoint tracking
* Dynamic mission progress
* Mission completion detection
* Return-to-home monitoring
* Telemetry logging
* Flight history recording
* Warning and alert systems

---

# 📌 Project Status

Telemetry Dashboard V3 successfully demonstrates:

✅ Real-time telemetry collection

✅ Flight-state detection

✅ Altitude safety monitoring

✅ Mission awareness

✅ Distance-from-home calculations

✅ Ground Control Station fundamentals

---

# Final Reflection

Telemetry Dashboard V3 represents the transition from simple drone control to mission supervision.

Rather than only commanding a drone, the software now understands and reports what the drone is doing, how it is behaving, and how the mission is progressing.

This is a foundational capability used in professional autonomous drone systems and Ground Control Station.

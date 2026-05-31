# 🧪 Telemetry Dashboard — Engineering Observations

This document records important discoveries, test results, and engineering lessons learned while developing the Telemetry Dashboard project.

---

# 🚀 Project Goal

The objective of this project is to build a real-time drone telemetry monitoring system capable of displaying and interpreting live flight information.

The project introduces concepts commonly used in Ground Control Stations (GCS) and autonomous UAV systems.

---

# 📡 Observation 1 — Position Overshoot

## Test

Command issued:

```python
client.moveToPositionAsync(10, 0, -15, 3).join()
```

Expected position:

```text
X = 10.00
Y = 0.00
Z = -15.00
```

Actual position:

```text
X = 10.20
Y = 0.00
Z = -15.30
```

---

## Result

The drone slightly exceeded the target coordinates.

---

## Engineering Lesson

Flight controllers do not always stop at the exact target position.

Small errors occur due to:

* momentum
* stabilization corrections
* flight controller tuning
* simulation physics

This behavior is called:

```text
position overshoot
```

and is normal in both simulations and real drones.

---

# 📡 Observation 2 — Hover Position Drift

## Test

The drone was commanded to hover after reaching the target location.

Telemetry values were monitored continuously.

---

## Result

Position values changed slightly over time.

Example:

```text
10.20
10.19
10.21
10.20
```

---

## Engineering Lesson

Even while hovering, a drone constantly performs micro-adjustments to maintain stability.

Factors include:

* flight controller corrections
* sensor noise
* physics simulation
* environmental effects

Perfectly stationary flight is uncommon.

---

# 📡 Observation 3 — Velocity Reaches Near Zero During Hover

## Test

Velocity values were monitored after movement completion.

Observed values:

```text
Velocity X = 0.00
Velocity Y = 0.00
Velocity Z = -0.01
```

Later:

```text
Velocity X = 0.00
Velocity Y = 0.00
Velocity Z = 0.00
```

---

## Engineering Lesson

When velocity approaches zero:

```text
the drone has completed movement
```

and is maintaining a hover state.

Tiny values such as:

```text
-0.01
```

represent stabilization corrections rather than meaningful movement.

---



# 📡 Observation 4 — Exact Equality Checks Are Dangerous

## Example

Avoid:

```python
if position.x_val == 10:
```

because the drone may report:

```text
10.20
9.95
10.08
```

instead of exactly:

```text
10.00
```

---

## Better Approach

Use tolerances:

```python
if abs(position.x_val - 10) < 0.5:
```

---

## Engineering Lesson

Robotics systems work with approximations rather than perfect values.

Most navigation systems use acceptable error ranges instead of exact comparisons.

---

# 📡 Observation 5 — Telemetry Creates Situational Awareness

Without telemetry:

```text
the drone flies blindly
```

With telemetry:

```text
the operator understands
- location
- altitude
- movement state
- flight behavior
```

---

## Engineering Lesson

Telemetry is the foundation of:

* Ground Control Stations
* Autonomous UAV systems
* Flight analytics
* Safety monitoring
* Mission supervision

---

# 🧠 Key Concepts Learned

During this project the following concepts became clearer:

* telemetry systems
* flight state monitoring
* position tracking
* velocity monitoring
* coordinate systems
* position tolerances
* hover stabilization
* flight controller behavior

---

# 🚀 Future Improvements

Planned upgrades:

* flight status indicators
* altitude warning system
* mission status display
* battery monitoring
* telemetry logging
* graphical dashboard
* real-time charts
* waypoint visualization

---

# 📌 Current Status

✅ Live telemetry monitoring operational

✅ Position tracking operational

✅ Velocity tracking operational

✅ Hover state monitoring operational

🚧 Intelligent telemetry interpretation in development

---

# Final Reflection

This project introduced a key lesson in drone engineering:

```text
Knowing where the drone is can be just as important as controlling where it goes.
```

Telemetry transforms a drone from a remotely controlled vehicle into an observable and manageable autonomous system.


# More Observation soon
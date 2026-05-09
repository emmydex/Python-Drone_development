This note contains
    what the script does
    commands used
    what you learned
    issues encountered



## Objective
Connect Python to the AirSim simulator and execute a fully autonomous drone mission.


## Mission milestones

The drone should:
1. Connect to AirSim
2. Enable API control
3. Arm itself
4. Take off
5. Fly upward
6. Hover
7. Land safely
8. Disarm

---



## Technologies Used

- Python 3.11
- AirSim
- NumPy
- msgpack-rpc-python

---

## Flight Script

File:
```text
scripts/first_flight.py
```



## Understanding the Flight Logic

### Connecting to AirSim

```python
client = airsim.MultirotorClient()
client.confirmConnection()
```

Purpose:
- establishes communication between Python and AirSim

---


### API Control

```python
client.enableApiControl(True)
```

Purpose:
- gives Python control over the drone

---


### Arming the Drone

```python
client.armDisarm(True)
```

Purpose:
- prepares motors for flight

---

### Takeoff

```python
client.takeoffAsync().join()
```

Purpose:
- launches the drone automatically

---


### Altitude Control

```python
client.moveToZAsync(-10, 2)
```

Meaning:
- fly to altitude:
```text
-10 meters
```

at speed:
```text
2 meters/second
```

Important:
- AirSim uses negative Z values for upward movement

---

### Landing

```python
client.landAsync().join()
```

Purpose:
- safely lands the drone

---

## Commands Used

Run mission:
```bash
python scripts/first_flight.py
```

---

## Problems Encountered

### Problem
No problems encountered in curret stage


---

## Lessons Learned

- Python can control drone behavior autonomously.
- AirSim supports programmable UAV simulations.
- API control allows software-based flight operations.
- Drone movement commands can be automated using scripts.
- Coordinate systems are important in drone programming.

---


## Current Status

✅ AirSim connected successfully  
✅ Drone armed successfully  
✅ Autonomous takeoff completed  
✅ Autonomous landing completed  

---

## Next Learning Goals

- directional movement
- waypoint navigation
- flight patterns
- telemetry monitoring
- MAVLink communication
# 📡 Telemetry Dashboard Drone

A real-time drone telemetry monitoring system built using Python and AirSim.

This project focuses on creating a beginner Ground Control Station (GCS)-style monitoring system capable of displaying live drone flight information during autonomous missions.

---

# 🚀 Project Goals

This project was created to learn:

- Real-time telemetry systems
- Drone state monitoring
- Autonomous system awareness
- Continuous data updates
- UAV monitoring architecture
- Ground Control Station concepts

---

# 🛰️ Features

Current features:

✅ Live altitude monitoring  
✅ Real-time X/Y/Z position tracking  
✅ Velocity monitoring  
✅ Continuous telemetry updates  
✅ Autonomous patrol state tracking  
✅ Flight state awareness  

---

# 🧠 Key Concepts Learned

## Telemetry Systems

Telemetry allows the drone to continuously report:

- position
- altitude
- orientation
- velocity
- system state

This creates:
```text
real-time drone awareness
```

---

## Continuous Monitoring

The system continuously:

```text
observe → analyze → display → repeat
```

This introduces the foundations of:
- autonomous systems
- reactive UAV behavior
- intelligent monitoring systems

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

# 📂 Project Structure

```text
telemetry_dashboard/
│
├── telemetry_dashboard.py
├── telemetry_dashboard_v2.py
├── telemetry_dashboard_v3.py
├── README.md
├── observations.md
└── future_improvements.md
```

---

# 🚀 Technologies Used

- Python 3.11
- AirSim
- Unreal Engine 5
- NumPy

---

# ▶️ Running The Project

Start AirSim first.

Then run:

```bash
python telemetry_dashboard.py
```

---

# 📡 Telemetry Data Displayed

The dashboard currently monitors:

- altitude
- X position
- Y position
- Z position
- drone movement state
- patrol status

---

# 🧪 Engineering Observations

Important discoveries during development:

| Observation | Result |
|---|---|
| continuous telemetry improves awareness | drone behavior easier to understand |
| delayed monitoring causes slow reactions | autonomy requires constant observation |
| telemetry loops are essential for intelligent systems | monitoring is the foundation of autonomy |

---

# 🚀 Future Improvements

Planned upgrades:

- GUI telemetry dashboard
- live charts and graphs
- battery monitoring
- warning systems
- obstacle alerts
- waypoint visualization
- map integration
- real-time mission analytics

---

# 🛰️ Long-Term Vision

This project is an early step toward building:

- intelligent UAV systems
- autonomous monitoring drones
- AI-assisted flight systems
- advanced Ground Control Stations (GCS)

---

# 📌 Current Status

✅ Telemetry monitoring functional  
✅ Continuous data updates working  
🚧 Expanding into real-time intelligent monitoring systems  

---
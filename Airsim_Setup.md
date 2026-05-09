# AirSim Setup Notes 🚁

## Objective
Setting up the AirSim drone simulator for Python-based drone programming.

---

## Software Installed

### Python
Version:
```text
Python 3.11.6
```

### Python Packages
Installed packages:

```bash
python -m pip install numpy
python -m pip install msgpack-rpc-python
python -m pip install airsim --no-build-isolation
```

---

## Simulator Setup

Downloaded:
- AirSim Blocks Environment

Simulator executable:
```text
Blocks.exe
```

Status:
✅ Simulator launches successfully

---

## Problems Encountered

### Problem 1
Error:
```text
pip not recognized
```

Solution:
Used:
```bash
python -m pip
```

instead of:
```bash
pip
```

---

### Problem 2
Error:
```text
ModuleNotFoundError: No module named 'numpy'
```

Solution:
Installed NumPy separately before installing AirSim.

---

### Problem 3
AirSim build isolation issue.

Solution:
Installed using:
```bash
python -m pip install airsim --no-build-isolation
```
```text
    why this works
 normally pip creates a temmporary isolated environment during installation.
 Airsim's installer then fails to see i already installed numpy.
```
```text
    The Flag ⛳

    --no-build-isolation
 tells pip:
            'use the packages already installed on my system.'
    so Airsim can finally detect Numpy
```
```text
    Testing
i tested if airsim was sussefully installed using :-
```
```bash
python -c "import airsim; print('AirSim installed!')"
```


---

## Lessons Learned

- Python package dependencies matter.
- AirSim requires NumPy during installation.
- Older robotics libraries may have compatibility issues.
- Reading error messages carefully helps debugging.

---

## Current Status

✅ AirSim installed  
✅ Simulator running  
✅ Python connected successfully  

Next step:
- Run first autonomous drone flight script
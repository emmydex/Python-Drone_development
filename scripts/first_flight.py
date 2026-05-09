import airsim
import time

# Connecting to AirSim
client = airsim.MultirotorClient()
client.confirmConnection()

print("Connected to AirSim!")

# Enabled API control
client.enableApiControl(True)

# Arm drone
client.armDisarm(True)

print("Drone armed!")

# Take off
client.takeoffAsync().join()

print("Taking off...")

time.sleep(2)

# Move to altitude
client.moveToZAsync(-10, 2).join()

print("Drone is flying!")

time.sleep(5)

# Land
client.landAsync().join()

print("Landing...")

# Disarm
client.armDisarm(False)

# Release control
client.enableApiControl(False)

print("Mission complete!")
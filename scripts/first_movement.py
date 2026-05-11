import airsim
import time

# Connecting to AirSim
client = airsim.MultirotorClient()
client.confirmConnection()

print("Connected to AirSim sucessfully!")

# Enabled API control
client.enableApiControl(True)

# Arm drone
client.armDisarm(True)

print("Drone is ready for lunch!")

# Take off
client.takeoffAsync().join()

print("countdown is T-5...")

time.sleep(2)

# Move to altitude
client.moveToZAsync(-10, 2).join()

print("Altitude reached!")

# direction foward
print("Moving forward..")
client.moveByVelocityAsync(5,0,0,3).join()
print("Forward movement achieved!")



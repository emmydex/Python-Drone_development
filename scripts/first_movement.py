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


# direction : hover
client.hoverAsync().join()
print("hovering")

time.sleep(2)

# direction : right
print("Moving right..")
client.moveByVelocityAsync(0,5,0,3).join()

# direction : backward
client.moveByVelocityAsync(-4,0,0,3).join()
print("Backward movement achieved!")

# direction : movement left
client.moveByVelocityAsync(0,-5,0,3).join()
print("left is me oluwafemi")


# direction : hover again
client.hoverAsync().join()

time.sleep(2)

# direction : land
client.landAsync().join()

print("Landing...")

# Disarm
client.armDisarm(False)

# Release control
client.enableApiControl(False)

print("Mission complete!")
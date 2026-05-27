import airsim
import time

#connect to airsim
client = airsim.MultirotorClient()
client.confirmConnection()
print("connected ")

# enabling Api control
client.enableApiControl(True)

# arm drone
client.armDisarm(True)

# takeoff
client.takeoffAsync().join()

# base altitude
client.moveToZAsync(-10, 3).join()


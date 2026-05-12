import airsim
import time

#connectin to airsim
client= airsim.MultirotorClient()
client.confirmConnection()
print("connected")

#api enabled
client.enableApiControl(True)

#arm drone
client.armDisarm(True)

#taking off
client.takeoffAsync().join()
print("we in the sky")



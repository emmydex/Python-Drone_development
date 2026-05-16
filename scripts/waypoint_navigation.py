import airsim
import time

# connect to airsim
client = airsim.MultirotorClient()
client.confirmConnection()

print("connected")

# enabling api
client.enableApiControl(True)

# arming
client.armDisarm(True)
print("drone armed")

# take ooff
client.takeoffAsync().join()

time.sleep(2)

# reach for altitiude

client.moveToZAsync(-10, 2).join()
print("reached altitude")


import airsim
import time

# connectng to airsim
client = airsim.MultirotorClient()
client.confirmConnection()
print("connected sucessfully")


#enabling api control
client.enableApiControl(True)

# arming
client.armDisarm(True)

# takeoff
client.takeoffAsync().join()

#move to monitoring altitude
client.moveToZAsync(-15,4).join()
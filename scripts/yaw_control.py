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

time.sleep(2)

# upward movement
client.moveToZAsync(-10, 2).join()
print("reached altitude")

# rotate 90 degrees yaw control
print("rotating ...")
client.rotateToYawAsync(90).join()

time.sleep(2)

#moving forward
print("moving forward..")
client.moveByVelocityAsync(5,0,0,3).join()

client.hoverAsync().join()

#landing
print("landing ...")
client.landAsync().join()

#disarm
client.armDisarm(False)


# realease control
client.enableApiControl(False)

print("mission was a success!") 
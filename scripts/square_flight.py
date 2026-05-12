import airsim
import time


#connect to airsim
client = airsim.MultirotorClient()
client.confirmConnection()
print("connected")

# Api enabling
client.enableApiControl(True)

#arm drone
client.armDisarm(True)

print("blades are waarming up")

#take off
client.takeoffAsync().join()
print("bird in the sky")

time.sleep(2)

#flying upward
client.moveToZAsync(-10, 2).join()
print("altitude reached")

# foward movement
client.moveByVelocityAsync(5,0,0,3).join()
print ("foward movement is attained")

#hovering
client.hoverAsync().join()
time.sleep(1)

#right movement
client.moveByVelocityAsync(0,5,0,3).join()
print("right side of life")

#hovering
client.hoverAsync().join()
time.sleep(1)

#move backwards
client.moveByVelocityAsync(-5,0,0,3).join()
print(" i dont want to go back")

#hovering
client.hoverAsync().join()
time.sleep(1)

# left movement
client.moveByVelocityAsync(0,-5,0,3).join()
print("left side of life")

#hovering
client.hoverAsync().join()
time.sleep(1)

#landing
client.landAsync().join()

#disarm
client.armDisarm(False)

#realease Api control
client.enableApiControl(False)
print("mission accomplished")

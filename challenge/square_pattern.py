#Try making the drone:

#take off
#move forward
#move right
#move backward
#move left
#return close to starting point
#land


import airsim
import time

#connect to airsim
client = airsim.MultirotorClient()
client.confirmConnection()
print("connection sucessful")


# Api enabling
client.enableApiControl(True)

# arm drone
client.armDisarm(True)
print("drone is ready for lunch")

# taking off bbbyyy
client.takeoffAsync().join()

time.sleep(4)

# hovering
client.hoverAsync().join()
print("hovering")

time.sleep(3)


# direction : forward
client.moveByVelocityAsync(7,0,0,3).join()
print("foward movement is attained")

# direction : right
client.moveByVelocityAsync(0,7,0,3).join()
print("right side of life")

# direction : backward
client.moveByVelocityAsync(-7,0,0,3).join()
print(" i dont want to go back")


# direction : left
client.moveByVelocityAsync(0,-7,0,3).join()
print("left the chat")

# direction : hover again
client.hoverAsync().join()

time.sleep(3)

# direction : landing
client.landAsync().join()
print("touchdown in T-5...")
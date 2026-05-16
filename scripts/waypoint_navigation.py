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

# waypoint 1
print("moving to waypoint 1")
client.moveToPositionAsync(20,0,-10,5).join()

time.sleep(2)


# waypoint 2
print("moving to waypoint 2")
client.moveToPositionAsync(20,20,-10,5).join()

time.sleep(2)


# waypoint 3
print("moving to waypoint 3")
client.moveToPositionAsync(0,20,-10,5).join()

time.sleep(2)


# return close to home
print("returning home")
client.moveToPositionAsync(0,0,-10,5).join()

time.sleep(2)

#land
print("landing")
client.landAsync().join()


# disarm
client.armDisarm(False)

# disable api
client.enableApiControl(False)

print("mission complete")
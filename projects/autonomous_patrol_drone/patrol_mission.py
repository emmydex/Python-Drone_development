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

waypoints = [

    (20, 0, -10),
    (20, 20, -10),
    (0, 20, -10),
    (0, 0, -10)

]

#looping through waypoints
for point in waypoints:
    x, y, z = point
    print(f"patrolling waypoint {point}")
    client.moveToPositionAsync(x, y, z, 3).join()

# monitoring telemetry 
state = client.getMultirotorState()

# hovering
client.hoverAsync().join()

time.sleep(2)

# landing
client.landAsync().join()


# disarm
client.armDisarm(False)

# release API control
client.enableApiControl(False)


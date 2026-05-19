import airsim
import time

client = airsim.MultirotorClient()
client.confirmConnection()

# connect to api
client.enableApiControl(True)

# arm drone
client.armDisarm(True)

print("starting mission")

client.takeoffAsync().join()

# moving to altitiude
client.moveToZAsync(-10, 2).join()

# adding waypoints to a list

waypoints = [
    (20, 10, -10),
   # (20, 20, -10),
    #(0, 20, -10),
    #0, 0, -10)
]

# looping through waypoints
for point in waypoints:
    x, y, z = point
    print(f"reaching first milestone {point}")
    client.moveToPositionAsync(x, y, z, 5).join()

    client.hoverAsync().join()
    time.sleep(1)


# landing
print("returning to start point")
client.landAsync().join()

# disarming
client.armDisarm(False)


# removing Api control
client.enableApiControl(False)

print("mission complete")
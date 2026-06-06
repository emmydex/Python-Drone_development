import airsim
import time

#connect to airsim
client = airsim.MultirotorClient()
client.confirmConnection()

client.enableApiControl(True)

client.armDisarm(True)

client.takeoffAsync().join()

client.moveToZAsync(-5, 0, -10, 2).join()


waypoints = [
    (20, 0, -10),
    (20, 20, -10),
    (0, 20, -10),
    (0, 0, -10)
]


def log_event(message):
    with open("drone_logger.txt", "a") as log:
        log.write(message + "\n")



yaw_angles = [90, 180, -90, 0]

for i in range(len(waypoints)):

    x, y, z = waypoints[i]

    print(f"Moving to waypoint {i+1}")

    client.moveToPositionAsync(x, y, z, 3).join()

    client.hoverAsync().join()

    print("Checkpoint reached")

    log_event(f"waypoint {i+1} reached at coordinates ({x}, {y}, {z})")

    # rotate at checkpoint
    client.rotateToYawAsync(yaw_angles[i]).join()

    print("Area scan complete")
    log_event(f"scan complete {i+1}")

    time.sleep(2)



# disarm
client.armDisarm(False)

#release API control
client.enableApiControl(False)
print("mission was a success!")
log_event("mission completed")
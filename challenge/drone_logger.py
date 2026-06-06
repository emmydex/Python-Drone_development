import airsim
import time

from datetime import datetime

#connect to airsim
client = airsim.MultirotorClient()
client.confirmConnection()


 # logger function
def log_event(message):
    timestamp = datetime.now().strftime("%H:%M:%S")

    with open("drone_logger.txt", "a") as log:
        log.write(f"[{timestamp}] {message}\n")

client.enableApiControl(True)

client.armDisarm(True)

client.takeoffAsync().join()

# added a separator 
log_event("\n==================")
log_event("mission started")
log_event("takeoff complete")

client.moveToZAsync(-10, 2).join()


waypoints = [
    (20, 0, -10),
    (20, 20, -10),
    (0, 20, -10),
    (0, 0, -10)
]




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


# landing
client.landAsync().join()
log_event("landing complete")
log_event("mission complete")


# disarm
client.armDisarm(False)

#release API control
client.enableApiControl(False)
print("mission was a success!")
log_event("mission completed")
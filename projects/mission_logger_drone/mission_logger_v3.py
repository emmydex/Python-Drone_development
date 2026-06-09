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

log_event("MISSION STARTED")
start_time = time.time()

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

# added mission duration, start time and end time 
end_time = time.time()
mission_duration = end_time - start_time

# disarm
client.armDisarm(False)

#release API control
client.enableApiControl(False)
print("mission was a success!")

# mission summery
log_event("=========================")
log_event("MISSION SUMMARY")
log_event("=========================")
log_event(f"mission started at: {datetime.fromtimestamp(start_time).strftime('%H:%M:%S')}")
log_event(f"mission ended at: {datetime.fromtimestamp(end_time).strftime('%H:%M:%S')}")
log_event(f"Total waypoints visited: {len(waypoints)}")
log_event(f"Mission duration: {mission_duration:.2f} seconds")
log_event("Mission status: success")
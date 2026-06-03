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

print("reached monitoring altitude")

client.moveToPositionAsync(10, 0, -15, 3).join()

# adding mission variables

total_waypoints = 4
current_waypoint = 2
mission_status = "patrol"

#calculating progress
progress = (current_waypoint / total_waypoints) * 100

# calculating distance from home
# distance_from_home = ((x ** 2) + (y ** 2)) ** 0.5

# a better logical approach
home_position = airsim.Vector3r(0, 0, -15)





print("\nStarting telemetry monitoring..\n")

for i in range(20):

    state = client.getMultirotorState()
    position = state.kinematics_estimated.position

    velocity = state.kinematics_estimated.linear_velocity

    x = position.x_val
    y = position.y_val
    z = position.z_val

    vx = velocity.x_val
    vy = velocity.y_val
    vz = velocity.z_val

    distance_from_home =(
        (position.x_val - home_position.x_val) ** 2 +
        (position.y_val - home_position.y_val) ** 2 +
        (position.z_val - home_position.z_val) ** 2 
    ) ** 0.5

    print("\n==========================")
    print(" 📊 TELEMETRY DASHBOARD")
    print("============================")

    print(f"x position: {x:.2f}")
    print(f"y position: {y:.2f}")
    print(f"z position: {z:.2f}")

    print(f"x velocity: {vx:.2f}")
    print(f"y velocity: {vy:.2f}")
    print(f"z velocity: {vz:.2f}")

        # mission section
    print("\nMISSION DATA")
    print(f"mission status : {mission_status}")
    print(f"waypoint : {current_waypoint}/{total_waypoints}")
    print(f"progress : {progress :.0f}%")

    # altitude check
    if z > -10:
        print("altitude status: ⚠️ low altitude")

    else:
        print("altitude status: ✅ safe altitude")


    # hover detection

    if abs(vx) < 0.1 and abs(vy) < 0.1 and abs(vz) < 0.1:
        print("flight Status: 🟩 Hovering ")

    else:
        print("Flight Status: reaching for the stars oluwafemi")

        time.sleep(1)
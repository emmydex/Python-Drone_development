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

    print("\n==========================")
    print(" 📊 TELEMETRY DASHBOARD")
    print("============================")

    print(f"x position: {x:.2f}")
    print(f"y position: {y:.2f}")
    print(f"z position: {z:.2f}")

    print(f"x velocity: {vx:.2f}")
    print(f"y velocity: {vy:.2f}")
    print(f"z velocity: {z:.2f}")

    time.sleep(1)
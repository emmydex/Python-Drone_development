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

    print(f"\n--- Telemetry Update {i+1} ---")

    print(f"x position: {position.x_val:.2f}")
    print(f"y position: {position.y_val:.2f}")
    print(f"z position: {position.z_val:.2f}")

    print(f"x velocity: {velocity.x_val:.2f}")
    print(f"y velocity: {velocity.y_val:.2f}")
    print(f"z velocity: {velocity.z_val:.2f}")

    time.sleep(1)

# landing
client.landAsync().join()

# disarming
client.armDisarm(False)

# realising api control
client.enableApiControl(False)

print("\nTelemetry monitoring ended. Drone landed and disarmed.")
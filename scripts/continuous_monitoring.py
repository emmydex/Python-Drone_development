import airsim
import time

# airsim connection
client = airsim.MultirotorClient()
client.confirmConnection()
print("connection successful")

# api connection
client.enableApiControl(True)

# arm drone
client.armDisarm(True)

#takeoff
client.takeoffAsync().join()

# base altitude
client.moveToSAsync(-5, 2).join()

print("autonomous monitoring mission starting...")

# continous monitoring loop
for i in range(5):
    print(f"\nMission cycle: {i+1}")

    #move forward
    client.moveByVelocityAsync(5, 0, 0, 2).join()

    # read telemetry
    state = client.getMultirotorState()

    position = state.kinematics_estimated.position
    current_altitude = position.z_val
    print(f"Current altitude: {current_altitude}")

    
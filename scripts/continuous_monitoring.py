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

    # creating decision logic

    if current_altitude > -10:

        print("Altitude is unsafe!")
        print("climbing to higher altitude")

        client.moveToZAsync(-15, 3).join()
        print("altitude corrected")

    else:
        print("altitude is presummed safe")

    time.sleep(1)


# hovering before landing
client.hoverAsync().join()

time.sleep(2)

#landing
client.landAsync().join()

# disarming
client.armDisarm(False)

# realeasing Api control
client.enableApiControl(False).join()

print("milestone acheived")
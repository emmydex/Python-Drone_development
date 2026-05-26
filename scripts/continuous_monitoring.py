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
client.moveToZAsync(-5, 2).join()

print("autonomous monitoring mission starting...")

# continous monitoring loop
for i in range(5):
    print(f"\nMission cycle: {i+1}")

    #move forward with a speed of 5 m/s for 2 second
    client.moveByVelocityAsync(5, 0, 0, 2).join()

    # reading drone information known as telemetry
    state = client.getMultirotorState()

    # this gets the drone position and location
    position = state.kinematics_estimated.position


    # this gets the drone altitude
    current_altitude = position.z_val
    print(f"Current altitude: {current_altitude}")

    # creating decision logic
    # the logic is -10 is lesser than the base altitude of -5 which is lower than the safe altitude
    if current_altitude > -10:

        print("Altitude is unsafe!")
        print("climbing to higher altitude")


        # this tells the drone to move to a higher altitude of -15 with a speed of 3 m/s
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
client.enableApiControl(False)

print("milestone acheived")
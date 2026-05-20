import airsim
import time

#  connect to airsim
client = airsim.MultirotorClient()
client.confirmConnection()
print("connected")

#enabling api
client.enableApiControl(True)

# arm drone
client.armDisarm(True)

#takeoff
client.takeoffAsync().join()

time.sleep(2)

#initial altitude
client.moveToZAsync(-5, 2).join()
print("checking telemetry")

# read telemetry
state = client.getMultirotorState()

# current position
position = state.kinematics_estimated.position

#current altitude
current_altitude = position.z_val

print(f"current altitude: {current_altitude}")

# decision making based on altitude
if current_altitude > -10:
    print("altitude tooo low!")

    print("climbing higher...")

    client.moveToZAsync(-15, 3).join()
    print("safe altitude achieved!")

else:

    print("altitude is safe.")

time.sleep(2)

# hovering

client.hoverAsync().join()

time.sleep(2)

# landing
print("touching down...")
client.landAsync().join()

#disarm
client.armDisarm(False)

#release api control
client.enableApiControl(False)

print("mission success")
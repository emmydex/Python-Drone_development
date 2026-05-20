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

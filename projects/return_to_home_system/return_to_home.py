import airsim
import time

#connecting to airsim
client = airsim.MultirotorClient()
client.confirmConnection()

# api control
client.enableApiControl(True)

# arm drone
client.armDisarm(True)

# take off
client.takeoffAsync().join()

# mission altitude
client.moveToZAsync(-10, 5).join()

# this gets and stores the current position
state = client.getMultirotorState()
position = state.kinematics_estimated.position

home_x = position.x_val
home_y = position.y_val
home_z = position.z_val

print('current position:')
print(
    position.x_val,
    position.y_val,
    position.z_val
)

# then drone moves back to home
client.moveToPositionAsync(
    home_x,
    home_y,
    home_z,
    3
).join()

print("home position")
print(
    home_x,
    home_y,
    home_z
)
time.sleep(1)

#hovering
client.hoverAsync().join()

#landing
client.landAsync().join()

#disarm
client.armDisarm(False)

# disable api
client.enableApiControl(False)

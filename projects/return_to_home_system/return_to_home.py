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

# passing home position to the variable
home_position = client.getMultirotorState().kinematics_estimated.position

print("home position saved")
print(
    home_position.x_val,
    home_position.y_val,
    home_position.z_val
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

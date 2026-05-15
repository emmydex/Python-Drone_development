import airsim
import time


#connect to airsim
client = airsim.MultirotorClient()
client.confirmConnection()

print("connected")

# enable control
client.enableApiControl(True)

#Arm drone 
client.armDisarm(True)

print("drone armed")

# take off
client.takeoffAsync().join()

#fly upwards
client.moveToZAsync(-10, 2).join()

print("we in the sky !")

#read telemetry data
for i in range(10):

    # get drone state 
    state = client.getMultirotorState()

    # getting drone posion
    position = state.kinematics_estimated.position

    #velocity

    velocity = state.kinematics_estimated.linear_velocity

    print("\n--- TELEMENTRY DATA FOR THIS DRONE---")

    print(f"x position: {position.x_val:.2f}")
    print(f"y position: {position.y_val:.2f}")
    print(f"z position: {position.z_val:.2f}")

    print(f"x velocity: {velocity.x_val:.2f}")
    print(f"y velocity: {velocity.y_val:.2f}")
    print(f"z velocity: {velocity.z_val:.2f}")

    time.sleep(1)

#land 
client.landAsync().join()
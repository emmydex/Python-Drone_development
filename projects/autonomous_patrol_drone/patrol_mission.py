import airsim
import time

#connect to airsim
client = airsim.MultirotorClient()
client.confirmConnection()
print("connected ")

# enabling Api control
client.enableApiControl(True)

# arm drone
client.armDisarm(True)

# takeoff
client.takeoffAsync().join()

# base altitude and this should be like -5 for all waypoint altitude is -10
client.moveToZAsync(-5, 2).join()


#adding a foward movement to test the decision making part of the project
client.moveToPositionAsync(5, 0, -10, 2).join()


waypoints = [

    (20, 0, -10),
    (20, 20, -10),
    (0, 20, -10),
    (0, 0, -10)

]

#looping through waypoints
#for point in waypoints:
 #   x, y, z = point

    
# implementing yaw rotation for rotation at checkpoints
#for waypoint in waypoints:
 #   print(f"patrolling waypoint {point}")
  #  client.moveToPositionAsync(x, y, z, 3).join()

#    client.hoverAsync().join()
#
 #   client.rotateToYawAsync(90).join()

#    print("scanning for stars")

# monitoring telemetry using for loop

# different rotations

yaw_angles = [90, 180, -90, 0]

for i in range(len(waypoints)):

    x, y, z = waypoints[i]

    print(f"Moving to waypoint {i+1}")

    client.moveToPositionAsync(x, y, z, 3).join()

    client.hoverAsync().join()

    print("Checkpoint reached")

    # rotate at checkpoint
    client.rotateToYawAsync(yaw_angles[i]).join()

    print("Area scan complete")

    time.sleep(2)

for i in range(20):

    #this gets the current state of the drone
    state = client.getMultirotorState()

    # getting drone position
    position = state.kinematics_estimated.position

    # current altitude
    current_altitude = position.z_val

    print(f"current altitude: {current_altitude}")

# decision making based on altitude
if current_altitude > -10:
    print("altitude is low")

    print("making decision to climb higher")

    client.moveToZAsync(-25, 5).join()
    print("safe altitude achieved")

else:

    print("current altitude is safe.")

time.sleep(1)

    # getting drone velocity
velocity = state.kinematics_estimated.linear_velocity

print("\n-- DATA FOR THIS PATROL DRONE--")

    # getting position data
print(f"x position: {position.x_val:.2f}")
print(f"y position: {position.y_val:.2f}")
print(f"z position: {position.z_val:.2f}")

    # getting velocity data
print(f"x velocity: {velocity.x_val:.2f}")
print(f"y velocity: {velocity.y_val:.2f}")
print(f"z velocity: {velocity.z_val:.2f}")



time.sleep(1)



# hovering
client.hoverAsync().join()



# landing
client.landAsync().join()


# disarm
client.armDisarm(False)

# release API control
client.enableApiControl(False)



print("project is a success oluwafemi")

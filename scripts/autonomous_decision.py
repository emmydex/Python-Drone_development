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

# added foward direction to make it more interesting, you can remove it if you want
#print("Moving forward..")
#client.moveByVelocityAsync(5,0,0,3).join()
#print("Forward movement achieved!")





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

    client.moveToZAsync(-35, 6).join()
    print("safe altitude achieved!")

else:

    print("altitude is safe.")

time.sleep(1)



# trying move to position
client.moveToPositionAsync(30,0,-10,2).join()


# without this it crashes when it tries to land
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
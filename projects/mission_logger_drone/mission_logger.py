def log_event(message):
    with open("flight_log.txt", "a") as log:
        log.write(message + "\n")


log_event("mission started")
log_event("takeoff complete")
log_event("waypoint 1 reached")
log_event("landing complete")
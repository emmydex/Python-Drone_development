Mission flow

START

→ connect to drone
→ arm drone
→ takeoff
→ climb to patrol altitude

→ begin patrol loop

    → fly to waypoint
    → monitor altitude
    → correct altitude if unsafe
    → rotate at checkpoint
    → hover briefly

→ repeat for all waypoints

→ return home
→ hover
→ land
→ disarm

This is a combination of

movement + decision-making + monitoring

Patrol waypoints for this projects 

waypoints = [

    (20, 0, -10),
    (20, 20, -10),
    (0, 20, -10),
    (0, 0, -10)

]

END
# ENPM661 Project 3- Phase 3 and 4
## This project plans a path for the TurtleBot taking into consideration its holonomic constraints and uses Astar algorithm to solve the obstacle space
<img src="https://github.com/AkshayKurhade/ENPM661Project3Phase3and4/blob/master/Output/Map.png" width="480">

### Note-All Dimensions were considered to be in millimeters(mm)

# Output video Link-https://youtu.be/RoZN09WYEkI

# Required Libraries-
    1) Matplotlib
    2) Numpy
    3) Time
    4) Math
    5) heapq
    6) Opencv
    Warning - Use of 'heapq' may generate low memory or running out of memory error

## Files required in the source directory
    1) Phase3.py
    2) Worldmap.py
    3) Functions.py

## How to run the code-
 ### System Requirements-
        Python v3.7.x or later
 ### Custom Parameter Cofiguration 
        Set the User Defined Flag in 'Phase3.py'
            True= User inputs the Configuration.
            False- Pre-defined configuration.
 #### Input parameters-
    start_x = enter start x co-ordinate     %Suggested(60)
    start_y =enter start y co-ordinate      %(60)
    start_orient =enter start orientation   %(30)
    goal_x = enter goal x co-ordinate       %1000
    goal_y = enter goal y co-ordinate       %1000
    rpm_l = enter the left wheel RPM        %3
    rpm_r =enter the right wheel RPM        %8
    clearance =enter the clearance of the robot %100
 ## Output-
 ## All Explored Nodes
   <img src="https://github.com/AkshayKurhade/ENPM661Project3Phase3and4/blob/master/Output/Explored%20path.png" width="480">
 # BacktrackedPath
   <img src="https://github.com/AkshayKurhade/ENPM661Project3Phase3and4/blob/master/Output/backtracked_path.png" width="480">
 
   

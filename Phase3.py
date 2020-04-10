import numpy as np
import math
import cv2
import matplotlib.pyplot as plt
from Worldmap import *

userdefined = False
if userdefined:
    start_x, start_y, start_orient = input("enter start co-ordinates and orientation").split()
    goal_x, goal_y = input("enter goal co-ordinates").split()
    rpm_left, rpm_right = input("enter the wheel RPM").split()
    clearance = input("enter the clearance of the robot")
else:
    start_x, start_y, start_orient = [10, 10, 30]
    goal_x, goal_y = [1010, 1010]
    rpm_left, rpm_right = [4, 4]
    clearance = 5
radius = 0.4  # From Datasheet

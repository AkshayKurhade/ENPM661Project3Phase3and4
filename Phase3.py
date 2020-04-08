import numpy as np
import math
import cv2
import matplotlib.pyplot as plt

userdefined = False
if userdefined:
    start_x, start_y, start_orient = input("enter start co-ordinates and orientation")
    goal_x, goal_y = input("enter goal co-ordinates")
    rpm_left, rpm_right = input("enter the wheel RPM")
    clearance = input("enter the clearance of the robot")
else:
    start_x, start_y, start_orient = [10, 10, 30]
    goal_x, goal_y = [1010, 1010]
    rpm_left, rpm_right = [4, 4]
    clearance = 5
radius = 0.4  # From Datasheet


def checkifobstacle(node):
    global radius, clearance
    x = node[0]
    y = node[1]

    # center circle
    if (x - 510) ** 2 + (y - 510) ** 2 <= (100 + radius + clearance) ** 2:
        return False

    # top circle
    elif (x - 710) ** 2 + (y - 810) ** 2 <= (100 + radius + clearance) ** 2:
        return False

    # bottom right circle
    elif (x - 710) ** 2 + (y - 210) ** 2 <= (100 + radius + clearance) ** 2:
        return False

    # bottom left circle
    elif (x - 310) ** 2 + (y - 210) ** 2 <= (100 + radius + clearance) ** 2:
        return False

    # left square
    elif 35 - radius - clearance <= x <= 185 + radius + clearance and 435 - radius - clearance <= y <= 585 + radius + clearance:
        return False

    # right square
    elif 835 - radius - clearance <= x <= 985 + radius + clearance and 435 - radius - clearance <= y <= 585 + radius + clearance:
        return False
    # top left square
    elif 235 - radius - clearance <= x <= 385 + radius + clearance and 735 - radius - clearance <= y <= 885 + radius + clearance:
        return False

    else:

        return True

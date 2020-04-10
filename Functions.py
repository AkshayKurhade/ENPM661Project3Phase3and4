import math
import heapq
import matplotlib.pyplot as plt
from Worldmap import *


def ActionSet(curr_node, orientation_facing, RPM_L, RPM_R):
    global time_run
    # Values From Datasheet
    r = 3.8
    L = 35
    t = 0
    dt = 0.1
    new_x = curr_node[0]
    new_y = curr_node[1]
    theta_new = 3.14 * orientation_facing / 180
    # calculate right and left wheel velocities using RPM
    ul = r * RPM_L * 0.10472
    ur = r * RPM_R * 0.10472
    time_run = 1
    while t < time_run:
        t = t + dt
        curr_start_x = new_x
        curr_start_y = new_y
        new_x += (r / 2) * (ul + ur) * math.cos(theta_new) * dt
        new_y += (r / 2) * (ul + ur) * math.sin(theta_new) * dt
        theta_new += (r / L) * (ur - ul) * dt

    new_final_orientation = 180 * (theta_new) / 3.14
    # calculating the degrees rotated   from the start to the new orientation and assigning costs accplordingly
    degrees_rotated = abs(orientation_facing - new_final_orientation)
    degrees_rotated = abs(degrees_rotated % 360)
    cost = 10 + (10 * degrees_rotated / 360)
    #     new_final_orientation = round(new_final_orientation,2)
    new_final_orientation = 15 * round(new_final_orientation / 15)
    new_node = ((round(new_x, 2), round(new_y, 2)), new_final_orientation, cost)
    same_out = (curr_node, orientation_facing, 100000)
    if 0.00 <= new_node[0][0] <= 1020.00 and 0.00 <= new_node[0][1] <= 1020.00:
        return new_node, True
    else:
        return same_out, False


def generateGraph(point, degree, rpm_l,
                  rpm_r):  # remember that this size_x and size_y are the sizes of the matrix, so not the end coordinates
    list_of_points_for_graph = []
    size_x, size_y = 1021, 1021
    global RPM_R
    global RPM_L

    i = point[0]  # x coordinate
    j = point[1]  # y coordinate

    if i <= size_x and j <= size_y and i >= 0 and j >= 0:

        all_neighbours = {}

        pos1 = ActionSet(point, degree, 0, rpm_l)[0]
        pos2 = ActionSet(point, degree, rpm_l, 0)[0]
        pos3 = ActionSet(point, degree, rpm_l, rpm_l)[0]
        pos4 = ActionSet(point, degree, 0, rpm_r)[0]
        pos5 = ActionSet(point, degree, rpm_r, 0)[0]
        pos6 = ActionSet(point, degree, rpm_r, rpm_r)[0]
        pos7 = ActionSet(point, degree, rpm_r, rpm_r)[0]
        pos8 = ActionSet(point, degree, rpm_r, rpm_r)[0]

        if pos1[0][0] >= 0 and pos1[0][1] >= 0 and pos1[0][0] <= size_x and pos1[0][1] <= size_y:
            all_neighbours[pos1[0]] = (round(pos1[2], 2), pos1[1])

        if pos2[0][0] >= 0 and pos2[0][1] >= 0 and pos2[0][0] <= size_x and pos2[0][1] <= size_y:
            all_neighbours[pos2[0]] = (round(pos2[2], 2), pos2[1])

        if pos3[0][0] >= 0 and pos3[0][1] >= 0 and pos3[0][0] <= size_x and pos3[0][1] <= size_y:
            all_neighbours[pos3[0]] = (round(pos3[2], 2), pos3[1])

        if pos4[0][0] >= 0 and pos4[0][1] >= 0 and pos4[0][0] <= size_x and pos4[0][1] <= size_y:
            all_neighbours[pos1[0]] = (round(pos4[2], 2), pos4[1])

        if pos5[0][0] >= 0 and pos5[0][1] >= 0 and pos5[0][0] <= size_x and pos5[0][1] <= size_y:
            all_neighbours[pos5[0]] = (round(pos5[2], 2), pos5[1])

        if pos6[0][0] >= 0 and pos6[0][1] >= 0 and pos6[0][0] <= size_x and pos6[0][1] <= size_y:
            all_neighbours[pos6[0]] = (round(pos6[2], 2), pos6[1])

        if pos7[0][0] >= 0 and pos7[0][1] >= 0 and pos7[0][0] <= size_x and pos7[0][1] <= size_y:
            all_neighbours[pos7[0]] = (round(pos7[2], 2), pos7[1])

        if pos8[0][0] >= 0 and pos8[0][1] >= 0 and pos8[0][0] <= size_x and pos8[0][1] <= size_y:
            all_neighbours[pos8[0]] = (round(pos8[2], 2), pos8[1])

        return all_neighbours

    else:

        pass


def EucledianDistance(node1, node2):
    x1 = node1[0]
    x2 = node2[0]
    y1 = node1[1]
    y2 = node2[1]
    dist = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)

    # dist = Round2Point5(dist)
    return dist


def plot_curve(X0, Y0, Theta0, RPM_L, RPM_R):
    global time_run
    r = 0.038 * 100
    L = 0.35 * 100
    t = 0
    dt = 0.1
    new_x = X0
    new_y = Y0
    theta_new = 3.14 * Theta0 / 180
    # calculate right and left wheel velocities using RPM
    ul = r * RPM_L * 0.10472
    ur = r * RPM_R * 0.10472
    while t < time_run:
        t = t + dt
        X0 = new_x
        Y0 = new_y
        new_x += (r / 2) * (ul + ur) * math.cos(theta_new) * dt
        new_y += (r / 2) * (ul + ur) * math.sin(theta_new) * dt
        theta_new += (r / L) * (ur - ul) * dt
        plt.plot([X0, new_x], [Y0, new_y], color="blue")

    new_final_orientation = 180 * (theta_new) / 3.14
    return new_x, new_y, new_final_orientation


point_and_angle_list = []


def BackTrack(backtracking_dict, goal, start):  # goal is the starting point now and start is the goal point now

    # initializing the backtracked list
    back_track_list = []
    # appending the start variable to the back_track_list list
    back_track_list.append(start)
    # while the goal is not found

    while goal != []:
        # for key and values in the backtracking dictionary
        for k, v in backtracking_dict.items():

            # for the key and values in the values, v
            for k2, v2 in v.items():
                # checking if the first key is the start
                if k == start:

                    # checking if not in the backtrackedlist

                    if v2[0] not in back_track_list:
                        back_track_list.append(start)
                        point_and_angle_list.append((start, v2[1]))
                    # updating the start variable
                    start = v2[0]

                    # checking if it is the goal
                    if v2[0] == goal:
                        goal = []
                        break
                        # returns the backtracked list
    return (back_track_list)


def Round2Point5(num):
    return (round(num * 2) / 2)


def a_star_Algorithm(start, goal, start_orientation, obstacle_list, radius, clearance, rpm_l, rpm_r):
    visited = []
    orientation_to_layer = {0: 0, 15: 1, 30: 2, 45: 3, 60: 4, 75: 5, 90: 6, 105: 7, 120: 8, 135: 9, 150: 10, 165: 11,
                            180: 12,
                            195: 13, 210: 14, 225: 15, 240: 16, 255: 17, 270: 18, 285: 19, 300: 20, 315: 21, 330: 22,
                            345: 23, 360: 24}

    cost_from = np.array(np.ones((2041, 2041, 24)) * np.inf)
    visited_array = np.zeros((2041, 2041, 24))
    heur = np.array(np.ones((2041, 2041)) * np.inf)
    f = np.array(np.ones((2041, 2041, 24)) * np.inf)
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, start_orientation))
    # initialize cost  for start node to zero
    cost_from[int(2 * start[0])][int(2 * start[1])][orientation_to_layer[start_orientation]] = 0
    f[int(2 * start[0])][int(2 * start[1])][orientation_to_layer[start_orientation]] = 0

    pts_quivgraph = []
    break_while = 0
    backtracking = {}

    if goal in obstacle_list or start in obstacle_list:
        print("Start or goal points are in the obstacle")
        return False

    else:
        while True:
            if break_while == 1:
                break
            _, current_node, curr_orient = heapq.heappop(priority_queue)
            # append visited nodes
            visited.append(current_node)
            pts_quivgraph.append((current_node, curr_orient))

            if ((current_node[0] - goal[0]) ** 2 + (current_node[1] - goal[1]) ** 2 <= (10) ** 2):
                print("Found Goal")
                break
            # check whether node is in the obstacle space
            if checkifobstacle(current_node, radius, clearance) == True:
                # generate neighbours
                graph = generateGraph(current_node, curr_orient, rpm_l, rpm_r)
                graph_list = []
                # put neighbours in a list for easy access
                for key, cost_value in graph.items():
                    graph_list.append((key, cost_value))
                for neighbour, cost in graph_list:
                    this_cost = graph[neighbour][0]
                    breakflag = 0
                    orientation = graph[neighbour][1]
                    orientation = orientation % 360

                    rounded_neighbour = (Round2Point5(neighbour[0]), Round2Point5(neighbour[1]))
                    if rounded_neighbour in visited:
                        breakflag = 1
                        # exit if found
                    if breakflag == 1:
                        continue
                    # check if this neighbour is goal
                    if ((rounded_neighbour[0] - goal[0]) ** 2 + (rounded_neighbour[1] - goal[1]) ** 2 <= (10) ** 2):
                        print("Reached the goal")
                        break_while = 1
                        break

                    if checkifobstacle(rounded_neighbour, radius, clearance) == True:
                        # check if visited
                        if visited_array[int(2 * rounded_neighbour[0])][int(2 * rounded_neighbour[1])][
                            orientation_to_layer[orientation]] == 0:
                            # if not, make it visited
                            visited_array[int(2 * rounded_neighbour[0])][int(2 * rounded_neighbour[1])][
                                orientation_to_layer[orientation]] = 1
                            # calculate cost from
                            cost_from[int(2 * rounded_neighbour[0])][int(2 * rounded_neighbour[1])][
                                orientation_to_layer[int(orientation)]] = (
                                    this_cost + cost_from[int(2 * current_node[0])][int(2 * current_node[1])][
                                orientation_to_layer[curr_orient]])
                            # calculate cost to go values
                            heur[int(2 * rounded_neighbour[0])][int(2 * rounded_neighbour[1])] = EucledianDistance(
                                rounded_neighbour, goal)
                            # calculate f = g+h
                            f[int(2 * rounded_neighbour[0])][int(2 * rounded_neighbour[1])][
                                orientation_to_layer[orientation]] = \
                                cost_from[int(2 * rounded_neighbour[0])][int(2 * rounded_neighbour[1])][
                                    orientation_to_layer[orientation]] + heur[int(2 * rounded_neighbour[0])][
                                    int(2 * rounded_neighbour[1])]
                            # push to the explored node queue
                            heapq.heappush(priority_queue, (
                                f[int(2 * rounded_neighbour[0])][int(2 * rounded_neighbour[1])][
                                    orientation_to_layer[orientation]], rounded_neighbour, orientation))
                            backtracking[rounded_neighbour] = {}
                            # adding to the backtracking dictionary
                            backtracking[rounded_neighbour][
                                f[int(2 * rounded_neighbour[0])][int(2 * rounded_neighbour[1])][
                                    orientation_to_layer[orientation]]] = (current_node, curr_orient)
                        else:
                            # if visited, check cost. if newly genrated neighbour has a lower cost, update it
                            if (f[int(2 * rounded_neighbour[0])][int(2 * rounded_neighbour[1])][
                                orientation_to_layer[orientation]]) > (
                                    f[int(2 * current_node[0])][int(2 * current_node[1])][
                                        orientation_to_layer[curr_orient]]):
                                f[int(2 * rounded_neighbour[0])][int(2 * rounded_neighbour[1])][
                                    orientation_to_layer[orientation]] = (
                                    f[int(2 * current_node[0])][int(2 * current_node[1])][
                                        orientation_to_layer[curr_orient]])
                                backtracking[rounded_neighbour][
                                    f[int(2 * rounded_neighbour[0])][int(2 * rounded_neighbour[1])][
                                        orientation_to_layer[orientation]]] = (current_node, curr_orient)

    return current_node, backtracking, visited, pts_quivgraph
    # return the last parent node and backtracked dictionary

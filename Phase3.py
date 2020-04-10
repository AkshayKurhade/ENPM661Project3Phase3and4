import cv2
import matplotlib.pyplot as plt
from Worldmap import *
from Functions import *
import time

print(
    "This project plans a path for the TurtleBot taking into consideration its holonomic constraints \n and uses Astar algorithm to solve the obstacle space")
print("All the Parameters are Pre-configured, to test a custom configuration set the 'userdefined' flag to True")
userdefined = False
if userdefined:
    start_x = float(input("enter start x co-ordinate"))
    start_y = float(input("enter start y co-ordinate"))
    start_orient = float(input("enter start orientation"))
    goal_x = float(input("enter goal x co-ordinate"))
    goal_y = float(input("enter goal y co-ordinate"))
    rpm_l = input("enter the left wheel RPM")
    rpm_r = input("enter the right wheel RPM")
    clearance = input("enter the clearance of the robot")

else:
    start_x = 60
    start_y = 60
    start_orient = 30
    goal_x = 1000
    goal_y = 1000
    rpm_l = 3
    rpm_r = 8
    clearance = 10

radius = 35  # From Datasheet
start = (int(start_x + radius + clearance), int(start_y + radius + clearance))
goal = (int(goal_x - radius - clearance), int(goal_y - radius - clearance))
# Create a list of obstacles
obstacle_list = obstaclespace(radius, clearance)
if start in obstacle_list:
    print("point start in obstacle")
elif goal in obstacle_list:
    print("goal in obstacle")
else:
    new_canvas, map_points = worldmap()
    cv2.imshow("world", new_canvas)
    cv2.imwrite("Map.png",new_canvas)
    cv2.waitKey(20)
    start_time = time.time()

    # A star algorithm fitted to holonomic constrains of Turtlebot
    new_goal_rounded, backtracking_dict, visited, quiver_list = a_star_Algorithm(start, goal, start_orient,
                                                                                 obstacle_list, radius, clearance,
                                                                                 rpm_l, rpm_r)
    print("Took ", round(time.time() - start_time, 2), "seconds to solve.(Fast ain't it?)")

    # Backtracking back to the goal
    backtracked_final = BackTrack(backtracking_dict, start, new_goal_rounded)
    # printing the nodes from initial to the end
    backtracked_path = []
    for backtr in backtracked_final:
        backtracked_path.append(((round(((backtr[0] / 100) - 5.1), 2)), (round(((backtr[1] / 100) - 5.1), 2))))
    np.savetxt('backtrackedpath.txt', backtracked_path, delimiter=',')
    print("Backtracked_path=", backtracked_path)
    new_list_visited = []
    for visited_node in visited:
        new_x = visited_node[0] * 2
        new_y = visited_node[1] * 2
        new_list_visited.append((new_x, new_y))

    new_backtracked = []
    for back in backtracked_final:
        new_x_b = back[0] * 2
        new_y_b = back[1] * 2
        new_backtracked.append((new_x_b, new_y_b))

    # #defining a blank canvas
    new_canvas = np.zeros((2040, 2040, 3), np.uint8)

    # for every point that belongs within the obstacle
    for c in map_points:  # change the name of the variable l
        x = 2 * c[1]
        y = 2 * c[0]
        new_canvas[(x, y)] = [255, 255, 255]

    # flipping the image for correct orientation
    new_canvas = np.flipud(new_canvas)
    # making a copy for backtracking purpose
    new_canvas_copy_backtrack = new_canvas.copy()
    new_canvas_copy_visited = new_canvas.copy()
    out = cv2.VideoWriter('Phase3Output.avi', cv2.VideoWriter_fourcc(*'XVID'), 15, (1020, 1020))
    # visited path
    for visit_path in new_list_visited:
        # print(path)
        x = int(visit_path[0])
        y = int(visit_path[1])

        cv2.circle(new_canvas_copy_visited, (x, 2040 - y), 5, [255, 0, 0], -1)
        resized_visited = cv2.resize(new_canvas_copy_visited, (1020, 1020))
        out.write(resized_visited)
        cv2.imshow('Explored Path', resized_visited)
        cv2.waitKey(10)
    cv2.destroyAllWindows()

    for path in new_backtracked:
        # print(path)
        x = int(path[0])
        y = int(path[1])
        cv2.circle(new_canvas_copy_visited, (x, 2040 - y), 5, [0, 0, 255], -1)
        resized_backtrack = cv2.resize(new_canvas_copy_visited, (1020, 1020))
        out.write(resized_backtrack)
        cv2.imshow('resized', resized_backtrack)
        cv2.waitKey(10)
    out.release()
    cv2.destroyAllWindows()

    # show visited path
    cv2.imshow('Explored', resized_visited)
    cv2.imwrite('Explored path.png', resized_visited)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # show backtracked path

    cv2.imshow("Backtracked path", resized_backtrack)
    cv2.imwrite('backtracked_path.png', resized_backtrack)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # final quiver plot

    fig, ax = plt.subplots()
    RPM1 = rpm_l
    RPM2 = rpm_r

    actions = [[0, RPM1],
               [RPM1, 0],
               [RPM1, RPM1],
               [0, RPM2],
               [RPM2, 0],
               [RPM2, RPM2],
               [RPM1, RPM2],
               [RPM2, RPM1]]

    count = 0
    # for point in point_and_angle_list:
    for point in quiver_list:
        x = point[0][0]
        y = point[0][1]
        theta = point[1]
        for action in actions:
            X1 = plot_curve(x, y, theta, action[0], action[1])
        count += 1
    plt.grid()
    ax.set_aspect('equal')
    plt.title('Path', fontsize=10)
    plt.savefig('Quiver.png')
    plt.show()
    time.sleep(10)
    plt.close()

import numpy as np


def obstaclespace(radius, clearance):
    worldmap_list = []
    obstacle_list = []
    for i in range(0, 1021):  # 1020 width
        for j in range(0, 1021):  # 1020 width
            worldmap_list.append((i, j))  # appending

    for pt in worldmap_list:
        x = pt[0]
        y = pt[1]

        # center Circle
        if (x - 510) ** 2 + (y - 510) ** 2 <= (100 + radius + clearance) ** 2:
            obstacle_list.append((x, y))

        # top right circle
        if (x - 710) ** 2 + (y - 810) ** 2 <= (100 + radius + clearance) ** 2:
            obstacle_list.append((x, y))

        # Bottom Right Circle
        if (x - 710) ** 2 + (y - 210) ** 2 <= (100 + radius + clearance) ** 2:
            obstacle_list.append((x, y))

        # Bottom Left Circle
        if (x - 310) ** 2 + (y - 210) ** 2 <= (100 + radius + clearance) ** 2:
            obstacle_list.append((x, y))

        # Bounding Rectangle
        if 0 < x < 10 + radius + clearance:
            if 0 < y < 1020:
                obstacle_list.append((x, y))
        if 1010 - radius - clearance < x < 1020:
            if 0 < y < 1020:
                obstacle_list.append((x, y))
        if 10 < x < 1010:
            if 0 < y < 10 + radius + clearance:
                obstacle_list.append((x, y))
        if 10 < x < 1010:
            if 1010 - radius - clearance < y < 1020:
                obstacle_list.append((x, y))

        # left square
        if 35 - radius - clearance <= x <= 185 + radius + clearance:
            if 435 - radius - clearance <= y <= 585 + radius + clearance:
                obstacle_list.append((x, y))

        # right square
        if 835 - radius - clearance <= x <= 985 + radius + clearance:
            if 435 - radius - clearance <= y <= 585 + radius + clearance:
                obstacle_list.append((x, y))

        # top left square
        if 235 - radius - clearance <= x <= 385 + radius + clearance:
            if 735 - radius - clearance <= y <= 885 + radius + clearance:
                obstacle_list.append((x, y))
    return obstacle_list


def worldmap():
    worldmap_mat = []
    map_points = []
    # SCALING all by 100 times
    for i in range(0, 1020):  # 1020 width
        for j in range(0, 1020):  # 1020 width
            worldmap_mat.append((i, j))  # appending

    for pt in worldmap_mat:
        x = pt[0]
        y = pt[1]

        # Center Circle
        if (x - 510) ** 2 + (y - 510) ** 2 <= 100 ** 2:
            map_points.append((x, y))

        # Top Right Circle
        if (x - 710) ** 2 + (y - 810) ** 2 <= 100 ** 2:
            map_points.append((x, y))

        # Bottom Right Circle
        if (x - 710) ** 2 + (y - 210) ** 2 <= 100 ** 2:
            map_points.append((x, y))

        # Bottom left Circle
        if (x - 310) ** 2 + (y - 210) ** 2 <= 100 ** 2:
            map_points.append((x, y))

        # borders

        # left vertical border
        if 0 < x < 10:
            if 0 < y < 1020:
                map_points.append((x, y))

        # right vertical border
        if 1010 < x < 1020:
            if 0 < y < 1020:
                map_points.append((x, y))
        # bottom horizontal border
        if 10 < x < 1010:
            if 0 < y < 10:
                map_points.append((x, y))
        # top horizontal border
        if 10 < x < 1010:
            if 1010 < y < 1020:
                map_points.append((x, y))
        # left square
        if 35 <= x <= 185:
            if 435 <= y <= 585:
                map_points.append((x, y))

        # right square
        if 835 <= x <= 985:
            if 435 <= y <= 585:
                map_points.append((x, y))

        # top left square
        if 235 <= x <= 385:
            if 735 <= y <= 885:
                map_points.append((x, y))

    blank_image = np.zeros((1020, 1020, 3), np.uint8)

    for c in map_points:  # change the name of the variable l
        x = c[1]
        y = c[0]
        blank_image[(x, y)] = [255, 255, 255]  # assigning a yellow coloured pixel

    flipped_map = np.flipud(blank_image)

    return flipped_map, map_points


def checkifobstacle(node, radius, clearance):
    # global radius, clearance
    x = node[0]
    y = node[1]
    i = int(0)
    j = int(0)

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

    elif 0 < x < 10 + radius + clearance:
        if 0 < y < 1020:
            return False
    elif 1010 - radius - clearance < x < 1020:
        if 0 < y < 1020:
            return False
    elif 10 < x < 1010 and 0 < y < 10 + radius + clearance:
        if i <= 1021 and j <= 1021 and i >= 0 and j >= 0:
            return False
    elif 10 < x < 1010 and 1010 - radius - clearance < y < 1020:
        if 735 <= y <= 885:
            return False
    else:

        return True

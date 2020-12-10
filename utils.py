import math


# calculate angle based on distance between two points
def calculate_angle(curr_x, curr_y, target_x, target_y):
    # calculate distance
    distance = math.sqrt((target_x - curr_x) ** 2 + (target_y - curr_y) ** 2)
    if distance == 0:
        return 0
    # calculate angle with relative to horizontal line
    radian = math.asin((target_y - curr_y) / distance)
    degree = math.degrees(radian)
    return degree


# calculate command based on angle and distance between two points
def calculate_command(angle, curr_x, curr_y, target_x, target_y):
    # calculate distance
    distance = math.sqrt((target_x - curr_x) ** 2 + (target_y - curr_y) ** 2)
    # calculate angle with relative to horizontal line
    radian = math.asin((target_y - curr_y) / distance)
    degree = math.degrees(radian)
    # calculate angle difference
    angle_diff = degree - angle
    if angle_diff == 0:
        return "forward " + str(math.ceil(distance)), degree
    direction = "cw"
    if angle_diff < 0:
        angle_diff = 360 + angle_diff
    if angle_diff > 180:
        direction = "ccw"
        angle_diff -= 180
    return direction + " " + str(math.ceil(angle_diff)) + " forward " + str(math.ceil(distance)), degree

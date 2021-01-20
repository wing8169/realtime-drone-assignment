import math


# calculate distance
def calculate_dist(curr_x, curr_y, target_x, target_y):
    # calculate distance
    distance = math.sqrt((target_x - curr_x) ** 2 + (target_y - curr_y) ** 2)
    if distance == 0:
        return 0
    return distance


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
    # calculate angle of target point with respect to horizontal x-axis
    degree = 0
    if target_x == curr_x and target_y > curr_y:
        degree = 90
    elif target_x == curr_x and target_y < curr_y:
        degree = 270
    elif target_y == curr_y and target_x < curr_x:
        degree = 180
    elif target_x != curr_x and target_y != curr_y:
        radian = math.atan(abs(target_y - curr_y) / abs(target_x - curr_x))
        degree = math.degrees(radian)
        if target_x > curr_x and target_y < curr_y:
            degree = 360 - degree
        elif target_x < curr_x and target_y > curr_y:
            degree = 180 - degree
        elif target_x < curr_x and target_y < curr_y:
            degree = 180 + degree
    # convert negative current angle to positive angle
    tmp_angle = angle
    if angle < 0:
        tmp_angle = 360 + angle
    # calculate angle difference between target angle and current angle
    angle_diff = degree - tmp_angle
    if angle_diff == 0:
        return "forward " + str(math.ceil(distance)), degree
    direction = "cw"
    if angle_diff > 180:
        direction = "ccw"
        angle_diff = 360 - angle_diff
    elif angle_diff <= -180:
        angle_diff = 360 + angle_diff
    elif angle_diff < 0:
        angle_diff *= -1
        direction = "ccw"
    # convert to negative angle
    if degree > 180:
        degree = -(360-degree)
    return direction + " " + str(math.ceil(angle_diff)) + " forward " + str(math.ceil(distance)), degree

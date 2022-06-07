from openCV import *
from transfer import *
from parameters import *

import cv2
import time


def get_coordinates(ball_center, origin):
    if not (ball_center is None or origin is None):
        x = 0
        y = 1
        difference = [int(ball_center[x]) - int(origin[x]), -(int(ball_center[y]) - int(origin[y]))]
    else:
        difference = [0,0 ]
    return difference


def get_difference(minuend, subtrahend):
    if not (minuend is None or subtrahend is None):
        difference = [int(minuend[0]) - int(subtrahend[0]), int(minuend[1]) - int(subtrahend[1])]
    else:
        difference = 0
    return difference


def rebound(value, min_value, max_value, low_bound, high_bound):
    if max_value == min_value:
        return min_value
    if value >= max_value:
        return high_bound
    if value <= min_value:
        return low_bound
    return (value - min_value) / (max_value - min_value) * (high_bound - low_bound) + low_bound


# main_function
cap = cv2.VideoCapture(0)
target_point = [0, 0]
error = [0, 0]

kp = 0.1
ki = 0.0
kd = 0.2

prev_time = 0
prev_value = [0, 0]
while True:
    check_quit()
    success, img = cap.read()
    set_frame(img)

    height = 4
    width = 3
    cap.set(width, 400)
    cap.set(height, 400)

    ball_center = find_ball(ball_color)
    origin = find_platform(platform_color)
    coordinates = get_coordinates(ball_center, origin)

    #print(coordinates)
    error = [0, 0]
    if coordinates is not None:
        error = coordinates[0] * kp + kd * (-error[0] + prev_value[0]), \
                coordinates[1] * kp + kd * (-error[1] + prev_value[0])

    #print(error[0], prev_value[0])


    angle = [90, 90]

    #print(error[0])
    angle[0] = int(rebound(error[0], -70, 70, 170, 10))
    angle[1] = int(rebound(error[1], -70, 70, 175, 15))
    print(angle)
    transfer_coordinates(angle)

    prev_value = error
    error = [0,0]

    cv2.imshow('video', img)


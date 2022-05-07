from openCV import *
from transfer import *
from parameters import *

import cv2

cap = cv2.VideoCapture(1)
while True:
    check_quit()
    success, img = cap.read()
    set_frame(img)

    # height = 4
    # width = 3
    # # cap.set(width, 400)
    # # cap.set(height, 300)

    ball_center = find_ball(ball_color)
    origin = find_platform(platform_color)
    ball_relative_coordinates = get_coordinates(ball_center, origin)
    if ball_relative_coordinates is not None:
        transfer_coordinates(ball_relative_coordinates)
        print(origin, ball_center, ball_relative_coordinates)
    cv2.imshow('video', img)


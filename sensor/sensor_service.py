from openCV import *
from transfer import *
from parameters import *

import cv2

cap = cv2.VideoCapture(1)
ball_center = (0,0)
while True:
    check_quit()
    success, img = cap.read()
    set_frame(img)

    # height = 4
    # width = 3
    # # cap.set(width, 400)
    # # cap.set(height, 300)

    coordinates = find_ball(ball_color)
    #origin = find_platform(platform_color)
    #ball_relative_coordinates = get_coordinates(ball_center, origin)
    if coordinates is not None:
        ball_center = coordinates
    transfer_coordinates(ball_center)
    print(ball_center)
    cv2.imshow('video', img)



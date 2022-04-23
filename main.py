import cv2
import numpy as np
import math


def check_quit():
    if cv2.waitKey(1) & 0xFF == ord('q'):
        exit(0)


def make_mask(color):
    global img
    global COLOR_RANGE

    hsv_min = COLOR_RANGE[color][0]
    hsv_max = COLOR_RANGE[color][1]

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    st1 = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 21), (10, 10))
    st2 = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11), (5, 5))
    thresh = cv2.inRange(hsv, hsv_min, hsv_max)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, st1)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, st2)
    thresh = cv2.GaussianBlur(thresh, (5, 5), 2)
    return thresh


def find_circle_center(color, frame_name, bound_color):
    thresh = make_mask(color)
    cv2.imshow(frame_name, thresh)
    circles = cv2.HoughCircles(thresh.copy(), cv2.HOUGH_GRADIENT, 1, 20, 50, 30, 29, 0)
    circles = np.uint16(np.around(circles))

    circle = circles[0, 0]
    try:
        center_x = circle[0]
        center_y = circle[1]
        circle_radius = circle[2]
        cv2.circle(img, (center_x, center_y), circle_radius, bound_color, 2)
        # нарисовать центры окружностей
        cv2.circle(img, (center_x, center_y), 2, (0, 0, 255), 3)
        return center_x, center_y

    except IndexError:
        x = 5


def get_square(box):
    x = 0
    y = 1
    square = ((box[0][x] - box[1][x]) ** 2 + (box[0][y] - box[1][y]) ** 2) * \
             ((box[1][x] - box[2][x]) ** 2 + (box[1][y] - box[2][y]) ** 2)
    return square


# def draw_rectangle(color):
#     thresh = make_mask(color)
#     cv2.imshow('field detection', thresh)
#
#     contours0, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     field = [[0, 0], [0, 0], [0, 0], [0, 0]]
#     for cnt in contours0:
#         try:
#             rect = cv2.minAreaRect(cnt)  # пытаемся вписать прямоугольник
#             box = cv2.boxPoints(rect)  # поиск четырех вершин прямоугольника
#
#             if box is not None and get_square(box) > get_square(field):
#                 field = box
#         except IndexError:
#             x = 5
#     field = np.int0(field)  # округление координат
#     cv2.drawContours(img, [field], 0, (200, 0, 0), 2)  # рисуем прямоугольник


# Main function
COLOR_RANGE = {
    'ball_light': (np.array((20, 70, 170), np.uint8), np.array((255, 255, 255), np.uint8)),
    'ball_dark': (np.array((0, 170, 120), np.uint8), np.array((20, 240, 255), np.uint8)),
    'ball_orange': (np.array((0, 153, 100), np.uint8), np.array((153, 255, 255), np.uint8)),
    'field_black': (np.array((15, 15, 15), np.uint8), np.array((100, 100, 100), np.uint8)),
    'ball_green': (np.array((40, 70, 40), np.uint8), np.array((225, 255, 225), np.uint8)),
    'white': (np.array((0, 0, 150), np.uint8), np.array((255, 50, 255), np.uint8)),
}


def find_platform(color):
    blue = (200, 0, 0)
    return find_circle_center(color, 'platform detection', blue)


def find_ball(color):
    green = (0, 200, 0)
    return find_circle_center(color, 'ball detection', green)


cap = cv2.VideoCapture(0)

while True:
    check_quit()
    success, img = cap.read()
    height = 4
    width = 3
    # cap.set(width, 400)
    # cap.set(height, 300)
    ball_center = find_ball('ball_green')
    origin = find_platform('white')

    if not (ball_center is None or origin is None):
        x = 0
        y = 1
        ball_coordinates = int(ball_center[x]) - int(origin[x]), -(int(ball_center[y]) - int(origin[y]))
    else:
        ball_coordinates = None

    print(origin, ball_center, ball_coordinates)
    cv2.imshow('video', img)

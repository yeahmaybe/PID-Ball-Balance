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


def draw_ball():
    thresh = make_mask('ball_orange')
    cv2.imshow('ball detection', thresh)
    circles = cv2.HoughCircles(thresh.copy(), cv2.HOUGH_GRADIENT, 1, 20, 50, 30, 29, 0)
    circles = np.uint16(np.around(circles))

    circle = circles[0, 0]
    try:
        center_x = circle[0]
        center_y = circle[1]
        circle_radius = circle[2]
        cv2.circle(img, (center_x, center_y), circle_radius, (0, 255, 0), 2)
        # нарисовать центры окружностей
        cv2.circle(img, (center_x, center_y), 2, (0, 0, 255), 3)

    except IndexError:
        x = 5


def get_square(box):
    x = 0
    y = 1
    square = ((box[0][x]-box[1][x]) ** 2 + (box[0][y]-box[1][y])**2) * \
             ((box[1][x] - box[2][x]) ** 2 + (box[1][y] - box[2][y]) ** 2)
    return square


def draw_field():
    thresh = make_mask('field_black')
    cv2.imshow('field detection', thresh)

    contours0, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    field = [[0, 0], [0, 0], [0, 0], [0, 0]]
    for cnt in contours0:
        try:
            rect = cv2.minAreaRect(cnt)  # пытаемся вписать прямоугольник
            box = cv2.boxPoints(rect)  # поиск четырех вершин прямоугольника

            if box is not None and get_square(box) > get_square(field):
                field = box
        except IndexError:
            x = 5
    field = np.int0(field)  # округление координат
    cv2.drawContours(img, [field], 0, (200, 0, 0), 2)  # рисуем прямоугольник


# Main function
COLOR_RANGE = {
    'ball_light': (np.array((20, 70, 170), np.uint8), np.array((255, 255, 255), np.uint8)),
    'ball_dark': (np.array((0, 170, 120), np.uint8), np.array((20, 240, 255), np.uint8)),
    'ball_orange': (np.array((0, 153, 100), np.uint8), np.array((153, 255, 255), np.uint8)),
    'field_black': (np.array((15, 15, 15), np.uint8), np.array((100, 100, 100), np.uint8)),
}
cap = cv2.VideoCapture(1)
while True:
    check_quit()
    success, img = cap.read()
    height = 4
    width = 3
    cap.set(width, 400)
    cap.set(height, 300)
    draw_ball()
    draw_field()

    cv2.imshow('video', img)

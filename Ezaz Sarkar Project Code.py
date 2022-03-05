import cv2
import numpy as np
from random import *
canvas = np.zeros([700, 700, 3])
snake_lst = [[200, 200]]
x = 200
y = 200
cv2.circle(canvas, snake_lst[0], 10, (255, 255, 0), -1)
cv2.putText(canvas, "W: Up  S: Down  A: Left  D: Right", (80, 660), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 6)
game = True
k = None
left = False
up = False
down = False
right = False
food = False
F_x = int(5 + (random() * 15)) * 20
F_y = int(5 + (random() * 15)) * 20
while True:
    cv2.rectangle(canvas, (70, 70), (630, 630), (255, 255, 255), 1)
    cv2.rectangle(canvas, (0, 0), (700, 60), (0, 0, 0), -1)
    if game:
        cv2.putText(canvas, f"SCORE: {len(snake_lst) -1}", (10, 45), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)
    else:
        cv2.putText(canvas, f"  !!GAME OVER!!  FINAL SCORE: {len(snake_lst) - 1}", (50, 45), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 4)
        break
    cv2.circle(canvas, [F_x, F_y], 10, (0, 0, 255), -1)
    if k == ord('d'):
        left = False
        up = False
        down = False
        right = True
    if k == ord('a'):
        left = True
        up = False
        down = False
        right = False
    if k == ord('w'):
        left = False
        up = True
        down = False
        right = False
    if k == ord('s'):
        left = False
        up = False
        down = True
        right = False
    if right:
        x += 20
        if x > 630:
            x = x-630 + 70
        snake_lst.insert(0, [x, y])
        if abs(x - F_x) < 20 and abs(y - F_y) < 20:
            food = True
            cv2.circle(canvas, [F_x, F_y], 10, (0, 0, 0), -1)
            F_x = int(5 + (random() * 25)) * 20
            F_y = int(5 + (random() * 25)) * 20
        else:
            food = False
        cv2.circle(canvas, snake_lst[0], 10, (255, 255, 0), -1)

    elif left:
        x -= 20
        if x-70 < 0:
            x = x - 70 + 630
        snake_lst.insert(0, [x, y])
        if abs(x - F_x) < 20 and abs(y - F_y) < 20:
            food = True
            cv2.circle(canvas, [F_x, F_y], 10, (0, 0, 0), -1)
            F_x = int(5 + (random() * 15)) * 20
            F_y = int(5 + (random() * 15)) * 20
        else:
            food = False
        cv2.circle(canvas, snake_lst[0], 10, (255, 255, 0), -1)
    elif down:
        y += 20
        if y > 630:
            y = y-630 + 70
        snake_lst.insert(0, [x, y])
        if abs(x - F_x) < 20 and abs(y - F_y) < 20:
            food = True
            cv2.circle(canvas, [F_x, F_y], 10, (0, 0, 0), -1)
            F_x = int(5 + (random() * 15)) * 20
            F_y = int(5 + (random() * 15)) * 20
        else:
            food = False
        cv2.circle(canvas, snake_lst[0], 10, (255, 255, 0), -1)
    elif up:
        y -= 20
        if y-70 < 0:
            y = y - 70 + 630
        snake_lst.insert(0, [x, y])
        if abs(x - F_x) < 20 and abs(y - F_y) < 20:
            food = True
            cv2.circle(canvas, [F_x, F_y], 10, (0, 0, 0), -1)
            F_x = int(5 + (random() * 15)) * 20
            F_y = int(5 + (random() * 15)) * 20
        else:
            food = False
        cv2.circle(canvas, snake_lst[0], 10, (255, 255, 0), -1)

    if len(snake_lst) > 1:
        if not food:
            cv2.circle(canvas, snake_lst[-1], 10, (0, 0, 0), -1)
            snake_lst.pop(-1)

    for i in range(1, len(snake_lst)):
        if x == snake_lst[i][0] and y == snake_lst[i][1]:
            game = False

    cv2.imshow("saurav", canvas)
    k = cv2.waitKey(100)

for node in snake_lst:
    cv2.circle(canvas, node, 10, (0.5, 0.5, 0.5), -1)

while True:
    cv2.imshow("game", canvas)
    cv2.waitKey(1)
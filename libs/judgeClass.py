# -*- encoding: utf-8 -*-

import random
import time


def judgeClass():
    # week = time.localtime(time.time()).tm_wday + 1
    week = random.randint(1, 5)  # 测试
    hour = time.localtime(time.time()).tm_hour
    if hour >= 8 and hour < 10:
        hour = 1
    elif hour >= 10 and hour < 12:
        hour = 2
    elif hour >= 14 and hour < 16:
        hour = 3
    elif hour >= 16 and hour < 18:
        hour = 4
    else:
        hour = 5

    return str(week) + str(hour)

from Canvas import *
import math
import random
from typing import Union, List, Tuple

num = Union[int, float]


def oval_point_for_angle(
    cx: num, cy: num, rx: num, ry: num, theta: num
) -> Tuple[int, int]:
    return (
        cx + math.cos(theta) * rx,
        cy + math.sin(theta) * ry,
    )


def create_wheel(x1: num, y1: num, x2: num, y2: num, **kw) -> List[int]:
    """Wheel with eight spoke thingys"""
    rets = []
    rets.append(create_oval(x1, y1, x2, y2, **kw))
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    rx = (x2 - x1) / 2
    ry = (y2 - y1) / 2

    # across = whole 180 degrees = math.pi
    for i in range(0, 8):
        theta = math.pi / 8 * i
        rets.append(
            create_line(
                *oval_point_for_angle(cx, cy, rx, ry, theta),
                *oval_point_for_angle(cx, cy, rx, ry, theta + math.pi),
            )
        )

    return rets


def create_ngon(
    x1: num, y1: num, x2: num, y2: num, n: int, delta: float = 0.0, **kw
) -> List[int]:
    """
    Draw a "regular" n-gon, optionally stretched like an oval because
    everything is a nail when you have a hammer

    :param delta: angle offset
    """
    rets = []
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    rx = (x2 - x1) / 2
    ry = (y2 - y1) / 2
    prev_point = oval_point_for_angle(cx, cy, rx, ry, delta)
    this_point = None

    for i in range(1, n + 1):
        theta = 2 * math.pi / n * i
        this_point = oval_point_for_angle(cx, cy, rx, ry, theta + delta)
        rets.append(create_line(*prev_point, *this_point, **kw))
        prev_point = this_point

    return rets


# task 1
create_wheel(10, 10, 80, 90)

# task 2
for y in range(10, 111, 10):
    create_line(0, y, 100, y, fill="red")

# task 3 & 7
# no i don't wanna make it optional


def make_grid(x0: num, y0: num, xn: int, yn: int, w: num, h: num, **kw) -> List[int]:
    ret = []
    for ix in range(0, xn + 1):
        x = x0 + ix * w
        ret.append(create_line(x, y0, x, y0 + yn * h, **kw))
    for iy in range(0, yn + 1):
        y = y0 + iy * h
        ret.append(create_line(x0, y, x0 + xn * w, y, **kw))
    return ret


make_grid(100, 100, 5, 4, 30, 20, fill="purple")


# task 4
prev_p = (100, 100)
for _ in range(0, 10):
    # Integer? Not fun!
    length = random.random() * 50
    orientation = random.random() * math.pi * 2
    dp = (math.cos(orientation) * length, math.sin(orientation) * length)
    curr_p = tuple(sum(x) for x in zip(prev_p, dp))
    create_line(*prev_p, *curr_p, fill="#66ccff")
    prev_p = curr_p


# task 5
create_ngon(70, 70, 100, 100, 5, fill="green")
create_ngon(70, 70, 100, 100, 5, math.pi / 5, fill="#009f00")

# task 6
def create_ngon_differently(x0: num, y0: num, n: num, l: num, **kw):
    """
    :param l: length of each side
    """
    # Well ain't this embarassing...
    # Fine. Math.
    # Since delta = 0, then center is just (x0 - l, y0)
    # Then we have rx and ry
    # Poof that's it!
    cx = x0 - l
    cy = y0
    rx = ry = l
    # No I am too lazy to extend it for delta
    return create_ngon(cx - rx, cy - ry, cx + rx, cy + ry, n, **kw)


create_ngon_differently(100, 100, 3, 40, fill="pink")

# task 9a
def make_a_golden_spiral(x0: num, y0: num, n: num, a: num, dt: num, **kw) -> List[int]:
    ret = []
    golden_ratio = (1 + math.sqrt(5)) / 2
    prev_p = (x0, y0)
    for i in range(1, n + 1):
        t = dt * i
        r = a * math.e ** (golden_ratio * t)
        d = (math.cos(t) * r, math.sin(t) * r)
        curr_p = (x0 + d[0], y0 + d[1])
        ret.append(create_line(*prev_p, *curr_p, **kw))
        prev_p = curr_p


make_a_golden_spiral(100, 100, 20, 1, math.pi / 12, fill="#808080")

# task 9b
def create_nstar(
    x1: num, y1: num, x2: num, y2: num, n: int, delta: float = 0.0, **kw
) -> List[int]:
    """
    No I am not supposed to duplicate code but i did anyways

    :param delta: angle offset
    """
    rets = []
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    rx = (x2 - x1) / 2
    ry = (y2 - y1) / 2
    all_points = [
        oval_point_for_angle(cx, cy, rx, ry, 2 * math.pi / n * i + delta)
        for i in range(0, n)
    ]
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                continue
            rets.append(create_line(*all_points[i], *all_points[j], **kw))
    return rets


create_nstar(70, 70, 100, 100, 5, fill="blue")

complete()

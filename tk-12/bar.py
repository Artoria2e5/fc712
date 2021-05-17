from tkinter import *
from typing import List

# Stauffer et al, HCL Wizard diverging schemes Pastel 1 and Set 3
COLORS = """
#FFC5D0
#EAD1AB
#BBDEB1
#99E2D8
#B8D8F8
#EDC8F5
#FFB3B5
#F1B2EE
#AAC8FC
#61D8D6
#95D69A
#DAC584
""".split(
    "\n"
)[
    1:-1
]


def get_color_for_x(x: int) -> str:
    return COLORS[x % len(COLORS)]


# objs are as usual for easy cleanup, not that I intend to clean anything up
# It might be more pleasant to write as a generator (so yield instead of the
# very long objs.append()), but then it won't work when called plain
def barchart(
    xOrigin: int,
    yOrigin: int,
    xSize: int,
    ySize: int,
    labels: List[str],
    data: List[float],
) -> List[int]:
    o = []

    # Because the coordinate system does not make sense
    ySize = -ySize
    n = len(data)
    w = xSize / n
    maxd = max(data)
    h = ySize / maxd

    print(n, w, h, maxd)

    # Draw Axes first
    o.append(c.create_line(xOrigin, yOrigin, xOrigin, yOrigin + ySize))
    o.append(c.create_line(xOrigin, yOrigin, xOrigin + xSize, yOrigin))

    # Place labels and numbers
    for y_pt in range(0, maxd, 1):
        y = yOrigin + y_pt * h
        o.append(c.create_line(xOrigin, y, xOrigin - 10, y))
        o.append(c.create_text(xOrigin - 25, y, anchor="e", text=str(y_pt)))

    yt = yOrigin + ySize
    o.append(c.create_line(xOrigin, yt, xOrigin - 10, yt))
    o.append(c.create_text(xOrigin - 25, yt, anchor="e", text=str(maxd)))
    del yt

    for x_pt in range(0, n, 1):
        x = xOrigin + (x_pt + 0.5) * w
        o.append(c.create_text(x, yOrigin + 10, text=labels[x_pt]))

    # Draw boxes
    for (x_pt, y_pt) in enumerate(data):
        x = xOrigin + x_pt * w
        y = yOrigin + y_pt * h
        o.append(c.create_rectangle(x, yOrigin, x + w, y, fill=get_color_for_x(x_pt)))

    top.geometry(f"{xOrigin + xSize + 5}x{yOrigin + 20}")
    return o


top = Tk()
top.resizable(True, True)
c = Canvas(top)

# Example taken from the solution code.
# I changed the yScale here, since it disagrees with my reading of what it means.
# I would also argue for making the data a bunch of tuples instead.
barchart(
    100,
    750,
    1100,
    600,
    [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
        "M13",
    ],
    [
        10.4,
        15,
        26,
        12,
        20,
        8,
        16,
        18,
        23,
        20,
        11,
        17,
        23.5,
    ],
)
c.pack(fill="both", expand=True)


top.mainloop()
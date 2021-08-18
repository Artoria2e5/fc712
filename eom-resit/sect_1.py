#!/usr/bin/env python3
# I know typing is optional to Python.
# But it's not to my declining working memory.
from typing import *

# Not technically a tuple, but a list.  But Python doesn't care anyways!
Q1_COURSE_PASS_PROB = List[Tuple[str, float]]


def q1_pass(courses: Q1_COURSE_PASS_PROB):
    """Multiply together all probabilites to get the total prob."""
    probability = 1
    for _, pass_prob in courses:
        probability *= pass_prob

    # Return as a dictionary?? What??? How????
    return {"probability": probability}


def q2_dfact(n):
    """Return double-factorial of n, pretending n is odd."""
    # Note that the iteration order is reversed.  Doing it low to high
    # requires... I don't know, a CLOSURE??? an additional parameter???
    if n % 2 == 0:
        return q2_dfact(n - 1)
    if n == 1:
        return 1
    else:
        return n * q2_dfact(n - 2)


def q3_tkinter_counter():
    """Tkinter application with a self-incrementing counter/button."""
    import tkinter

    root = tkinter.Tk()
    root.title("Tkinter Counter")
    root.geometry("200x50")
    counter = tkinter.IntVar()
    counter.set(0)
    # It works, but on macOS the text is... white on a white button.
    # But the macOS tk is deprecated anyways, and it doesn't really
    # react to styling the way it's supposed to, so I'm going to forget
    # about it.
    # I think/hope it will look different on Windows.
    button = tkinter.Button(
        root, textvariable=counter, command=lambda: counter.set(counter.get() + 1)
    )
    button.pack()
    root.mainloop()


def q4_vowels(word: str) -> Dict[str, int]:
    """Count the number of vowels in a string."""
    count = {k: 0 for k in "aeiou"}
    for char in word:
        if char in count:
            count[char] += 1
    return count


STOP_WORDS = set(["a", "the", "this", "that", "he", "she", "it", "I", "by"])


def q5_stop_words(word: str) -> List[str]:
    """Remove stop words."""
    # Wrap with set() if you want to remove duplicates.
    return [word for word in word.split() if word not in STOP_WORDS]


def printify(func):
    """Decorator. Make function print the return value."""
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        print(val)
        return val
    return wrapper


@printify
def q6_collatz(n: int) -> List[int]:
    """Return collatz sequence until it get 1."""
    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        seq.append(n)
    return seq


def q7_population() -> None:
    """Print population of a town specified in towns.txt."""
    townlist: Dict[str, int] = {}
    try:
        with open("towns.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    town, pop = line.split(",")
                    townlist[town] = int(pop)
    except Exception as e:
        print("Oopsie doopsie the file is bad!")
        print(e)
        return
    
    # Print the population of the town.
    town = input("What town? ")
    print(townlist.get(town, "NOT FOUND"))

    # Get the total pop.  It's really as simple as sum(townlist.values()),
    # but you are asking for a loop.
    total_pop = 0
    for town, pop in townlist.items():
        total_pop += pop
    # If the total seems off, it's because I added some non-human... things
    # to towns.txt.
    print("total population: ", total_pop)


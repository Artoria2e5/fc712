# 2-1
def multiplication_table(n):
    # Okay, this uses the "unpack" syntax (I actually forgot what it's called).
    # Basically it fills in the arguments from an iterable, so that
    # `print(0, *[1, 2], 3)` is the same as `print(0, 1, 2, 3)`.
    # Figured that I should demonstrate I understand it!
    print(*range(n, n * 11, n))


multiplication_table(2)
# output:
# 2 4 6 8 10 12 14 16 18 20


for x in range(1, 11):
    multiplication_table(x)

# 2-3
def divisible_by_five(list):
    # I feel like I should explain this "generator comprehension" thing.
    # This one is the same as:
    #    for n in list:
    #        if n <= 120 and n % 5 == 0:
    #            yield n
    # Python people hold some serious pride in using this stuff instead
    # of everyone else's map and filter. Weirdos. ;)
    result = (n for n in list if n <= 120 and n % 5 == 0)
    print(*result, sep="\n")


divisible_by_five([12, 15, 32, 42, 55, 75, 120, 122, 132, 150, 180, 200])
# output:
# 15
# 55
# 75
# 120


# 2-4
def middle(s):
    # The // operator rounds down. It works like the / in the olden days of Python 2, but is more predictable.
    # Seriously, who on Earth decided that making a scripting language use C-like type rules is a good idea?
    halfway = len(s) // 2
    # As usual, ranges includes the left but not the right.
    return s[halfway - 1 : halfway + 2]


print(middle("GoFurnHat"))
# output:
# urn


# 2-5
# Finally the end of printing stuff. I am a bit allergic to only producing side effects.
def odd_and_even(list1, list2):
    # Use of the slicing syntax. The general form is [start:end:step],
    # and in this case we are:
    #   * Starting from the second (1) with step 2 to produce all odd results
    #   * Starting from the first (0) with step  to produce all even results
    return list1[1::2] + list2[::2]


print(odd_and_even([1, 3, 5, 7, 9, 10, 12, 13], ["John", "Sue", 4, "Banana", "Tiger"]))
# output:
# [3, 7, 10, 13, 'John', 4, 'Tiger']


# 2-6
def time_converter(number, unit):
    return number * {
        "hours": 1 / 60,
        "seconds": 60
    }[unit]


print(time_converter(120, "hours"))
# output:
# 2.0
print(time_converter(30, "seconds"))
# output:
# 1800

# Thanks for reading this far I guess. I am just being chatty because I am still
# trying to figure out what to write for my website.

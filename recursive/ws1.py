"""
Some non-tail-recursive functions.  Tail recursion isn't optimized in Python
anyways, so no point in feeling bad about not using an accumulator there!
"""
from typing import List, Union, Callable

Number = Union[int, float]


def sum_even(n: int) -> int:
    assert n >= 0
    if n == 0:
        return 0
    else:
        n = n // 2 * 2  # make even
        return n + sum_even(n - 2)


def sum_odd(n: int) -> int:
    assert n > 0
    if n == 1:
        return 1
    else:
        n = n // 2 * 2 + 1  # make odd
        return n + sum_odd(n - 2)


def prod(L: List[int]) -> int:
    if len(L) == 0:
        return 1
    else:
        return L[0] * prod(L[1:])


def sum_to(n: int) -> int:
    assert n >= 0
    if n == 0:
        return 0
    else:
        return n + sum_to(n - 1)


def sum_list(L: List[Number], n: int) -> Number:
    # assert n == len(L)
    if n == 0:
        return 0
    else:
        return L[0] + sum_list(L[1:], n - 1)


def most_element(
    f: Callable[[Number, Number], Number]
) -> Callable[[List[Number]], Number]:
    def most_element_impl(L: List[Number]) -> Number:
        assert len(L) > 0
        if len(L) == 1:
            return L[0]
        else:
            return f(L[0], most_element_impl(L[1:]))

    return most_element_impl


max_element = most_element(max)
min_element = most_element(min)


def is_palindrome(s: str) -> bool:
    if len(s) < 2:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])
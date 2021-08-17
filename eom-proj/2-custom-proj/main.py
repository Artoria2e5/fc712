#!/usr/bin/python3
# TODOMVC, Tkinker.

from sys import platform
import model
import shlex
import re
from typing import *
from tempfile import NamedTemporaryFile
import subprocess
import os
from itertools import islice
import sys

COMMANDS = {}
HELPS = {}
MODEL = model.TodoList(key="cli")


def bind(name: str, doc: str = None):
    def bind_decorator(func):
        nonlocal doc
        COMMANDS[name] = func
        if doc is None:
            doc = func.__doc__
        HELPS[name] = doc
        return func

    return bind_decorator


def edit_text(buf: str) -> str:
    """Edit a bunch of text in the editor."""
    f = NamedTemporaryFile(mode="w", encoding="utf-8", suffix=".txt", delete=False)
    f.write(buf)
    f.close()
    ret = -1
    print("Please remember to save.")
    print(f.name)
    if os.name == "nt":
        ret = subprocess.call(["notepad", f.name])
    elif sys.platform == "darwin":
        ret = subprocess.call(["nano", f.name])
    else:
        ret = subprocess.call(["nano", f.name])
    if ret != 0:
        raise OSError("editor exited with code {}".format(ret))
    f2 = open(f.name, "r", encoding="utf-8")
    result = f2.read()
    f2.close()
    os.unlink(f.name)
    return result


def uuid_from_arg0(arg: str) -> str:
    """Get a UUID from an argument."""
    if re.match(r"^[0-9]+$", arg):
        return MODEL.uuid_for_index(int(arg))
    else:
        return arg


@bind("show")
def cmd_show(args: List[str]):
    """Show a TODO identified by the UUID or index."""
    if len(args) != 1:
        raise ValueError("show takes exactly one argument.")
    uuid = uuid_from_arg0(args[0])
    print(MODEL.get_text(uuid))


@bind("add")
def cmd_add(args: List[str]):
    """Add a TODO."""
    if len(args) != 1:
        raise ValueError("add takes exactly one argument.")
    (n, _) = MODEL.add_todo(args[0])
    print(
        "New item is item #{n} now. Use `edit {n}` to edit, or `toggle {n}` to toggle.".format(
            n=n
        )
    )


@bind("edit")
def cmd_edit(args: List[str]):
    """Edit a TODO identified by the UUID or index."""
    if len(args) != 1:
        raise ValueError("edit takes exactly one argument.")
    uuid = uuid_from_arg0(args[0])
    text = edit_text(MODEL.get_text(uuid))
    MODEL.set_text(uuid, text)


@bind("list")
def cmd_list(args: List[str]):
    """List TODOs. Defaults to item #0-9; pass a number to show more."""
    start = 0
    if len(args) == 1:
        start = 10 * int(args[0])
    elif len(args) > 1:
        raise ValueError("list takes 0 or 1 arguments.")

    iter = MODEL.items.items()
    iter = islice(iter, start, start + 10)
    print(f"#\tdone?\ttitle\n")
    for (index, (_, entry)) in enumerate(iter, start):
        print(f"{index}\t{entry.completed}\t{entry.title}")


@bind("search")
def cmd_grep(args: List[str]):
    """Search for a string in all TODOs, using a regular expression."""
    if len(args) != 1:
        raise ValueError("search takes exactly one argument.")
    keyword = re.compile(args[0])
    # Linear search.
    iter = MODEL.items.items()
    for (index, (_, entry)) in enumerate(iter):
        if keyword.search(entry.title):
            print(f"{index}\t{entry.completed}\t{entry.title}")
        if keyword.search(entry.content):
            print(f"{index}\t{entry.completed}\t{entry.title} (body matches)")


@bind("toggle")
def cmd_toggle(args: List[str]):
    """Toggle an item."""
    if len(args) != 1:
        raise ValueError("edit takes exactly one argument.")
    uuid = uuid_from_arg0(args[0])
    print("Set to: {}".format(MODEL.toggle_todo(uuid)))


@bind("clear")
def cmd_clear(args: List[str]):
    """Clear completed todos."""
    if len(args) != 0:
        raise ValueError("clear takes no arguments.")
    MODEL.clear_completed()


@bind("help")
def cmd_help(args: List[str]):
    """Print help."""
    for name, help in HELPS.items():
        print("{}:\t{}".format(name, help))


@bind("quit")
def cmd_quit(args: List[str]):
    """Quit."""
    print("Goodbye.")
    exit()


def run(cmd: List[str]):
    """Command runner."""
    if len(cmd) == 0:
        return

    if cmd[0] in COMMANDS:
        COMMANDS[cmd[0]](cmd[1:])
    else:
        print("Unknown command: {}".format(cmd[0]))


def main():
    """Command processor loop."""
    print("Type 'help' to get help.")
    while True:
        try:
            run(shlex.split(input("> ")))
        except Exception as err:
            print(repr(err))


main()

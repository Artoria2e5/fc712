#!/usr/bin/python3
from typing import Callable, Dict, List
from uuid import uuid4
import csv
from itertools import islice
from pathlib import Path


def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)


class Item:
    def __init__(self, id: str, completed: bool, title: str, content: str):
        self.id = id
        self.completed = completed
        self.title = title
        self.content = content

    def get_text(self) -> str:
        return f"{self.title}\n\n{self.content}"

    def set_text(self, text: str) -> str:
        self.title, self.content = text.split("\n\n", 1)


ItemList = List[Item]
ItemDict = Dict[str, Item]


# IO backing.
def read_store(filename: str) -> ItemDict:
    l = dict()
    try:
        with open(filename, "r", newline="") as f:
            fr = csv.reader(f, dialect='unix')
            first = True
            for row in fr:
                if first:
                    first = False
                    continue
                l[row[0]] = Item(row[0], bool(int(row[1])), row[2], row[3])
    except FileNotFoundError:
        Path(filename).touch()
    return l


def write_store(filename: str, data: ItemDict) -> None:
    with open(filename, "w", newline="") as f:
        fw = csv.writer(f, dialect='unix')
        # schema row
        fw.writerow(["id", "completed", "title", "content"])
        # data
        for krow in data:
            row = data[krow]
            fw.writerow([row.id, int(row.completed), row.title, row.content])


class TodoList:
    def __init__(self, key: str = "default"):
        self.key = key
        # Use a dict here unlike our JS counterparts.
        # We get nicer indexing without ditching order.
        self.items: ItemDict = read_store(f"data/{key}.csv")
        self.actions: List[Callable] = []

    def subscribe(self, onChange: Callable):
        self.actions.append(onChange)

    def inform(self):
        """Supposed to call the view so it knows something's changed."""
        write_store(f"data/{self.key}.csv", self.items)
        for action in self.actions:
            action()

    def add_todo(self, title: str):
        uuid = str(uuid4())
        self.items[uuid] = Item(str(uuid4()), False, title, "")
        self.inform()
        return (len(self.items) - 1, uuid)

    def toggle_todo(self, id: str) -> bool:
        item = self.items[id]
        item.completed = not item.completed
        self.inform()
        return item.completed

    def toggle_all(self, state: bool):
        for _, item in self.items.items():
            item.completed = state
        self.inform()

    def set_content(self, id: str, title: str, content: str):
        item = self.items[id]
        item.title = title
        item.content = content
        self.inform()

    def clear_completed(self):
        for _, item in self.items.items():
            if item.completed:
                del self.items[item.id]
        self.inform()

    def uuid_for_index(self, idx: int):
        return nth(self.items.keys(), idx)

    def get_text(self, uuid: str) -> str:
        return self.items[uuid].get_text()

    def set_text(self, uuid: str, text: str):
        self.items[uuid].set_text(text)
        self.inform()

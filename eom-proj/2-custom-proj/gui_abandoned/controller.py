#!/usr/bin/python3
from . import model
from . import view

def main():
    model = model.TodoList()
    view = view.View(model)

    
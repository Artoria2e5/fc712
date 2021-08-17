#!/usr/bin/python3
from . import model
import PySimpleGUI as sg
from typing import Callable, Dict, List


def render_rows(rows: List[model.Item]):
    return [
        [
            sg.Checkbox(it.title, default=it.done, key=f"{it.id}_check"),
            sg.Button("edit...", key=f"{it.id}_edit"),
        ]
        for it in rows
    ]


def App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # TodoList
        self.todolist = Listbox(self, width=50, height=15, bg="red")
        # Render each Todo
        # ....... I don't get this thing!!!

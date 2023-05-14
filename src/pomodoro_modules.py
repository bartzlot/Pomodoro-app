import json
from notifypy import Notify
import abc
import PySimpleGUI as sg
import os
class ErrorsHandling(): 

    def handling_negatives(value: int, max_value: int):
        if value > max_value:
            return 0
        
        if value < 0:
            return max_value
        return value


    def handling_popups_empty_value(value: str, message: str):
        if not value:
            return True, sg.popup(message)
        if not value.isnumeric():
            return True, sg.popup("Please insert numeric value...")
        return False


    def handling_popups_empty_value_title(value: str, message: str):
        if not value:
            return True, sg.popup(message)
        return False


    def file_existence(path: str):
        if os.path.exists(path):
            return True
        sg.popup(f"File {path} doesn't exist, automatically creating one...")
        return False

  


def notify(t, m):
    n = Notify()
    n.title = t
    n.message = m
    n.send()


def saving_defaults_to_file(data: list, destination: str):
    object = json.dumps(data, indent=2)
    with open(destination, "w") as f:
        f.write(object)


def reading_defaults_from_file(destination: str):
    with open(destination, "r") as f:
        object = json.load(f)
    return object

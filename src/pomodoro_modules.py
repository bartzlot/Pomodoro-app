import time
import json
import os
from notifypy import Notify

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

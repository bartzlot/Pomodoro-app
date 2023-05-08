import time
def hours_validation(h: int):
    if h == -1:
        return 24
    if h == 25:
        return 0
    return h

def minutes_validation(m: int):
    if m == -1:
        return 60
    if m == 61:
        return 0
    return m

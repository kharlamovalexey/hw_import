import random

def calculate_salary():
    start = 100000
    stop = 300000
    step = 100
    return random.randrange(start, stop, step)

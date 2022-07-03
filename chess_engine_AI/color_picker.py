import numpy as np

def color():
    """ 50:50 chance of generating True or False. Used for selecting colors at start of match"""
    return

if __name__ == "__main__":
    n = 100
    res = len([1 for _ in range(100) if color()])
    print(f"{res} Heads, {100-res} Tails")

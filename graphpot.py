import matplotlib.pyplot as plt
import numpy as np


def main_p(a,b,c):
    if a == str:
        return "errorree"
    else:
        x = np.arange(0,a+2)
    if b == 2:
        y = x**2
    elif b == 3:
        y = x**3
    elif b == 4:
        y = x**4
    else:
        return 'Errortt'
    if c == 1:
        plt.plot(x,y)
    elif c == 2:
        plt.scatter(x,y)
    elif c == 3:
        plt.bar(x,y)
    else:
        return 'Error'
    plt.title("A Simple Graph of X against Y")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()
    return "Successfully plotted !"  







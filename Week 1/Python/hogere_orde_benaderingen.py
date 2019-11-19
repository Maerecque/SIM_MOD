import math
import numpy as np
import matplotlib.pyplot as plt


def func(x, y):
    return y


def heun(h, x0, y0, end):
    def asol(x):
        return math.exp(x)

    yasol = np.vectorize(asol)

    x = np.arange(0.0, end + h, h)
    y = np.zeros(x.size)
    y[0] = y0

    for i in range(1, x.size):
        y_intermediate = y[i - 1] + h * func(x[i - 1], y[i - 1])

        y[i] = y[i - 1] + (h / 2.0) * (func(x[i - 1], y[i - 1]) + func(x[i], y_intermediate))
    plt.plot(x, y, 'r-', label='Heun')
    plt.plot(x, yasol(x), 'b-', label='Actual')

    print("Actual solution at x = ", x[-1], " is ", "%.6f\n------" % yasol(x)[-1])
    print("Heun's Method solution at x = ", x[-1], " is ", "%.6f" % y[-1])


# Function for euler formula
def euler(x0, y, h, end):
    # Iterating till the point at which we
    # need approximation
    all_x = [x0]
    all_y = [y]
    while x0 < end:
        y = y + h * func(x0, y)
        x0 = x0 + h

        all_x.append(x0)
        all_y.append(y)

    plt.plot(all_x, all_y, 'y-', label='Euler')
    # Printing approximation
    print("Euler's Method solution at x = ", end, " is ", "%.6f" % y)

stepsize = 100
x0 = 0
y0 = 1
end = 1.0
h = end / stepsize

heun(h, x0, y0, end)
euler(x0, y0, h, end)
plt.legend()
plt.show()
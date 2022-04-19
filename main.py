import numpy as np


def deriv_side(f, x, h):
    return (f(x + h) - f(x)) / h


def deriv_center(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


def deriv (f, x, h, n):
    if n == 1:
        return deriv_center(f, x, h)
    return (deriv(f, x+h, h, n-1)-deriv(f, x-h, h, n-1))/(2*h)


if __name__ == '__main__':
    h = 10**-3

    print(deriv(lambda x: np.sin(x), 0, h, 1))
    print(deriv(lambda x: np.sin(x), 0, h, 2))
    print(deriv(lambda x: np.sin(x), 0, h, 3))
    print(deriv(lambda x: np.sin(x), 0, h, 4))


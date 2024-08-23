import numpy as np
import numdifftools as nd
from scipy.linalg import inv
EPSILON = 1e-6

# hi

def optimize(f, x_0):
    """
    Optimize the function f using Newton's method starting
    with x_0 as your initial guess.
    Returns a tuple contianing the optimum value and the x yielding that value.
    """
    x = x_0
    for _ in range(1000):
        x_new = x - np.dot(inv(nd.Hessian(f)(x)), nd.Gradient(f)(x))
        if np.linalg.norm(x_new - x) < EPSILON:
            return  {'x': x_new, 'f(x)': f(x_new)}
        x = x_new

    print("Didnt find minimum after 1000 runs")
    return {'x': x, 'f(x)': f(x)}

def f(x):
    return np.sum(np.array(x)**2) - 5

print(optimize(f,[8,8]))

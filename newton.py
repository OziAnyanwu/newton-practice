EPSILON = 1e-6


# Returns a function representing the nth derivative of f
def derivative(f, n):
    if n == 1:
        return lambda x: (f(x + EPSILON) - f(x)) / EPSILON
    return derivative(derivative(f, n - 1), 1)

def optimize(f, x_0):
    """
    Optimize the function f using Newton's method starting
    with x_0 as your initial guess.
    Returns a tuple contianing the optimum value and the x yielding that value.
    """
    x = x_0
    for _ in range(1000):
        x_new = x - derivative(f, 1)(x) / derivative(f, 2)(x)
        if abs(x_new - x) < EPSILON:
            return  {'x': x_new, 'f(x)': f(x_new)}
        x = x_new

    print("Didnt find minimum after 1000 runs")
    return {'x': x, 'f(x)': f(x)}

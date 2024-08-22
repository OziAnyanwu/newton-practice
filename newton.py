EPSILON = 0.001


# Returns a function representing the nth derivative of f
def derivative(f, n):
    if n == 1:
        return lambda x: (f(x + EPSILON) - f(x)) / EPSILON
    return derivative(derivative(f, n - 1), 1)


def optimize(f, x_0):
    x = x_0
    for _ in range(1000):
        x_new = x - derivative(f, 1)(x) / derivative(f, 2)(x)
        if abs(x_new - x) < EPSILON:
            return x_new, f(x)
        x = x_new
    print("Didnt find minimum after 1000 runs")
    return x, f(x)


def f(x):
    return x**2 - 5


x_opt, opt = optimize(f, 17.5)
print(f"Minimum: {opt} at x = {x_opt}")

EPSILON = 0.001

def derivative(f,n):
    if n == 1:
        return lambda x: (f(x+EPSILON) - f(x)) / EPSILON
    return derivative(derivative(f,n-1), 1)

def optimize(f, x):
    for _ in range(1000):
        x_new = x - derivative(f,1)(x) / derivative(f,2)(x)
        if x_new - x < EPSILON:
            return x_new
        x = x_new
    print('Didnt find minimum after 1000 runs')
    return x

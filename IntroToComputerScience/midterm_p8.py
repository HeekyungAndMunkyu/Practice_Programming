def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float

    returns the best guess when that guess is less than epsilon
    away from f(guess) or after 100 trials, whichever comes first.
    """
    guess = 1.0
    epsilon = float(epsilon)
    for i in range(100):
        if abs(f(guess) - guess) < epsilon:
            print f(guess) - guess, '<', epsilon
            return 'within 100 trials', guess
        else:
            guess = f(guess)
            print guess
    return 'after 100 trials', guess

def f(x):
    return x**2 - 2


epsilon = 0.01

print fixedPoint(f, epsilon)

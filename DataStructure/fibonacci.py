# recursive fibonacci

def fibonacci(n):
    '''
    n: int >= 0

    returns: 0 if n == 0
            1 if n == 1
            sum of previous two fibonacci numbers if n > 1
    '''
    # base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacciSeries(n):
    '''
    n: int >= 0

    returns: list, of fibonacciSeries
    '''
    fibSeries = []
    for i in range(n + 1):
        fibSeries.append(fibonacci(i))
    return fibSeries

n = int(raw_input('Enter an integer (>= 0):   '))
print fibonacciSeries(n)

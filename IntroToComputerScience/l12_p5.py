# L12 Problem 5

def genPrimes():
    primeList = []
    num = 2
    while True:
        isPrime = True

        for i in primeList:
            if (num % i) == 0:
                isPrime = False
        if isPrime:
            primeList.append(num)
            yield num
        num += 1

def genPrimesSample():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last

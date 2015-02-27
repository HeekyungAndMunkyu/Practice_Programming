# Intro to Statistics
# Problem Set 2: Probability



def nextHead(probs, flips):
    '''
    probs: list, of each coin's P(head)
    flips: string, of flips so far (ex. HHT, TTTH)

    returns: float, probability of next flip coming up heads
    '''
    print '-----numerator-----'
    numerator = 0

    for prob in probs:
        print 'num', prob
        numerator += (1.0 / len(probs)) * coinFlip(prob, flips) * prob
        print numerator


    print '-----denominator-----'
    denominator = 0

    for prob in probs:
        print 'denom', prob
        denominator += (1.0 / len(probs)) * coinFlip(prob, flips)
        print denominator
    print 'numerator', numerator
    print 'denominator', denominator

    return numerator / denominator

def coinFlip(prob, flips):
    '''
    prob: float, P(head)
    flips: string, of flips so far (ex. HHT, TTTH)

    returns: float, P(flips|coin #)
    '''
    result = 1
    for flip in flips:
        print 'coinFlip', flip, type(flip)
        if flip == 'H':
            result *= prob
        else:
            result *= (1 - prob)
    print 'coinFlip', prob, flips, 'result', result
    return result

probs = raw_input('probabilities: ')
probs = eval(probs)
flips = raw_input('flips so far: ')

print probs, type(probs)
print flips, type(flips)

print nextHead(probs, flips)

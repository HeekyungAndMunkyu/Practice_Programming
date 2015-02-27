from __future__ import division

def nextHead(probs, flips):
    '''
    probs: list, of each coin's P(head)
    flips: string, of flips so far (ex. HHT, TTTH)

    returns: float, probability of next flip coming up heads
    '''

    numerator = 0

    for prob in probs:

        numerator += (1.0 / len(probs)) * coinFlip(prob, flips) * prob


    denominator = 0

    for prob in probs:

        denominator += (1.0 / len(probs)) * coinFlip(prob, flips)


    return numerator / denominator

def coinFlip(prob, flips):
    '''
    prob: float, P(head)
    flips: string, of flips so far (ex. HHT, TTTH)

    returns: float, P(flips|coin #)
    '''
    result = 1
    for flip in flips:

        if flip == 'H':
            result *= prob
        else:
            result *= (1 - prob)

    return result



def maxdiff(l1,l2):
    return max([abs(x-y) for x,y in zip(l1,l2)])



testcases=[
(([0.5,0.4,0.3],'HHTH'), 0.43639398998330553),
(([0.14,0.32,0.42,0.81,0.21],'HHHTTTHHH'), 0.6297110187222278),
(([0.14,0.32,0.42,0.81,0.21],'TTTHHHHHH'), 0.6297110187222278),
(([0.12,0.45,0.23,0.99,0.35,0.36],'THHTHTTH'), 0.37479179323540324),
(([0.03,0.32,0.59,0.53,0.55,0.42,0.65],'HHTHTTHTHHT'), 0.536055356823069)]

for inputs, output in testcases:
    print inputs
#    print *inputs
    print output
for inputs,output in testcases:
    if abs(nextHead(*inputs) - output)<0.001:
        print 'Correct'
    else: print 'Incorrect'

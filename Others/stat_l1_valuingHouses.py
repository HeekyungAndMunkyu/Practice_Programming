# Stat101
# l1_2_Looking At Data
# Valuing Houses

s1, c1 = 1400, 112000.0
s2, c2 = 2400, 192000.0
s3, c3 = 1800, 144000.0
s4, c4 = 1900, 152000.0
s5, c5 = 1300, 104000.0
s6, c6 = 1100, 88000.0


avgCostPerSize = ( c1/s1 + c2/s2 + c3/s3 + c4/s4 + c5/s5 + c6/s6) /6
print avgCostPerSize

size = float(raw_input('What\'s the size of the housing?  '))

print 'The expected cost is', avgCostPerSize * size 

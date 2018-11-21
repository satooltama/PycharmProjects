from pracLibrary import _148calculator
# find statistic value from tuple
# 62.5,78,50,42,84,65.5,48,53.5,43
weight = input("Enter all of weight(,) :")
weight = tuple(map(float,weight.split(',')))

print('Maximum weight of {0} perons  = {1}'.format(len(weight),max(weight)))
print('Maximum weight of {0} perons  = {1}'.format(len(weight),min(weight)))

avg,aa,ba,ea = _148calculator(weight)

print('Maximum weight of {0} perons  = {1:.2f}'.format(len(weight),avg))
print('No. of weight above average  ={}'.format(aa))
print('No. of weight below average  ={}'.format(ba))
print('No. of weight equal to average  ={}'.format(ea))

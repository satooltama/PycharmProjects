# tuple of tuple

from operator import itemgetter

score = (('Adisak',12,34,50),('Sumon',10,34,41),('Wilai',40,21,45))

scoreSort = sorted(score,key=itemgetter(0),reverse=True)

print(scoreSort)
scoreSort = tuple(scoreSort)
print(scoreSort)

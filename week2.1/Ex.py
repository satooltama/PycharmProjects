# Tuple
# is immutable
# can't change value durning process

score = (10.5,50,20,30,43,12)
# เรียงข้อมูล แล้วจะกลายเป็น List
scoreSort = sorted(score)
scorereverse = sorted(score,reverse=True)

print("{0}".format(type(score)))

print("Number of tuple = {0}".format(len(score)))

print("max of tuple = {0}".format(max(score)))

print("min of tuple = {0}".format(min(score)))

print("sum of tuple = {0}".format(sum(score)))

print("sorted function = {}".format(scoreSort))

print("reverse sort function = {}".format(scorereverse))

print("index in tuple{}".format(score[0]))

for i in range(len(score)):
    print('test loop tuple {}'.format(score[i]))

# also can use anbai as loop (for each)
for i in score:
    print('test loop tuple {}'.format(i))

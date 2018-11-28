myList = []
print('TYPE = {}'.format(type(myList)))
myList += ['AAA','BBB','CCC']
print(myList)
myList.append('DDD')
print(myList)
print(myList[0])
myList[0] = 'EEE'
print(myList)
ok = 'ddd' in myList # True , False
if 'ddd' in myList:
    print(myList.index('ddd'))
print('*'*30)
for i in range(len(myList)):
    print(myList[i])
print(sorted(myList))
print(sorted(myList,reverse=True))
print("-"*20)



def miles_km(m):   # return Function
    return m*1.60934


for i in range(1 ,6):
    print ("{0:3} : {1:5.2f}".format(i,i*1.60934))



print("-"*20)

[print ("{0:3} : {1:5.2f}".format(i,i*1.60934)) for i in range(1 ,6)]


print("-"*20)

text = ['AAA','BBB','CCC']
newText = [x.lower() for x in text]

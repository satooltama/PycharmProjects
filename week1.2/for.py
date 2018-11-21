from pracLibrary import line
def sum1to1000():
    # set value of variable
    s = 0
    for i in range(1,1001,1):
        # sum+++
        s += i
    return s

print(sum1to1000())
line()

# for loop range(ตัวแรก,last,เพิ่มทีละเท่าไร)
for i in range(1,13,1):
    print('2 x {} = {}'.format(i,2*i))
line()
#####################################################################

car = ('Toyota','Honda','Suzuki','GM','GM')

# list ['Toyota','Honda','Suzuki','GM']
car1 = list(car)
print(car1)

car2 = set(car)
print(car2)
line()
for i in car:
    print('{0}'.format(i))
line()
for i in car2:
    print('{0}'.format(i))
line()
print(type(car))
line()

test1 = (10,20,30)
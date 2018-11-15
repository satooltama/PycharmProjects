birthyear = input('Enter Birth year (Christ) :')
print('variable type of year input = {}'.format(type(birthyear)))
# calculate
# convert str to int
age = 2018 - int(birthyear)
print('variable type of year after convert = {}'.format(type(int(birthyear))))
print(' Your age = {}'.format(age))

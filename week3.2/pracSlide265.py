# homework

import os.path
from pracLibrary import setConfig

def readFile(filename):
    with open (filename,'r',encoding='UTF-8') as f :
        data = f.readlines()
        return data


if __name__ == '__main__':
    filename = 'myFile/products.csv'
    fileconfig = 'myFile/appConfig.ini'
    if os.path.exists(filename):
        count = readFile(filename)
        decimal, comma, line, unit = setConfig(readFile(fileconfig))
    else:
        print('"{}" is missing'.format(filename))

    totalvalue = 0
    for i in range(len(count)):
        name, price, stock = count[i].split(',')
        value = float(price) * int(stock)
        print('{0:15}{1:15{2}.{3}f}'.format(name, value, comma, decimal))
        totalvalue += value
    print('{}'.format(line) * 30)
    print('Total Value{0:15{1}.{2}f} {3}'.format(totalvalue, comma, decimal, unit))
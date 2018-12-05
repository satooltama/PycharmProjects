# homework (Download : goo.gl/gd2Q8c)
import os.path

def readFile(filename):
    with open (filename,'r',encoding='UTF-8') as f :
        count = f.readlines()
        for i in range(len(count)):
            print('{0}. - {1}'.format(i+1,count[i].upper()),end='')

if __name__ == '__main__':

    filename = 'myFile/ilovesea.txt'
    if os.path.exists(filename):
        readFile(filename)
    else:
        print('"{}" is missing'.format(filename))
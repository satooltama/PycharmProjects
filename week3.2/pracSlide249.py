import os.path

def readFile(filename,m): #.readlines()
    with open (filename,m,encoding='UTF-8') as f :
        count = f.readlines()
        sortData = sorted(count,reverse=True)
        for i in range(len(sortData)):
            print('{0}.) {1}'.format(i+1,sortData[i].upper()),end='')

if __name__ == '__main__':
    filename = 'myFile/MarvelComics.txt'
    mode = 'r'
    if os.path.exists(filename):
        readFile(filename,mode)
    else:
        print('"{}" is missing'.format(filename))

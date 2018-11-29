def readFile(filename):
    with open(filename,"r",encoding="UTF-8") as f:
        data = f.readline()
        print(data,end="")
        data = f.readline()
        print(data)
        for i in f:
            data = f.readline()
            print(data)

def readFile3(filename):#.readlines()
    with open(filename,"r",encoding="UTF-8") as f:
        data = f.readline()
        print(data,end="")
        data = f.readline()
        print(data)
        for i in f:
            data = f.readline()
            print(data)



if __name__ == '__main__':
    filename = "myFile/MarvelComics.txt"
    readFile(filename)

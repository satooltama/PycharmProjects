#slide 226

import os.path

def workingWithFile(filename,m):
    f = open(filename,mode=m)
    f.write("Chatkawin\nTaola\n")
    f.close()

def workingWithFile2(filename,m):

    with open(filename,mode=m) as f:
        f.write("Chatkawin\nTaola\n")

if __name__ == '__main__':
    filename = "myFile/students.txt"
    mode = "x"
    workingWithFile(filename,mode)


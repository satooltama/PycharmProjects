# เขียนรันและสร้างไฟล ให้เขียนข้อมูลตามรูปแปป ใช้แบบสไลด์ 240
import os.path
'''
def workingWithFile(filename,m):
    f = open(filename,mode=m)
    f.write("Chatkawin\nTaola\n")
    f.close()
'''
def workingWithFile2(filename,m,n,value):

    with open(filename,mode=m,encoding='UTF-8') as f:
        for i in range(int(n)):
            f.write('{0} {1} {2}\n'.format(value[i][0],value[i][1],value[i][2]))

if __name__ == '__main__':

    product = []

    n = input('Enter number of new product: ')
    for i in range(int(n)):
        pName = input('Enter Product name: ')
        pPrice = input('Enter Product Price: ')
        pStock = input('Enter Product Stock: ')
        product.append([pName,pPrice,pStock])

    filename = "myFile/students1.txt"
    if os.path.exists(filename):
        mode = 'a'
    else:
        mode = 'x'
    workingWithFile2(filename,mode,n,product)


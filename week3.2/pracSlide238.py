# เขียนรันและสร้างไฟล ให้เขียนข้อมูลตามรูปแปป ใช้แบบสไลด์ 240
'''
def workingWithFile(filename,m):
    f = open(filename,mode=m)
    f.write("Chatkawin\nTaola\n")
    f.close()
'''
def workingWithFile2(filename,m,n,value):

    with open(filename,mode=m) as f:
        for i in range(int(n)):
            f.write(str(value[i]))

if __name__ == '__main__':

    product = []

    n = input('Enter number of new product: ')
    for i in range(int(n)):
        pName = input('Enter Product name: ')
        pPrice = input('Enter Product Price: ')
        pStock = input('Enter Product Stock: ')
        product.append([pName,pPrice,pStock])
    print(product)

    filename = "myFile/students1.txt"
    mode = "x"
    workingWithFile2(filename,mode,n,product)


from pracLibrary import split

print("Senior : 65 up\nAdult : 18-64 \nJunior : 4-17\nChild : 0-3")

se,ad,ju,ch = input("Enter number of Senior,Adult,Junior,Child :").split(",")

split(se,ad,ju,ch)

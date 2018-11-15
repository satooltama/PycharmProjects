priceofproduct = input('Enter type of product :')
amout = input('Enter amout of product :')
line = ('-'*30)

# function
def line1():
    print('-'*30)
# another function
def line2(ch):
    print("{}".format(ch)*30)
#another function
def line3(ch,num):
    print("{}".format(ch)*num)

subtotal = float(priceofproduct) * int(amout)
vat = 7 * subtotal / 100
grandtotal = vat+subtotal

print(line)
print('Price        :   {0:10,.2f} Bath'.format(float(priceofproduct)))
print('Amout        :   {0:10} Bath'.format(int(amout)))
print('Subtotal     :   {0:10,.2f} Bath'.format(float(subtotal)))
line1()
print('VAT(7%)      :   {0:10,.2f} Bath'.format(float(vat)))
print('Grand total  :   {0:10,.2f} Bath'.format(float(grandtotal)))
line2('x')
line3('*',20)

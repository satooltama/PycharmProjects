# import function from another file

# from type like m.bmitype
import mylibrary as m

# for just import function
from mylibrary import bmitype,showCerrentThaiYear

if __name__ == '__main__':
    weight = float(input("Enter Weight : "))
    Height = float(input("Enter Height : "))
    bmi = m.calMBI(weight,Height)
    m.line1()
    print("BMI is {0:,.2f}".format(bmi))
    print("You are {0}".format(bmitype(bmi)))
    m.line1()
    print('Cerrent Thai year = {}'.format(showCerrentThaiYear()))


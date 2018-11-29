
import tesLib as m

# for just import function
from testLib import bmitype,showCerrentThaiYear

if __name__ == '__main__':
    emp = {"Name":"Somsak","Age":25,
       "Height":170,"Address":"Bangkok",
       "Weight":61}

    bmi = m.calMBI(emp["Weight"],emp["Height"])
    emp["BMI"] = bmi
    m.line1()
    print("BMI is {0:,.2f}".format(emp["BMI"]))
    print("You are {0}".format(bmitype(emp["BMI"])))
    m.line1()


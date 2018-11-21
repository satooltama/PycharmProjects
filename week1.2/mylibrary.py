import math as M
# math.pow(x,y)

import datetime as dt
# date time

import os

def showCerrentThaiYear():
    TY = dt.datetime.now().year + 543
    return TY

def calMBI(w,h):
   #bmi = w/((h/100)**2)
   # use math for calculate
   bmi = w/M.pow(h/100,2)

   return bmi

def bmitype(bmi):
   if(bmi<=18.50):
       return 'underweight'
   elif(bmi<=22.99):
       return 'normalweight'
   elif(bmi<=30):
       return 'overweight'
   elif(bmi>30):
       return 'obecity'

def line1():
   print("-"*40)

# for prevent this message to show on another file
if __name__ == '__main__':
    print('Thai is message from mylibrary')

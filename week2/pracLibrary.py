import math as m

def line():
    print('*'*40)

def circleArea(r):
    a = m.pow(r,2) * m.pi
    return a

def regtangleArea(w,l):
    a = w * l
    return a

def checkChoice(c):
    if c.upper() == "C":
        r = input('Please input Radius : ')
        line()
        return print('AREA = {0:.2f}'.format(circleArea(float(r))))
    elif c.upper() == "S":
        w = input('Please Input Width :')
        l = input('Please Input Length:')
        line()
        return print('AREA = {0:.2f}'.format(regtangleArea(float(w),float(l))))

def scoresum(m,f,h):
    m = int(m)*0.3
    f = int(f)*0.5
    h = int(h)*0.2

    sum = m+f+h

    return sum

def gradeScale(sum):
    if sum > 97:
        return 'A+'
    elif sum > 93:
        return 'A'
    elif sum > 90:
        return 'A-'
    elif sum > 87:
        return 'B+'
    elif sum > 83:
        return 'B'
    elif sum > 80:
        return 'B-'
    elif sum > 77:
        return 'C+'
    elif sum > 73:
        return 'C'
    elif sum > 70:
        return 'C-'
    elif sum > 67:
        return 'D+'
    elif sum > 63:
        return 'D'
    elif sum > 60:
        return 'D-'
    elif sum < 59:
        return 'F'
    return

def scoreloop(n):

    smin = 0
    smax = 0
    ssum = 0
    avg  = 0

    for i in range(n):

        ss = input('Enter score of student number {} :'.format(i+1))
        ss = float(ss)
        ssum += ss

        if i == 0:
            smin = ss
            smax = ss
        elif ss > smax:
            smax = ss
        elif ss < smin:
            smin = ss

    avg = float(ssum) / n

    line()

    return print('AVEARG SCORE = {0:.2f} \nMAX SCORE = {1:.2f} \nMIN SCORE = {2:.2f}'.format(avg,smax,smin))

def YearCal(p,d,y):

    for i in range(y):
        dp = d * p / 100
        recentprice = p - dp
        print('After use {0} Year : Reduce = {1:,.2f} BATH    Price = {2:,.2f}'.format(i+1,dp,recentprice))
        p = recentprice
    return

def zetacal(i,j,N):

    sum = 0

    for i in range(i,j+1,1):
        print('({0}-10)^{1}*{0}'.format(i,N))
        sum += m.pow(i-10,N)*i
    line()
    return print('Answer is {0}'.format(sum))


def _92main():
    line()
    print('                 MENU                  ')
    line()
    print('C or c Area of circle')
    print('S or s Area of Regtangle')
    line()
    choice = input('Enter your Choice :')
    line()
    checkChoice(choice)
    line()

def _94main():
    print('Input Score')
    m = input('1.Midterm    :')
    f = input('2.Final      :')
    h = input('3.Homework   :')
    print('Your Grade = {}'.format(gradeScale(scoresum(m,f,h))))

def _109main():

    snum = input('How many student in your class :')
    line()
    scoreloop(int(snum))
    line()

def _111main():
    pricecar = input('Input Price of car :')
    dperyear = input('Input depreciation per year (%) :')
    yearcount = input('Input how many year you want to see :')
    pricecar = float(pricecar)
    dperyear = int(dperyear)
    yearcount = int(yearcount)
    line()
    print('Price of Car = {0:,.2f}'.format(pricecar))
    line()
    YearCal(pricecar,dperyear,yearcount)
    line()

def _113main():
    i = input('Input i :')
    j = input('Input j :')
    N = input('Input N :')
    i = int(i)
    j = int(j)
    N = int(N)
    line()
    zetacal(i,j,N)
    line()
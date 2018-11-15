import math as m

def menu():
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
    sum = int(m)+int(f)+int(h)
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

def score():
    print('Input Score')
    m = input('1.Midterm    :')
    f = input('2.Final      :')
    h = input('3.Homework   :')
    print('Your Grade = {}'.format(gradeScale(scoresum(m,f,h))))

def scoreloop(n):
    smax = 0
    smin = 0
    sbase = 0

    for i in range(1,n+1,1):
        score =  input('Enter score of student number {} :'.format(i))
        score = float(score)

        if score > smax:
            smax = score
        elif score < smin:
            smin = score



def _109main():
    snum = input('How many student in your class :')
    line()
    scoreloop(int(snum))

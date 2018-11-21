import math as m

def split(se,ad,ju,ch):
    se = float(se)
    ad = float(ad)
    ju = float(ju)
    ch = float(ch)
    print("Total of ticket = ${0:,.2f}".format(ticketcal(se,ad,ju,ch)))

def ticketcal(se,ad,ju,ch):
    adp = 22.95
    sep = 19.95
    jup = 14.95
    chp = 0

    se = se*sep
    ad = ad*adp
    ju = ju*jup
    ch = ch*chp

    sum = se+ad+ju+ch

    return sum


def namesplit(name):

    fname,lname = name.split()

    lname = lname[0:2]

    return "{}.{}@tni.ac.th".format(lname,fname)

def discal(x1,y1,x2,y2):

    return m.sqrt(m.pow(x2-x1,2) + m.pow(y2-y1,2))

def _148calculator(weight):
    avg = sum(weight)/len(weight)
    aa = 0
    ba = 0
    ea = 0
    for i in weight:
        if i > avg:
            aa += 1
        elif i < avg:
            ba += 1
        elif i == avg:
            ea += 1
    return avg,aa,ba,ea

def checkNumber(*amout,see):
    if see == "max-min":
        x = max(amout)
        y = min(amout)
    elif see == "ab-bl-av":
        avg = sum(amout)/len(amout)
        x,y = 0,0
        for i in amout:
            if i > avg:
                x += 1
            elif i < avg:
                y += 1
    return x,y


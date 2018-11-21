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

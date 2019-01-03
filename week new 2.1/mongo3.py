import pymongo


def findMobile():
    conn = pymongo.MongoClient("localhost",27017)
    db = conn.get_database("studyMobileShop")
    #cursor = db.Products.find({'pbrand':'Samsung'}).sort([('pprice',pymongo.DESCENDING),('pname',pymongo.ASCENDING)])

    cursor = db.Products.find({'pbrand':'Samsung'}).sort([('pprice',pymongo.DESCENDING),('pbrand',pymongo.ASCENDING)])

    print('Found {0}'.format(cursor.count()))
    print('*'*30)
    for e in cursor:
        print("{0:25} {1:10}".format(e['pname'],e['pprice']))

def findMobile2(B,S):
    conn = pymongo.MongoClient("localhost",27017)
    db = conn.get_database("studyMobileShop")
    #cursor = db.Products.find({'pbrand':'Samsung'}).sort([('pprice',pymongo.DESCENDING),('pname',pymongo.ASCENDING)])

    cursor = db.Products.find({'$and':[{'pbrand':B},{'psize':{'$gt':S}}]}).sort([('pprice',pymongo.DESCENDING),('pbrand',pymongo.ASCENDING)])

    print('Found {0}'.format(cursor.count()))
    print('*'*30)
    for e in cursor:
        print("{0:25} {1:10}".format(e['pname'],e['pprice']))

def removeMobile1():
    conn = pymongo.MongoClient("localhost",27017)
    db = conn.get_database("studyMobileShop")
    db.Products.remove({'pbrand':{'$regex':'^oppo$','$options':'i'}})

def removeMobile2():
    conn = pymongo.MongoClient("localhost",27017)
    db = conn.get_database("studyMobileShop")
    db.Products.remove({'$and':[{'pbrand':{'$regex':'^samsung$','$options':'i'}},{'pprice':{'$gt':150000}}]})

def updateData():
    conn = pymongo.MongoClient("localhost",27017)
    db = conn.get_database("studyMobileShop")


if __name__ == '__main__':
    #findMobile()
    #findMobile2('Samsung',6)
    #removeMobile1()
    #removeMobile2()

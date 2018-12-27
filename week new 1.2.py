import pymongo


def insertNewMobile1():
    conn = pymongo.MongoClient("localhost", 27017)
    db = conn.get_database("MobileShop")
    db.Products.insert({"pid": "p0007", "pname": "iPhone XRRL", "pprice": 340000.0})
    print(1)


def insertNewMobile2():
    conn = pymongo.MongoClient("localhost", 27017)
    db = conn.get_database("MobileShop")
    db.Products.insert([{"pid": "p0010", "pname": "iPhone XRIRS", "pprice": 550000.0},
                        {"pid": "p0011", "pname": "iPhone XPSORFKX", "pprice": 53340000.0}])
    print(2)


def insertNewMobile3():
    conn = pymongo.MongoClient("localhost", 27017)
    db = conn.get_database("MobileShop")
    res = db.Products.insert_one({"pid": "p0012", "pname": "iPhone XRIRSSS", "pprice": 4521000.0})
    print('Inserted {0}'.format(res.inserted_ids))


def insertNewMobile4():
    conn = pymongo.MongoClient("localhost", 27017)
    db = conn.get_database("MobileShop")
    res = db.Products.insert_many([{"pid": "p0013", "pname": "iPhone XRssIRS", "pprice": 55400.0},
                                   {"pid": "p0014", "pname": "iPhone XPSORERWRFKX", "pprice": 3433000.0}])
    print('Inserted {0}'.format(res.inserted_ids))


def insertByMe():
    conn = pymongo.MongoClient("localhost",27017)
    db = conn.get_database("MobileShop")
    ans = 'y'
    allinfo = []
    while ans.lower()=='y':
        id = input("Enter Products ID :")
        name = input('Enter Products Name :')
        price = input('Enter Product Price :')
        color = input('Enter Product Color :')
        allinfo.append({"pid":id,"pname":name,"pprice":price,"pcolor":color})
        ans = input('Do you want to continue(Y|N)?')
    res = db.Products.insert_many(allinfo)
    print('Inserted {0}'.format(res.inserted_ids))


if __name__ == '__main__':
    #insertNewMobile1()
    #insertNewMobile2()
    #insertNewMobile3()
    #insertNewMobile4()
    insertByMe()

import pymongo

def conDB():
    try:
        conn = pymongo.MongoClient("localhost", 27017)
        db = conn.get_database("companyDB")
    except Exception as ex:
        print(ex)
    return db

def findEmp():
    try:
        conn = pymongo.MongoClient("localhost", 27017)
        db = conn.get_database("companyDB")
        cursor = db.employee_salary.find()
        return cursor

    except Exception as ex:
        print(ex)

def insertCol():
    try:
        conn = pymongo.MongoClient("localhost", 27017)
        db = conn.get_database("companyDB")
        db.create_collection('employee_salary')
        cursor = db.employee_salary.insert_many([{"_id":1,
                                                  "emp_id":10001,
                                               "firstName":"Chatkawin",
                                               "lastName":"Taola",
                                               "emp_salary":20000},
                                              {"_id":2,
                                               "emp_id": 10002,
                                               "firstName": "Akira",
                                               "lastName": "Takahashi",
                                               "emp_salary": 18000},
                                              {"_id":3,
                                               "emp_id": 10003,
                                               "firstName": "Sean",
                                               "lastName": "Roger",
                                               "emp_salary": 19000},
                                              {"_id":4,
                                               "emp_id": 10004,
                                               "firstName": "Emmy",
                                               "lastName": "Stella",
                                               "emp_salary": 21000},
                                              {"_id":5,
                                               "emp_id": 10005,
                                               "firstName": "Robin",
                                               "lastName": "Singh",
                                               "emp_salary": 20000},
                                              {"_id":6,
                                               "emp_id": 10006,
                                               "firstName": "Erika",
                                               "lastName": "Krisanti",
                                               "emp_salary": 18000},
                                              {"_id":7,
                                               "emp_id": 10007,
                                               "firstName": "Nuttaput",
                                               "lastName": "Kowadisigunbun",
                                               "emp_salary": 20000},
                                              {"_id":8,
                                               "emp_id": 10008,
                                               "firstName": "Shinpat",
                                               "lastName": "Pronpunrath",
                                               "emp_salary": 19000},
                                              {"_id":9,
                                               "emp_id": 10009,
                                               "firstName": "Make",
                                               "lastName": "Tawatchai",
                                               "emp_salary": 20000},
                                              {"_id":10,
                                               "emp_id": 10010,
                                               "firstName": "Arthur",
                                               "lastName": "Falcon",
                                               "emp_salary": 18000},
                                              {"_id":11,
                                               "emp_id": 10011,
                                               "firstName": "Zento",
                                               "lastName": "Saint",
                                               "emp_salary": 21000},
                                              {"_id":12,
                                               "emp_id": 10012,
                                               "firstName": "Schaniya",
                                               "lastName": "Ngmps",
                                               "emp_salary": 20000},
                                              {"_id":13,
                                               "emp_id": 10013,
                                               "firstName": "Lucksika",
                                               "lastName": "Khemaluk",
                                               "emp_salary": 19000},
                                              {"_id":14,
                                               "emp_id": 10014,
                                               "firstName": "Law",
                                               "lastName": "Rimthong",
                                               "emp_salary": 18000},
                                              {"_id":15,
                                               "emp_id": 10015,
                                               "firstName": "Nongnapat",
                                               "lastName": "Jiratthaphon",
                                               "emp_salary": 19000},
                                              {"_id":16,
                                               "emp_id": 10016,
                                               "firstName": "Akarawat",
                                               "lastName": "Wangsawat",
                                               "emp_salary": 19000},
                                              {"_id":17,
                                               "emp_id": 10017,
                                               "firstName": "Arm",
                                               "lastName": "Takakorn",
                                               "emp_salary": 18000},
                                              {"_id":18,
                                               "emp_id": 10018,
                                               "firstName": "Neng",
                                               "lastName": "Gasamsak",
                                               "emp_salary": 18000},
                                              {"_id":19,
                                               "emp_id": 10019,
                                               "firstName": "Wafer",
                                               "lastName": "Foxs",
                                               "emp_salary": 18000},
                                              {"_id":20,
                                               "emp_id": 10020,
                                               "firstName": "Jeen",
                                               "lastName": "Nithi",
                                               "emp_salary": 18000},
                                              {"_id":21,
                                               "emp_id": 10021,
                                               "firstName": "Boat",
                                               "lastName": "Chaisun",
                                               "emp_salary": 18000},
                                              {"_id":22,
                                               "emp_id": 10022,
                                               "firstName": "Moltol",
                                               "lastName": "Krasaesom",
                                               "emp_salary": 19000},
                                              {"_id":23,
                                               "emp_id": 10023,
                                               "firstName": "Jaruwattana",
                                               "lastName": "Bunpim",
                                               "emp_salary": 18000},
                                              {"_id":24,
                                               "emp_id": 10024,
                                               "firstName": "Thanapol",
                                               "lastName": "Saranatrai",
                                               "emp_salary": 19000}
                                              ])
        return cursor

    except Exception as ex:
        print(ex)

def dropCol():

    try:
        conn = pymongo.MongoClient("localhost", 27017)
        db = conn.get_database("companyDB")
        cursor = db.employee_salary.drop()
        return cursor

    except Exception as ex:
        print(ex)




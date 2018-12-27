import sqlite3
import csv
import os

def generateData(db):
    try:
        with (sqlite3.connect(db)) as conn:
            sql_command = """
            CREATE TABLE `Catagories` (
	        `id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	        `name`	TEXT NOT NULL);
            
            CREATE TABLE `Products` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL,
	`price`	REAL CHECK(price > 0),
	`stock`	INTEGER DEFAULT 10,
	`categoryID`	INTEGER,
	FOREIGN KEY(`categoryID`) REFERENCES `Catagories`(`id`)
);
            """
            conn.executescript(sql_command)
    except Exception as e :
        print('Error {0}'.format(e))

def insertDummyData(db):
    try:
        with (sqlite3.connect(db)) as conn:
            sql_dummy = """
            insert into Catagories (name) values ('Condiments');
            insert into Catagories (name) values ('Dairy Product');
            insert into Catagories (name) values ('Meat');
            insert into Catagories (name) values ('Seafood');
            insert into Catagories (name) values ('Grains');
            
            insert into Product (name,price,stock,categoryID) values ('Chai',30.0,100,1);
            insert into Product (name,price,stock,categoryID) values ('Geitost',200.0,25,2);
            insert into Product (name,price,stock,categoryID) values ('Gula Malacca',300.5,10,1);
            insert into Product (name,price,stock,categoryID) values ('Mishi Kobe Niku',120.0,5,3);
            insert into Product (name,price,stock,categoryID) values ('Inlagd Sill',2500.0,2,4);
            insert into Product (name,price,stock,categoryID) values ('Filo Mix',12.0,23,5);
            insert into Product (name,price,stock,categoryID) values ('Pert Pasties',40.0,3,3);
            insert into Product (name,price,stock,categoryID) values ('Gravad lax',23.0,0,4);
            insert into Product (name,price,stock,categoryID) values ('Tofu',250.75,10,2);
            """
            conn.executescript(sql_dummy)
    except Exception as e:
        print('Error{0}'.format(e))

def updateProductPrice(db,id,incresepercent):
    try:
        with (sqlite3.connect(db)) as conn:
            sql_update = "update Products set price ="+incresepercent+"where id ="+id+";"
            conn.executescript(sql_update)
    except Exception as e:
        print('Error{0}'.format(e))

def deleteProductID(db,id):

    try:
        with (sqlite3.connect(db)) as conn:
            sql_delete = "delete from Products where id="+str(id)+";"
            conn.executescript(sql_delete)
    except Exception as e:
        print('Error{0}'.format(e))

def file(value):
    if os.path.exists("Database\ExportZeroStock.csv"):
        with open("Database\ExportZeroStock.csv",mode="w") as f:
            Writer=csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL);
            for i in range(len(value)):
                Writer.writerow(list(value[i]))

    else:
        with open("Database\ExportZeroStock.csv",mode="x") as f:
            Writer=csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL);
            for i in range(len(value)):
                Writer.writerow(list(value[i]))


def exportZeroStock(db):
    sqlcommand="select * from product"
    subdata=[]
    ZeroStock=[]
    try:
        with (sqlite3.connect(db)) as conn:
             cursor = conn.execute(sqlcommand)
             for i in cursor:
                 subdata.append(i)
             for i in range(len(subdata)):
                 if (subdata[i][3]==0):
                     ZeroStock.append(subdata[i])
             file(ZeroStock)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    dbapp = "mydatabase/mydatabase.sqlite3"

    #generateData(dbapp)
    #insertDummyData(dbapp)
    #updateProductPrice(dbapp,id,percent)
    #deleteProductID(dbapp,id)
    #exportZeroStock(dbapp)

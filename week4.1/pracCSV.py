import csv

def write_csv():
   with open("products-csv.csv",'w',newline='', encoding="UTF-8") as f:
       fw = csv.writer(f,delimiter=",")
       # Implement by List
       fw.writerow(["Product","Price" , "Stock"])
       fw.writerow(["Coffee",50 , 80])
       fw.writerow(["Radio", 1200, 10])
       fw.writerows([["TV 16 นิ้ว", 234.5, 100],["Car", 30000, 2]])
if __name__ == '__main__':
   write_csv()

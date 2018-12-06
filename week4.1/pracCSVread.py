import csv

def read_csv():
    with open('products-csv.csv','r',encoding='utf8') as f:
        fr = csv.reader(f)
        for row in fr:
            print('{0}'.format(row))

if __name__ == '__main__':

    read_csv()

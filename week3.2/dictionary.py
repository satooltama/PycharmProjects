# dictionary

emp = {}

emp = {"Name":"Somsak","Age":25,
       "Height":170,"Address":"Bangkok"}

# ไม่ใช้เป็น index **emp[0]**
print(emp["Name"])
# add value
emp["Gender"] = 'M'

print(emp)
# chack only key
print(emp.keys())

if "name" is emp.keys():
    print(emp["name"])
# เพิ่ม
emp["name"] = "samsung"
print(emp)
del emp["name"]
print(emp)

for i in emp.keys():
    print(i)
for i in emp.values():
    print(i)







# Dictionary: (Key-Value): Mỗi phần tử gồm một Key và một Value.
person ={"name":"Loi","age":20,"City":"Ha Noi"}
a =dict(name="a",age=25,city="TPHCM")
print(type(person))
print(person)
print(a["name"])
# cập nhật 
person["nam sinh"]=2006
print(person)
a.update({"name": "long"})
print(a)
# xóa 
a.pop("name") 
print(a)
print(a.popitem())  # xóa key và trả về giá trị của nó 
del person["age"]
print(person)

for x in person:
    print(x)

# duyệt các values
for i in person.values():
    print(i)
# duyệt các từ khó 
for b in person.keys():
    print(b)
# duyệt các cặp khóa và giá trị 
for x,y in person.items():
    print(f"{x}:{y}")

# sắp xếp theo key 
data = {
    "c": 3,
    "a": 1,
    "b": 2
}
datamoi=dict(sorted(data.items()))
print(datamoi)
# sắp xếp theo value
dataa= {
    "An": 8,
    "Lợi": 10,
    "Nam": 6
}

data_moii = dict(sorted(dataa.items(), key=lambda x: x[1]))

print(data_moii)
print(dataa[1])
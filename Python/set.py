monhoc ={"Toan","Ly","hoa"}
print(monhoc)
for x in monhoc:
    print(x)
numbers =set([1,2,3,4,5,6])
print(type(numbers))
name =set("loi")
print(type(name) )
print(name)
# thêm phần tử 
monhoc.add('lich su')
print(monhoc)
hocthem={"anh van","dia","ngu van"}
monhoc.update(hocthem)
print(monhoc)
# xóa phần tử 
hocthem.remove("ngu van")
print(hocthem)
hocthem.discard("tin hoc")
print(hocthem)
numbers.pop()
print(numbers)
# Xóa hết 
numbers.clear()
print(numbers.clear())
# xóa biến lun
del monhoc
print(monhoc)
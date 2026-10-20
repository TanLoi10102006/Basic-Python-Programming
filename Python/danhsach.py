ds =["loi",2006,True ]
print(ds)
print(ds[2])
print(ds[:])
print(ds[0:2]) # [x:y)

ds[0]="A"
print(ds)
ds.append("nguyen van a") # thêm vào cuối danh sách
print(ds)
ds.insert(2,"huhu") # chèn vào vị trí 
print(ds)
Ls =["a","b","c","d","a","b","a"]
print("dem so a la ",Ls.count("a"))

# xóa phần tử 
Ls.remove("b")
print(Ls)
# xóa theo index 
Ls.pop(3)
print(Ls)
# kiểm tra phân thử có tồn tại k 
if "a" in Ls:
    Ls.remove("a")
    print("da xoa a ", Ls)
else:
    print("k co a ")

# đảo ngược vị trí 
haha=[1,2,3,4,5,6,7,8]
haha.reverse()
print(haha)

# sap xep 
huhu=[5,2,4,7,9,8]
huhu.sort()
print(huhu)
# sắp xếp đảo ngược 
huhu.sort(reverse=True)
print(huhu)


text = """Đây là dòng 1
Đây là dòng 2
Đây là dòng 3"""
print(text)
# chuỗi nhân 
chuoi="aaa\n"
print(chuoi*10)

chuoi1 ="xin chao tan loi "
chuoi2="tan loi "
if chuoi2 in chuoi1:
    print("chuoi 2 la con chuoi 1")
else:
    print(" chuoi 2 k la con chuoi 1")

# viet hoa va thuong
chuoi3="meta"
print(chuoi3.lower())
print(chuoi3.upper())
# viet hoa chu dau 
chuoi4="python"
print(chuoi4.capitalize())

# Tìm và Đếm số lượng chuỗi con 
s ="Lap tring python la xu huong hien nay "
print(s.find("python"))
print(s.find("pythonx"))
# thay the 
ss="Lap tring python la xu huong hien nay "
ss=ss.replace("python","PYTHON")
print(ss)

# cắt thành 1 list 
list=ss.split(" ")
print(list)




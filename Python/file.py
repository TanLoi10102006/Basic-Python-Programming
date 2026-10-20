# tạo file
try:
    with open("vidu1.txt", "x") as f:  # "x" tạo file mới, lỗi nếu file đã tồn tại
        pass
except FileExistsError:
    pass
except Exception as e:
    print(e)

# ghi du lieu 
# w ghi du lieu 
# a nối vào file 
try:
    with open("vidu1.txt", "a") as f:
        f.write("xin chao cac ban\n")
        f.close()
except Exception as p:
    print(p)

try:
    with open("vidu1.txt","r") as a:
        data=  a.read()
        print(data)
        a.close()
except Exception as x:
    print(x)

print("====================") 
try:
    with open("vidu1.txt", "r") as b:
        c = b.readlines()
        i =1
        for e in c:
            print(str(i)+" "+e)
            i+=1
except Exception as l:
    print(l)

# encoding =utf8 
try: 
    with open("vidu2.txt","x", encoding='utf-8'):
        pass
except Exception as K:
    print(K)


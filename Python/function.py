def xinChao():
    print("hello")
xinChao()
def tong(a,b):
    return a+b
Ketqua=tong(3,4)
print(Ketqua)

# khi xác định được số đối số, chúng ta có thể sử dụng dấu * 
def thoikhoabieu(*monhoc):
    print("mon 1"+monhoc[0])
    print("mon 2"+monhoc[1])
thoikhoabieu("toan","li")

def tinhtong(*giatri):
    sum=0
    for x in giatri:
        sum+=x
    print(sum)
tinhtong(1,2,3,4,5,6,7,8,9,10)
# Truyền nhiều đối số, xác định thông qua tên, sử dụng **
def hello(**hoten):
    print("xin chao "+hoten["ho"])
hello(ten="loi",ho="Doan")
class sinhVien:
    def __init__(self,name,id):
        self.name=name
        self.id=id 
        pass
sv1=sinhVien("loi",222)
print(sv1.name)
print(type(sv1))
sv1.name="nguyen van a"
print(sv1.name)

class simple:
    # contructor
    def __init__(self):
        self.name="nguyen van b "
        pass
    def hienthi(self):
        print("hello "+self.name)

    #static methods
    @staticmethod
    def hello(name):
        print("hello "+name)
sv2=simple()
sv2.hienthi()
simple.hello("c")
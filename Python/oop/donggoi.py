class sinhVien:
    def __init__(self,ten,_diem,__cannang):
        self.ten=ten # thuộc tính public 
        self._diem=_diem # thuộc tính protected
        self.__cannang=__cannang # thuộc tính private
        pass

    @property
    def cannang(self):
        return self.__cannang
    @cannang.setter
    def cannag(self,cannang):
        if 0<=self.cannang<=100:
            self.__cannang=self.cannang
        else :
            print("loi")

sv = sinhVien("Lợi", 8, 60)
print(sv.ten)
print(sv._diem)
print(sv.cannang)
print(sv.cannang)
        
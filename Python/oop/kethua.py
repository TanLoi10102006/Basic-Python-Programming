class DongVat:

    def __init__(self, ten):
        self.ten = ten

    def keu(self):
        print("dong vat keu")

    def an(self):
        print("dang an")


class Cho(DongVat):

    def __init__(self, ten, tuoi):
        super().__init__(ten)  # Dùng super() chuẩn OOP
        self.tuoi = tuoi


cho = Cho("Milu", 3)
print(cho.ten)
print(cho.tuoi)


class Meo(DongVat):

    def __init__(self, ten, can_nang):
        super().__init__(ten)
        self.can_nang = can_nang

    def meokeu(self):  # Sửa sef -> self
        super().keu()
        print("meu meu")


meo = Meo("A", 55)
meo.meokeu()

# Kế thừa nhiều cấp:
print("===========KE THUA NHIEU CAP==========")


class DongVatCoVu(DongVat):

    def uongSua(self):
        print("Đang uống sữa")


class Gau(DongVatCoVu):

    def sua(self):
        print("go go")

GAU = Gau("Gấu Misa")
GAU.an()
GAU.uongSua()
GAU.sua()

#  đa kế thừa 
class A:
    def hello_a(self):
        print("Hello A")


class B:
    def hello_b(self):
        print("Hello B")


class C(A, B):
    pass
c = C()

c.hello_a()
c.hello_b()

# đa hình 
class Vit:

    def keu(self):
        print("Quạc quạc!")


class ga:

    def keu(self):
        print("Gâu gâu!")


class XeOTo:

    def keu(self):
        print("Bíp bíp!")

def phat_am_thanh(doi_tuong):
    doi_tuong.keu()

phat_am_thanh(Vit())
phat_am_thanh(ga())  
phat_am_thanh(XeOTo())
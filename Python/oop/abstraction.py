from abc import ABC, abstractmethod

class DongVat(ABC):

    def __init__(self, ten):
        self.ten = ten

    @abstractmethod
    def keu(self):
        pass
class Cho(DongVat):

    def keu(self):
        print("Gâu gâu!")

cho = Cho("Cún")

print(cho.ten)
cho.keu()
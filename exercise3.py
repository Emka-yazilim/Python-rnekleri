import time

class Yazilimci():

    def __init__(self,isim,soyadi,diller,alan,maas):

        self.isim = isim
        self.soyadi = soyadi
        self.diller = diller
        self.alan = alan
        self.maas = maas

#yeni dil eklemek için fonk. oluşturduk.
    def dil_ekle(self,yeni_dil):
        print("Dil Ekleniyor...")
        self.diller.append(yeni_dil)

# yeni alan eklemek için fonk. oluşturduk.
    def alan_ekle(self,yeni_alan):
        print("Yeni Alan Ekleniyor...")
        self.alan.append(yeni_alan)

#maaşa zam yapmak için fonk. oluşturduk.
    def zam(self,miktar):
        self.maas +=miktar

#bilgileri ekrana göstermek için fonk. oluşturduk.
    def bilgilerigoster(self):
        print(" Yazılımcı Bilgileri Listeleniyor...")
        time.sleep(1)
        print("""
        İsim: {}
        Soyadı: {}
        Bildiği Diller: {}
        Uzmanlık Alanı: {}
        Maaş: {}
        
        """.format(self.isim,self.soyadi,self.diller,self.alan,self.maas))


yazilimci =Yazilimci("Emir","Karabulak",["Python"],["Yapay Zeka"],4500)

print(yazilimci.bilgilerigoster())

#yeni dil ekledim ve ekrana bastırdım.
print(yazilimci.dil_ekle("R,C++"))
print(yazilimci.bilgilerigoster())

#yeni alan ekledim ve ekrana bastırdım.
print(yazilimci.alan_ekle("OpenCV"))
print(yazilimci.bilgilerigoster())

#maaşa zam yaptım ve ekrana bastırdım
print(yazilimci.zam(1500))
print(yazilimci.bilgilerigoster())


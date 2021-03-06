import  time

class Computer():

    def __init__(self,pc_durum="kapali" , pc_wifi="kapali", pc_ses=0,
                 pc_parlaklık=0,pc_bluetooth="kapalı" ,program_indirme=[]):

        self.pc_durum = pc_durum
        self.pc_wifi=pc_wifi
        self.pc_ses=pc_ses
        self.pc_parlaklık=pc_parlaklık
        self.pc_bluetooth=pc_bluetooth
        self.program_indirme=program_indirme




#pc durumun açık olma olasılığı için fonk. yazdık
    def pc_on(self):
        if(self.pc_durum == "Açık"):
            print("Bilgisayarınız Açık")

        else:
            print("Bilgisayar Açılıyor.\nLütfen Bekleyiniz...")
            time.sleep(1)
            print("Bilgisyar Açıldı...")
            self.pc_durum="Açık"





# pc durumun kapalı olma olasılığı için fonk. yazdık
    def pc_off(self):
        if(self.pc_durum == "Kapalı"):

            print("Bilgisayar Kapalı")

        else:
            print("Bilisayar Kapatılıyor.\nLütfen Bekleyiniz...")
            time.sleep(1)
            print("Bilgisayar Kapatıldı...")
            self.pc_durum ="Kapalı"







# pc wifi durumun açık olma olasılığı için fonk. yazdık
    def wifi_on(self):
        if (self.pc_wifi =="Açık"):
            print("Wifi açık")
            print("İnternete Bağlı")

        else:
            print("Wifi Açılıyor\nLütfen Bekleyiniz...")
            time.sleep(0.7)
            print("Wifi Açıldı")
            print("İnternete Bağlanılıyor...")
            time.sleep(0.7)
            print("İnternete Bağlandı...")
            self.pc_wifi="Açık"






# pc wifi durumun kapalı olma olasılığı için fonk. yazdık
    def wifi_off(self):
        if(self.pc_wifi == "Kapalı"):
            print("Wifi Kapalı")

        else:
            print("Wifi Kapatılıyor.\nLütfen Bekleyiniz...")
            time.sleep(0.7)
            print("Wifi Kapatıldı...")
            self.pc_wifi="Kapalı"






# pc ses açma ve kapamak için fonk. yazdık
    def ses(self):
        print("Ses Açma Tuşu : '+'\nSes Kısma Tuşu:'-'\nÇıkmak İçin:'q'")
        while True:

            cevap=input("İşleminizi Giriniz:")

            if (cevap == "q"):
                print("Ses ayarları güncellendi...\nGüncel ses:{}".format(self.pc_ses))
                time.sleep(0.7)
                print("Programdan Çıkılıyor...")
                print("Programdan Çıkıldı")
                break

            elif(cevap=="+"):
                if(self.pc_ses !=100):
                    self.pc_ses +=1
                    print("Ses: {}".format(self.pc_ses))

            elif(cevap=="-"):
                if(self.pc_ses !=0):
                    self.pc_ses -=1
                    print("Ses: {}".format(self.pc_ses))








# pc parlaklık açma ve kapamak için fonk. yazdık


    def parlaklik(self):
        print("Parlaklık Açma Tuşu : '+'\nParalaklık Kısma Tuşu:'-'\nParlaklık İçin:'q'")
        while True:

            cevap = input("İşleminizi Giriniz:")

            if (cevap == "q"):
                print("Parlaklık ayarları güncellendi...\nGüncel Parlaklık:{}".format(self.pc_parlaklık))
                time.sleep(0.7)
                print("Programdan Çıkılıyor...")
                print("Programdan Çıkıldı")
                break

            elif (cevap == "+"):
                if (self.pc_parlaklık != 100):
                     self.pc_parlaklık += 1
                     print("Parlaklık: {}".format(self.pc_parlaklık))

            elif (cevap == "-"):
                if (self.pc_parlaklık != 0):
                     self.pc_parlaklık -= 1
                     print("Parlaklık: {}".format(self.pc_parlaklık))







#pc bluetoooth açma için fonk. yazdık

    def blue_on(self):
        if (self.pc_bluetooth == "Açık"):
            print("Bluetooth Açık")

        else:
            print("Bluetooth Açılıyor.\nLütfen Bekleyiniz...")
            time.sleep(0.7)
            print("Bluetooth Açıldı...")
            self.pc_bluetooth = "Açık"







#pc bluetoooth kapamak için fonk. yazdık
    def blue_off(self):
        if(self.pc_bluetooth == "Kapalı"):

            print("Bluetooth Kapalı")

        else:
            print("Bluetooth Kapatılıyor.\nLütfen Bekleyiniz...")
            time.sleep(1)
            print("Bluetooth Kapatıldı...")
            self.pc_bluetooth ="Kapalı"






#dosya indirmek için yazdığımız fonk.

    def indirme(self,dosya_ismi):
        print("Program İndiriliyor\nLütfen Bekleyin....")
        time.sleep(0.7)
        self.program_indirme.append(dosya_ismi)
        print("Program İndirildi")





    def __str__(self):
        return "Bilgisayar Durumu: {}\nWifi Durumu: {}\n Ses: {}\nParlaklık: {}\nBluetooth: {}\nİndirilen Programlar: {}" .format(self.pc_durum,self.pc_wifi,self.pc_ses,self.pc_parlaklık,self.pc_bluetooth,self.program_indirme)




bilgisayar =Computer()




print(""" 
Başlangıç Menüsüne Hoşgeldiniz
***********************************
1.Bilgisayarı Açma

2.Bilgisayar Kapama 

3.WİFİ Bağlantısı Açma

4.WİFİ Bağlantısı Kapama

5.Ses

6.Parlaklık

7.Bluetooth Açma

8.Bluetooth Kapama

9.Program İndirme

Programdan çıkmak için 'q'

""")

while True:
    işlem=input("Yapmak İstediğiniz İşlemi Tuşlayınız: ")

    if (işlem=="q"):
        print("Program Sonlandırıldı.")
        break

    elif (işlem=="1"):
        bilgisayar.pc_on()

    elif (işlem=="2"):
        bilgisayar.pc_off()

    elif (işlem=="3"):
        bilgisayar.wifi_on()

    elif (işlem=="4"):
        bilgisayar.wifi_off()

    elif (işlem=="5"):
        bilgisayar.ses()

    elif (işlem=="6"):
        bilgisayar.parlaklik()

    elif (işlem=="7"):
        bilgisayar.blue_on()

    elif (işlem=="8"):
        bilgisayar.blue_off()

    elif (işlem=="9"):
        program_isimleri = input("Program isimlerini ',' ile ayırarak girin:")

        program_indirme =program_isimleri.split(",")

        for eklenecekler in program_indirme:
            bilgisayar.indirme(eklenecekler)
        print(bilgisayar.program_indirme)

    else:
        print("Geçersiz İşlem")
        break













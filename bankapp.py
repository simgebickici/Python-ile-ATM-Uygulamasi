import datetime

class Musteri():
    def __init__(self,ID,Isim,Parola):
        self.id=ID
        self.isim=Isim
        self.parola=Parola
        self.bakiye=0
        
class Hesap():
    def __init__(self,ID,Isim):
        self.id=ID
        self.isim=Isim
        self.bakiye=0
    
class Banka():
    def __init__(self):
        self.musteriler=list()
        
    
    def musteri_olmak(self,ID:str,Isim:str,Parola:str):
        self.musteriler.append(Musteri(ID,Isim,Parola))
        print("Bankaya kaydınız yapılmıştır.")

class Baska_hesap():

    def __init__(self):
        self.hesaplar=list()
      
    def hesap_ekleme(self,ID:str,Isim:str):
        self.hesaplar.append(Hesap(ID,Isim))
        print("Kayıt yapılmıştır.")
    
        
def main():
    banka=Banka()
    baska_hesap=Baska_hesap()
    while True:
        print("""
              [1] Banka Müşterisiyim
              [2] Banka Müşterisi Olmak İstiyorum
              [3] Para Gönderilecek Kişiyi Kaydetmek İstiyorum
              """)
        
        secim=input("Seçiminiz nedir?: ")
        
        if secim=="1":
            ids=[i.id for i in banka.musteriler]
            ID=input("ID: ")
            if ID in ids:
                for musteri in banka.musteriler:
                    if ID==musteri.id:
                        print("Hoşgeldiniz {}".format(musteri.isim))
                        parola=input("Parolanız: ")
                        if parola==musteri.parola:
                            while True:
                                print("""
                                      [1] Bakiye Sorgulama
                                      [2] Kendi Hesabına Para Yatırma
                                      [3] Başkasının Hesabına Para Yatırma
                                      [4] Para Çekme
                                      [0] Çıkış
                                      """)
                                
                                secim2=input("Seçiminiz: ")
                                if secim2=="1":
                                    print("Bakiyeniz: {}".format(musteri.bakiye))
                                    input("Ana menüye dönmek için enter e basınız.")
                                    
                                elif secim2=="2":
                                    miktar=int(input("Yatırmak istediğiniz tutar: "))
                                    onay=input("Kendi hesabınıza {} TL para yatırma işlemini onaylıyor musunuz?: Evet/Hayır\n")
                                    
                                    if onay=="Evet" or onay=="evet":
                                        musteri.bakiye+=miktar
                                        print("Paranız yatırıldı.")
                                        input("Ana menüye dönmek için enter e basınız.")
                                        
                                    elif onay=="Hayır" or onay=="hayır":
                                        print("İşleminiz iptal edildi.")
                                        input("Ana menüye dönmek için enter e basınız.")
                                        
                                    else:
                                        print("Hatalı giriş yapıldı, işlem iptal edildi.")
                                        input("Ana menüye dönmek için enter e basınız.")
                                        
                                elif secim2=="3":
                                    arananID=input("Para yatırılması istenilen kişinin ID numarası: ")
                                    for digermusteri in baska_hesap.hesaplar:
                                        if arananID==digermusteri.id:
                                            miktar=int(input("Yatırmak istediğiniz tutar: "))
                                            if miktar<=musteri.bakiye:
                                                onay=input("{} adlı müşteriye para {} TL para yatırma işlemini onaylıyor musunuz?: Evet/Hayır\n")                                                    
                                                if onay=="Evet" or onay=="evet":
                                                    digermusteri.bakiye+=miktar
                                                    musteri.bakiye-=miktar
                                                    print("Para yatırıldı.")
                                                    input("Ana menüye dönmek için enter e basınız.")
                                                    
                                                elif onay=="Hayır" or onay=="hayır":
                                                    print("İşleminiz iptal edildi.")
                                                    input("Ana menüye dönmek için enter e basınız.")
                                                        
                                                else:
                                                    print("Hatalı giriş yapıldı, işlem iptal edildi.")
                                                    input("Ana menüye dönmek için enter e basınız.")
                                            else:
                                                print("Bakiyeniz bu işlem için yeterli değildir.")
                                                
                                elif secim2=="4":
                                    miktar=int(input("Kartınızdan çekmek istediğiniz tutar: "))
                                    if miktar<=musteri.bakiye:
                                        onay=input("Hesabınızdan {} TL para çekme işlemini onaylıyor musunuz?: Evet/Hayır\n")
                                        if onay=="Evet" or onay=="evet":
                                            musteri.bakiye-=miktar
                                            print("İşlem tamamlandı, paranızı alabilirsiniz.")
                                            input("Ana menüye dönmek için enter e basınız.")
                                        
                                        elif onay=="Hayır" or onay=="hayır":
                                            print("İşleminiz iptal edildi.")
                                            input("Ana menüye dönmek için enter e basınız.")
                                            
                                    else:
                                        print("Bakiyeniz bu işlem için yeterli değildir.")
                                        input("Ana menüye dönmek için enter e basınız.")
                                        
                                elif secim2=="0":
                                    break
                    
            else:
                print("Bu bankanın müşterisi olarak bulunmamaktasınız.")
                input("Ana menüye dönmek için enter e basınız.")  
                
        elif secim=="2":
            ID=input("ID: ")
            Isim=input("İsminiz: ")
            Parola=input("Parolanız: ")
            f=open("Musteri_listesi.txt", "a+")
            f.write("ID: %s" % ID)
            f.write("    Ad: %s" % Isim)
            an = datetime.datetime.now()
            tarih = datetime.datetime.strftime(an, '%c')
            f.write("     -------> %s\n" % tarih)
            f.close()
            banka.musteri_olmak(ID,Isim,Parola)
            
        elif secim=="3":
            ID=input("ID: ")
            Isim=input("İsim: ")
            f=open("Kaydedilen_hesap_listesi.txt", "a+")
            f.write("ID: %s" % ID)
            f.write("   Ad: %s" % Isim)
            an = datetime.datetime.now()
            tarih = datetime.datetime.strftime(an, '%c')
            f.write("     --------> %s\n" % tarih)
            f.close()
            baska_hesap.hesap_ekleme(ID,Isim)
            print("Hesap başarıyla kaydedildi.")
                                
main()
                                
                            
                        
        
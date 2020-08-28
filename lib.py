class User:
    def __init__(self,_ad,_soyad,_username,_password):
        self.ad=_ad
        self.soyad=_soyad
        self.username=_username
        self.password=_password
    def userleriGoster(self):
        print(f"Adi : {self.ad} \nSoyadi : {self.soyad}  \nIstifadeci adi : {self.username}")
        print("Istifadeci Melumatlari Gosterildi ... ")

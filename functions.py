from lib import User
from db import userData
def userMelumatlariniAl():
    u_ad=input("Adi : ")
    u_soyad=input("Soyadi : ")
    u_username=input("Istifadeci adi : ")
    u_password=input("Istifadeci parolu : ")
    return [u_ad,u_soyad,u_username,u_password]

def userMelumatlariniGoster():
    for user in userData:
        user.userleriGoster()
def userYaratVeDatayaElaveEt():
    userData.append(User(*userMelumatlariniAl()))
def userQeydiyyat():
    userSayi=int(input("Daxil olunacaq User sayi : "))
    for say in range(userSayi):
        say+=1
        print(f"{say}. Istifadeci Melumatlari ... ")
        userYaratVeDatayaElaveEt()
def executeOrders():
    print("Qeydiyyat baslatmaq ucun ( 1`i daxil edin ) : ")
    print("Melumatlari gostermek ucun ( 2`ni daxil edin ) : ")
    order=int(input("Secim ucun reqemi daxil edin : "))
    if order==1:
        userQeydiyyat()
    elif order==2:
        userMelumatlariniGoster()

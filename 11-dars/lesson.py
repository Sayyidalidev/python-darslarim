# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     print('Sizga kirish bepul.')
# elif yosh<=12:
#     print('Sizga kirish 5000 so\'m')
# else:
#     print('Sizga kirish 10000 so\'m')

# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# else:
#     price = 10000
    
# print(f"Sizga kirish {price} so'm")

# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4: # yosh bolalarga bepul
#     price = 0
# elif yosh<=12: # 4 dan 12 yoshgacha 5000 so'm
#     price = 5000
# elif yosh<65: # 12 dan katta va 65 dan kichiklarga narh 10000 so'm
#     price = 10000
# else: # qariyalarga esa 8000 so'm
#     price = 8000
# print(f"Sizga kirish {price} so'm")


# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# elif yosh<65:
#     price = 10000
# elif yosh>=65:
#     price = 8000    
# print(f"Sizga kirish {price} so'm")

# kun = input("Bugun nima kunga  >>> ")

# if kun.lower() == 'yakshanba' or kun.lower() == 'shanba':
#     print("bugun dam olish kuni")
# else:
#     print('Bugun ish kuni')

# kun = input("Bugun nima kunga >>> ")
# harorat = float(input("Bugun harorat nechchi daraja >>> "))

# if (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat >= 30:
#     print('Cho\'milgani kettik')
# elif (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat < 30:
#     print("Uyda dam olamiz")
# else:
#     print("Bugun ish kuni")

# narx = 10000
# choy = True
# salat = False

# if choy and salat:
#     narx = narx + 10000
# elif choy or salat:
#     narx = narx + 5000

# print(f"Jami narx {narx} so'm ")

# narx = 10000
# choy = 1
# salat = 0
# non = 1
# kompot = 1
# assorti = 1

# if choy:
#     narx = narx + 5000
#     print("Mijoz choy oldi")
# if salat:
#     narx = narx + 5000
#     print("Mijoz salat oldi")
# if non:
#     narx += 3000
#     print("Mijoz non oldi")
# if kompot:
#     narx += 7000
#     print("Mijoz kompot oldi")
# if assorti:
#     narx += 20000
#     print("Mijoz assorti oldi")

# print(f"Jami narx {narx} so'm ")

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input("Nima yeysiz ? >>>")

# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi ')
# else:
#     print("Afsuski bizda bunday taom yo'q ")

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() not in menu:
#     print('Afsuski bizda bunday ovqat yo\'q')
# else:
#     print('Buyurtma qabul qilindi.')

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]

# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Kechirasiz, menuda {taom} yo'q")

menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]

if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q")
else: # agar ro'yxat bo'sh bo'lsa
    print("Savatchangiz bo'sh!")
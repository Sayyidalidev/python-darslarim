user = float(input("Iltimos muzeyga kirish narxini bilish uchun yoshingizni kiriting >>> "))

if  user <= 4 or user >= 60:
    price = 0
elif user <= 18:
    price = 10000
elif user > 18:
    price = 20000

print(f"Muzeyga kirish uchun sizga narx {price} so'm")
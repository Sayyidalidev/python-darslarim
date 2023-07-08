mahsulotlar = ['kartoshka', 'gosht', 'non', 'sabzi', 'pomidor', 'bodring', 'mayonez', 'ketchup', 'tuxum', 'guruch', 'karam', 'qalampir']

print("Iltimos 5 ta mahsulot qo'shing \n")

savat = [ ]
savat.append(input("Savatga 1-mahsulotni qo'shing "))
savat.append(input("Savatga 2-mahsulotni qo'shing "))
savat.append(input("Savatga 3-mahsulotni qo'shing "))
savat.append(input("Savatga 4-mahsulotni qo'shing "))
savat.append(input("Savatga 5-mahsulotni qo'shing "))

bor_mahsulotlar = []
mavjud_emas = []

for x in savat:
    if x in mahsulotlar:
        bor_mahsulotlar.append(x)
    elif x not in mahsulotlar:
        mavjud_emas.append(x)
    elif x in mahsulotlar and mavjud_emas not in mahsulotlar:
        print("Do'konimizda siz so'ragan barcha mahsulotlar bor")



print("Do'konimizda bor mahsulotlar: ")
for n in bor_mahsulotlar:
    print(n)
print("Do'konimizda yo'q mahsulotlar: ")
for m in mavjud_emas:
    print(m)
    
    
    # mahsulotlar = ["olma", "banan", "uzum", "nok", "anor"]
    # bor_mahsulotlar = []
    # mavjud_emas = []

    # for i in range(5):
    #     mahsulot = input(f"{i+1}-mahsulotni kiriting: ")
    #     if mahsulot in mahsulotlar:
    #         bor_mahsulotlar.append(mahsulot)
    #     else:
    #         mavjud_emas.append(mahsulot)

    # if mavjud_emas:
    #     print("Quyidagi mahsulotlar do'konimizda yo'q:")
    #     for mahsulot in mavjud_emas:
    #         print(mahsulot)
    # else:
    #     print("Siz so'ragan barcha mahsulotlar do'konimizda bor.")


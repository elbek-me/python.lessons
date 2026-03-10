# Takrorlash operatorlari
# for loop
# while (toki)loop
# 1 dan 10 gacha sonlar chiqarish
# for son in range(1,10):
#     print(son)

# son = 1
# while son <= 10:
#     print(son)
#     son += 1  # o'chrilsa infinify loopga o'tadi

# infinity loop - cheksiz sikl / qayta qayta ishlaydi
# while True:
#     print("infinity loop")   bunday qilishdan qochish kerak
# while va input()

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ""
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
#     else:
#         print("Dastur ishlashdan to'xtadi.")
       
# Ishora (flag)
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)


# break(sindirish) operatori
# sonlar = list(range(1,11))  
# for son in sonlar:
#     if son == 5: # son 5 ga teng bo'lsa kod toxatiladi
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True: # abadiy tsikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break # tsiklni to'xtatish
#     else:
#         print(float(qiymat)**2)

# continue(davom etish) operatoris
# sonlar = list(range(1,11))  
# for son in sonlar:
#     if son == 5: # son 5 ga teng bo'lsa tsikl boshiga davom etadi
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")

# son = 0
# while son < 10:
#     son += 1
#     if son % 2 != 0:
#         continue
#     else:
#      print(son)

# Abadiy sikl tuzog'i
# infinity loop 
# son=0
# while son < 10:
#     son += 1  # bolmasa infinify loopga o'tadi
#     if son % 2 != 0:
#         continue
#     else:
#         print(son)

# kitob = ""
# while kitob != 'stop':
#     kitob = input("Yaxshi ko'rgan kitobingizni kiriting: ")
#     if kitob != 'stop':
#         print(f"Siz {kitob} yaxshi ko'rgan kitobingiz")



# yaqin do'stingizning ro'yhatini tuzuvchi dastur
# dostlar = []
# while True:
#     dost = input("Do'stingizni kiriting to'xtatish uchun 'exit' deb yozing): ")
#     if dost == 'exit':
#         break
#     dostlar.append(dost)
# print("Sizning do'stlaringiz ro'yhati:")
# for dost in dostlar:
#     print(dost)

# ismlar = {}
# ishora = True
# while ishora:
#     ism = input("Ismingizni kiriting: ")
#     yosh = input("Yoshingizni kiriting: ")
#     ismlar[ism] = yosh
#     javob = input("Yana ma'lumot kiritasizmi: ")
#     if javob == 'exit':
#         ishora = False
# print("Ismlar va yoshlar ro'yhati:")
# for ism, yosh in ismlar.items():
#     print(f"ism {ism}: {yosh} yosh")


# students = ['Behruz', 'Elbek', 'Dilbek', 'Rahimboy', 'Gulomjon']
# baholar = {}
# while students:
#     talaba = students.pop()
#     baho = input(f"{talaba} bahosini kiriting: ")
#     baholar[talaba] = baho
# print("students va ularning baholari:")
# for talaba, baho in baholar.items():
#     print(f"{talaba}: {baho}")


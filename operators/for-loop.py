# # takrorlash operatorlari
# # loop - skill
# # 1. for loop
# # 2. whil loop
# students = ['elbek','maftuna','g\'ulomjon','mahliyo','dilbek']
# # hard coding
# # print(students[0])
# # print(students[1])
# # print(students[2])
# # print(students[3])
# # print(students[4])
# for student in students:
#     print(student)

# # sonlar ro'hati bo'yich ishash
# even_numbers =list(range(2,51,2)) # 2 dan 50 gacha bo'lgan juft sonlar ro'hati
# for number in even_numbers:
#     print(number)

# print("Dastur tugadi.")

# students = ["Alice", "Bob", "Charlie", "David", "Eve"]
# for student in students:    
#     print(student)

# # 1-iteratsiya student = "Alice"
# # 2-iteratsiya student = "Bob"
# # 3-iteratsiya student = "Charlie"
# # 4-iteratsiya student = "David"    
# # 5-iteratsiya student = "Eve"

# for guest in students:
#     print(f"Hurmatli {guest}, sizni interviewga taklif qilmoqchiman.")
#     print("Hurmat bilan, Al-Xorazmiy vorislari loyihasi.")

# # Sonlar ro'yxati uchun for loop    
# even_numbers = list(range(2, 51, 2)) # 2 dan 50 gacha bo'lgan juft sonlar ro'yxati
# for number in even_numbers:
#     print(number)

# print("Dastur tugadi.")

# # 1 ning kvadrati 1 ga teng.
# # 2 ning kvadrati 4 ga teng.
# # 3 ning kvadrati 9 ga teng. 
# sonlar = list(range(1, 11)) # 1 dan 10 gacha bo'lgan sonlar ro'yxati
# for son in sonlar:
#     print(f"{son} ning kvadrati {son ** 2} ga teng.")


# numbers = list(range(20))  
# # start_default_value = 0
# # stop = 20
# # step_default_value = 1
# print(numbers)
# sonlar = list(range(-20,21)) 
# for son in sonlar:
#     print(son)

# people = ['elbek','maftuna','g\'ulomjon','mahliyo','dilbek']
# for person_name in people:
#     print(person_name)

# # 2-usul:range() funksiyasi yordamida indekslar orqali interatsiya qilish
# for index in range(len(people)):
#    print(index)
#    print(people[index])
     
# 1-literatsiya index = 0, people[index] = "elbek"
# 2-literatsiya index = 1, people[index] = "maftuna"
# 3-literatsiya index = 2, people[index] = "g'ulomjon"
# 4-literatsiya index = 3, people[index] = "mahliyo"
# 5-literatsiya index = 4, people[index] = "dilbek"
# for son in range(1,101):
#     print(sonlar)

# sonlar = list(range(1, 101))
# # for son in sonlar:
# #     print(son)
# for index in range(len(sonlar)):   
#     print(index)
#     print(sonlar[index])

# 1-marta: index= 0 => sonlar[0 = 1]
# 2-marta: index= 1 => sonlar[1 = 2]
# ...
# 99-marta: index= 98 => sonlar[98 = 99]


# for number in range(1,200):
#     print(f"{number} ning kvadrati  {number ** 2} ga teng ")

# number_of_friends = int(input(" Do'stingiz sonini kiriting : "))
# friends = [] 
# if (number_of_friends == 0):
#     print("sizning do'stingiz yo'qmi ? ")
# else:
#     for n in range(number_of_friends):
#        friend = input(f"{n+1}-Do'stingizning ismini kiriting: ")
#        friends.append(friend)
#     print(friends)


# ismlar = ['Elbek','Elbek','Elbek','Elbek','Elbek']
# for ism in ismlar:
#     print(f"Salom, {ism}. bugun darsga borasiizmi")

# print(f"Kod {len(ismlar)} marta takrorlandi")


# sonlar = list(range(1,10,2))
# for son in sonlar:
#     print(son**3)


# kinolar = []
# print("5 ta sevimli kinoingizni kiriting :")
# for son in range(5):
#     kinolar.append(input(f"{son+1}-sevimli kinongiz:"))
# print(kinolar)   



# kishilar_soni = int(input("Bugun necha kishi bn suhbat qildingiz :"))
# ismlar = []
# for n in range(kishilar_soni):
#     ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi : "))
# print(ismlar)




# s = 0
# numbers=[12,5,18,25,23]
# for number in numbers:
#     s +=number
# print(s)

# summa = 0
# for son in range (1, 50,2):
#     summa +=son
# print(summa)

# numbers= [12,5,18,25,23,88,-52]
# for number in numbers:
#    s += number 
# average_value = s / len(numbers)
# print(average_value)

# import math
# l = len(numbers)
# k=1
# for number in numbers:
#   k*=number
# a= math.pow(k,1/1)



# juftlar_kopaytmasi = 1
# toqlar_yigindisi = 0
# for son in range(1,21):
#     if son % 2 == 0:
#         juftlar_kopaytmasi *= son
#     else:
#         toqlar_yigindisi += son
# bolinishi = juftlar_kopaytmasi / toqlar_yigindisi
# print(f"Juft sonlar ko'paytmasi: {juftlar_kopaytmasi}")
# print(f"Toq sonlar yig'indisi: {toqlar_yigindisi}")
# print(f"Nisbat: {bolinishi}")
# s = 0
# couter = 0 
# numbers = [7,97,-58,90]
# for number in numbers:
#     if number % 2 ==0:
#         s +=number
#         couter +=1
# print(s/couter)        



# n = int(input("1-son :"))


# a = list( input("2-son :"))

# numbers = 0
# for number in range(n):
#     if a[number] % 2 == 0 or a[number] % 3 == 0 or a[number] % 5 == 0:
#         numbers += a[number]

# print(numbers)

# Birinchi qator: n sonini kiritish (masalan, 97)
# s =0 
# numbers = [97, 97, -92, 14, 22]
# for number in numbers:
#     if number % 2 == 0 or number % 3 ==0 or number % 5 == 0:
#         s+=number
#         print(s)

# s = 0
# couter = 0 
# numbers = [76, 12 ,51 ,50 ,98]
# for number in numbers:
#     if number % 2 ==1:
#         s+= number
#         couter+=1
# print(s/couter)

# numbers = [76, 12 ,51 ,50 ,98]
# n = int(input())
# arr = list(map(int, input().split()))


# kvadratlar_yigindisi = sum(x**2 for x in arr)


# ortacha_qiymat = sum(arr) / n


# print(kvadratlar_yigindisi)
# print(f"{ortacha_qiymat:.2f}")

# import math
# n = 8
# a = [7, 24, -5, 23 ,99 ,-3, 24, 51]
# urtacha_qiymat = sum(a) / n
# log_qiymat = math.log(urtacha_qiymat)
# natija = []
# for x in a:
#     if x < 0:
#         natija.append(f"{log_qiymat:.2f}")
#     else:   
#         natija.append(f"{x:.2f}")

# print(" ".join(natija))



# import math
# a =[7, 24, -5, 23 ,99 ,-3, 24, 51]
# s=0
# for num in a:
#    s +=num
# lenght=len(a)
# average_value = s / lenght
# log_value=math.log(average_value)

# for index in range (lenght):
#    if a[index] <0:
#       a[index]=log_value
# print(a)
      

# a = [46, 23, -52, 34, 6, -18, 52]
# min_qiymat = min(a)
# kvadrat = min_qiymat ** 2
# for n in range(len(a)):
#     if a[n] < 0:
#         a[n] = kvadrat
# print(a)
# numbers=[3,17,-59]
# s=0
# for index in range (len(numbers)):
#     s+=numbers[index]
# for nunber in numbers:
#     if nunber % 2==1:
#         print(nunber /s," ")
#     else:
#         print(nunber," ")




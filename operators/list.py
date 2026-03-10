# List - ro'yhat
# user1 = "Elbek"
# user2 = "Behruz"
# print(user1)
# print(type(user2)) #str
# users = ['Gulyora', "G'ulomjon", 'John', 'Margaritta']
# List elementlari indekslanadi
# Dasturlashda indekslash 0 dan boshlanadi
# List elementini olish
# first_element = users[0]
# third_element = users[2]
# print(first_element,third_element,users[3])
# print(type(users)) #list
# mixed_data = ['test',12, True,-5.75]

# Listdan element sug'urib olish
# list.pop(index?)
# bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
# mahsulot = bozorlik.pop(3) 
# print("Men " + mahsulot + " sotib oldim")
# print("Olinmagan mahsulotlar: ", bozorlik)

# ismlar=['behruz','ibrohim']
# print(f"salom {ismlar[1]} ahvollaring qanday \n {ismlar[0]} bugun darsga kelasanmi")

# sonlar = [22,58,34,67,98,114]
# print(sonlar)
# sonlar[0] = sonlar[0]+sonlar[-1]
# sonlar[1] = 69
# sonlar[4] = sonlar[4] + 50
# print(sonlar)

# a_shaxs=['amir temur','abu rayhon beruniy','alisher navoiy']
# b_shaxs = ['Bill Gates', 'Elon Musk', 'Doasnald Trump']

# print(f"""Men tarixiy shaxslardan {a_shaxs.pop(1)} bilan
# zamonaviy shaxslardan esa {b_shaxs.pop(0)} bilan
# suhbat qilishni istar edim""")

# friends = []
# friends.append('hasan')
# friends.append('umid')
# friends.append('nurmurod')
# friends.append('ibrohim')
# friends.append('behruz')
# print(friends)
# friends.remove('hasan')
# friends.remove('ibrohim')
# print(friends)


# mehmonlar = []
# mehmonlar.append(friends.pop(0))
# mehmonlar.append(friends.pop(1))
# mehmonlar.append(friends.pop(-1))
# print("Kelgan mehmonlar: ", mehmonlar)

# list.sort()
# friends = ['zaynab', 'dilmira','lobar','maftuna','zaynab']
# friends.sort()
# print(friends)
# friends.sort(reverse=True)
# print(friends)

# # sorted() function
# sorted_list = sorted(friends,reverse=True)
# print(friends)
# # print(sorted_list)
# nums = [10,20,30,40,50,60]
# # nums.sort()  # o'sish
# # print(nums)
# # print(sorted(nums,reverse=True))
# nums.reverse()
# print(nums)



# List bilan ishlash
# list methods
# 1. list.append(element)
# 2. list.insert(index, element)
# 3. list.remove(element)
# 4. list.pop(index?)
# 5. list.sort()
# cars = ['bmw','mercedes benz', 'volvo', 'damas', 'general motors', 'tesla', 'audi']
# cars.sort() # alifbo(english) ketma-ketlik bo'yicha tartiblash
# print(cars)
# cars.sort(reverse=True) # reverse(teskari)
# print(cars)
# sorted_list = sorted(cars)
# reversed_sort_list = sorted(cars, reverse=True)
# print(cars)
# print(sorted_list)
# print(reversed_sort_list)

# ages = [12, 98, 34, 65, 34, 76, 11]
# ages.sort() # o'sish tartibi
# print(ages)
# print(sorted(ages, reverse=True)) # kamayish tartibi

# # list.reverse() 
# fruits = ['pear','banana','apple','watermelon','lemon']
# fruits.reverse()
# print(fruits)
# print(len(fruits)) # 5

# # list() funksiyasi
# users = ['akmal', 'farzona', 'shodlik']
# students = list(('jamol', 'asal', 'kamol', 'zebo')) # ['jamol', 'asal', 'kamol', 'zebo']
# print(students)
# # range() funksiyasi - ma'lum bir oraliqdagi sonlarni shakllantirish uchun ishlatilanadi
# # range(start, stop, step?)
# # step = 1(default value)
# # range(0, 10) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# # range(2, 20, 2) # 2, 4, 6, 8, ... 16, 18
# sonlar = list(range(0, 10))
# juft_sonlar = list(range(2, 21, 2))
# print(sonlar)
# print(juft_sonlar)

# # min() - eng kichik, max() - eng katta, sum() - yig'indi
# # min(12, 15, 56, -2, 0, 99) # -2
# narxlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874] 
# eng_arzoni = min(narxlar)
# eng_qimmati = max(narxlar)
# print(eng_arzoni)
# print(eng_qimmati)
# yigindi = sum(narxlar)
# print(yigindi)

# listni kesish
# techs = ['AI', 'Robot', 'Python', 'DB', 'Chat GPT', 'Web']
# # new_list = list[start : end]
# my_techs = techs[2 : 5]
# print(my_techs)
# print(techs[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
# print(techs[2:]) # 2-indexdagi elementdan boshlab ro'yxat oxirigacha kesib oladi
# # new_list=list[start_index : end_index]
# # 1-case
# students=['akmal','jasur','asal','kumush','maftuna','elbek']
# students1=students[2:5]
# students2=students[0:2]

# # 2-case
# students3=students[1:]  # start_index dan boshlab oxirgach kesib oladi
# print(students3)

# # 3-case
# students4=students[:4]  # ro'xat boshidan end_index gacha kesadi
# print(students)

# 0 dan boshlab indekslanadi
# manfiy index (-1, -2, -3, ...)





# Ro'hatdan copy olish
# 1.Shallow(sayoz)copy
# sonlar=[1,2,3,4,5]
# # sonlar2=sonlar
# # sonlar2.append(77)
# # sonlar.insert(2,-8)
# # print(sonlar)
# # print(sonlar2)

# # 2.Deep (chuqur)cpy
# sonlar3=sonlar[:]
# sonlar3.append(8)
# print(sonlar3)
# print(sonlar)

# deep copy using copy library
# import copy
# original_list = [1, 2, [3, 4], 5]
# deep_copy = copy.deepcopy(original_list)

# deep_copy[2].append(99) 
# print(deep_copy)
# print(original_list)

# Tuple - o'zgarmas ro'xat
# toys=('bus','car','bear','dino','snake','lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])
# # toys[-1] ='dragon'
# # print(toys)error
# toys=list(toys)
# toys[1]= 'dragon'
# toys.remove("dino")
# toys.append("mcueen")
# toys=tuple(toys)
# print(toys)




sonlar = list(range(120,1200,2))
# print(sonlar[:20])
# print(sonlar[-20:])
length=len(sonlar)



start_index = length // 2 - 10
end_index = length // 2 + 10
print(sonlar)
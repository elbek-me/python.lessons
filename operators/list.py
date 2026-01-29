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

ismlar=['behruz','ibrohim']
print(f"salom {ismlar[1]} ahvollaring qanday")
print(f"{ismlar[0]} bugun darsga kelasanmi")

sonlar = [22,58,34,67,983,114]
print(sonlar)
sonlar[0] = sonlar[0]+sonlar[-1]
sonlar[1] = 67
sonlar[4] = sonlar[4] + 50
print(sonlar)

a_shaxs=['amir temur','abu rayhon beruniy','alisher navoiy']
b_shaxs = ['Bill Gates', 'Elon Musk', 'Doasnald Trump']

print(f"Men tarixiy shaxslardan {a_shaxs.pop(1)} bilanzamonaviy shaxslardan esa {b_shaxs.pop(0)} bilansuhbat qilishni istar edim")

friends = []
friends.append('hasan')
friends.append('umid')
friends.append('nurmurod')
friends.append('ibrohim')
friends.append('behruz')
print(friends)
friends.remove('hasan')
friends.remove('ibrohim')
print(friends)


mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(-1))
print("Kelgan mehmonlar: ", mehmonlar)


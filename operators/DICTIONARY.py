# # data typs
# # 1.string 2.integer  3.float 4.boolean 5.list 6.tuple  7.dictionary

# # dictionary
# cars = ['audi', 'bmw', 'volvo']
# car = {'brad':"ford",
#        'model':"mustang",
#        'year':1964,
#        'color':"red"}
# print(car)
# print(type(car))


# student = {
#     'fullname': "Elbek",
#     'age': 20,
#     'course': 3,
#     'favorite_books': ["atomic habits", "otkan kunlar", "dunyoning ishlari"],
#     'is_coplete_books': False,
#     'is_married': True
# }
# print(student)


# # 1. QIYMATLARNI OLISH
# print(student['fullname'])
# print(student['age'])   
# print(student['favorite_books']) 

# for book in student['favorite_books']:
#     print(book)

# # 2. qiymatlarni ozgatirish
# student['age'] = 21
# student['course'] = 4
# print(student)

# # 3.yangi key_value qo'shish
# student['hobby'] = ["football", "programming", "traveling", "cooking"]
# print(student)

# # 4. key-value ochirish
# del student['is_married']
# print(student)

# # 5. Empty dictionarys
# talaba_1 = {}

# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 20
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# # 6.get metodi
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }

# print(telefonlar.get('ali')) # iphone x qaytaradi
# print(telefonlar.get('akmal')) # None qaytaradi


ona = {
    'ism': "Zebo",
    'tugilgan_yil': 1991,
    'shahar': "xorazm"
}   
print(f"Onamning ismi {ona['ism']}, {ona['tugilgan_yil']}-yilda, {ona['shahar']} viloyatida tug'ilgan")

taomlar = {
    'ibrohim': "osh",
    'behruz': "manti",
    'elbek': "shashlik",
}
print(f"Ibrohimning sevimli taomi {taomlar['ibrohim']}")
print(f"Behruzning sevimli taomi {taomlar['behruz']}")
print(f"Elbekning sevimli taomi {taomlar['elbek']}")


lugat = {
    'integer': "butun son",
    'float': "o'nlik son",
    'string': "matn",
    'if': "agar",
    'else': "aks holda",
    'list': "ro'yxat",
    'tuple': "o'zgarmas ro'yxat",
    'dictionary': "lug'at",
    'boolean': "mantiqiy qiymat",
    'for': "uchun"
}


soz = input("Tarjimasini bilmoqchi bo'lgan so'zni kiriting: ")
tarjima = lugat.get(soz)
if tarjima:
    print(f"{soz}ning tarjimasi: {tarjima}")
else:
    print("Bunda so'z mavjud emas")
    
# Malumotlar turlari(Data types)
# 1. String(matn)
# 2. Number(son) => 1. Integer(butun son) 5 -5 10 2. Float(kasr son)50.1 2.23 20.33
# 3. Boolean(Mantiqiy qiymat) => 1.True(haqiqat) 2.False(yolgon)
text="lorem ipsum"
age=15
is_student=True
# type
print(type(text))
print(type(-78))
print(type(8.97))
print(type(is_student))
# a=20
# b=-30
# c=a+b
# print(c) #10
pi = 3.1415 # o'nlik son (float)
radius = 10  # butun son (integer)
diametr = 2*radius
yuza=pi*radius**2
print("Aylana uzunligi ", pi*diametr, " ga teng.")
print(yuza)

print(50/10) #5.0s

a = 2
b = 3.0
# Quyidagi arifmetik amallarning natijasi o'nlik son hosil qiladi
print(a+b) 
print(a*b)
print(a**b)
print(2*(a+b))

aholi_soni = 7_594_000_000 # o'zmizga qulay bo'lishi uchun shinday yozdik
print("Yer kurrasida", aholi_soni, " ga yaqin odam yashaydi")

PI=3.1415
G=9.81
print(PI,G)

# x=7
# y=-5
# z=10
# x, y, z =7, -5, 10
# print(x+y-z)


kv_tomon=int(input('kvadrat tomoni kiriting'))
print(kv_tomon ** 2)
# typecasting - bir turdagi ma'lumotni boshqa turga o'qkazish
ism = 'Jobir'
yosh = 36
# jobir 36da
xabar = ism + ' ' + str(yosh) + ' yoshda'
print(xabar)

print(int(5.36)) #5
print(int(5.5))  #5
print(float('8.8710')) # 8.87 => floats
print(float(5))  #5.0

x = int(input("hohlagan son kiriting"))
# xabar1=f"{x} ning kvadrati{x**2}  ga teng"
# xabar2=f"{x} ning kubi {x**3}ga teng"
xabar1= str(x)  + " ning kvadrati " +str(x**2) +  "  ga teng"
xabar2= str(x)  + " ning kubi " +str(x**3) +  "  ga teng"
print(xabar1)
print(xabar2)
yosh = int(input("Yoshingiz nechida?"))
tugilgan_yil = 2025-yosh
print("Siz ", tugilgan_yil, " da tugilgansiz")


a = float(input("birinchi sonni kiriting "))
b = float(input("ikkinchi sonni kiriting "))
print("a+b=",a+b)
print("a-b=",a-b)
print("axb=",a*b)
print("a/b=",a/b)

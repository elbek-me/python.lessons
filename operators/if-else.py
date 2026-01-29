# age = int(input("Yoshingizni kiriting"))
# if age > 18:
#    print("kirish huquqiga egasiz")
# else:
#    print("siz hali yoshsiz")
# ball=50
# if ball < 56:
#    print("siz imtihondan o'ta olmadingiz")

# age = int(input("Yoshingizni kiriting :"))
# if age >= 16:
#    print("Passport olish huquqiga egasiz")
# else:
#  print("Siz hali yoshsiz !")

# son=int(input("son kiriting"))
# if son > 0:
#    print("siz kiritgan son musbat")
# else:
#    print("siz kiritgan son manfiy")

# son1=int(input("1-tomonini kiriting :"))
# if son1 % 2==0:
#    print("siz kiritgan son juft")
# else:
#    print("siz kiritgan son toq")



# a=int(input("1-sonni kiriting :"))
# b=int(input("2-sonni kiriting :"))
# c=int(input("3-sonni kiriting :"))
# if a + b > c and b + c > a and a + c > b                                                                                                                                                                                                                 a + c > b:
#    print("uchburchak yasash mumkun")
# else:
#    print("uchburchak yasash mumkun emas")
# Amaliyot
# 1-mashq
# son1=int(input("1-sonni kiriting :"))
# if son1 % 2==0 and son1 %3 ==0:
#    print("6 ga bolinadi")
# else:
#    print("6 ga bolinmaydi")
# 2-mashq
# a=int(input("Uchburchakning 1-tomonini kiriting :"))
# b=int(input("Uchburchakning 2-tomonini kiriting :"))
# c=int(input("Uchburchakning 3-tomonini kiriting :"))

# if a + b > c and a + c > b and b + c > a:
#    print("uchburchak yasash mumkun")
# else:
#       print("uchburchak yasash mumkun emas")
# a=int(input(" 1-tomonini kiriting :"))
# b=int(input(" 2-tomonini kiriting :"))
# c=int(input(" 3-tomonini kiriting :"))
# 
# if a < b < c:
#     print("YES")
# else:
#     print("NO")
# 36
# a=int(input(" 1-tomonini kiriting :"))
# b=int(input(" 2-tomonini kiriting :"))
# if a > b:
#     print(a)
# else:
#     print(a, b)

# a=int(input(" 1-tomonini kiriting :"))
# b=int(input(" 2-tomonini kiriting :"))
# if a <= b:
#     print(0, b)
#     a = 0
# else:
#     print(a, b)
# import math 
# a=int(input(" 1-tomonini kiriting :"))
# b=int(input(" 2-tomonini kiriting :"))
# c=int(input(" 3-tomonini kiriting :"))
# if a >= b >= c:
#     print(a * 2, b * 2, c * 2)
# else:
#     print(math.fabs(a), math.fabs(b), math.fabs(c))


# x=int(input(" 1-tomonini kiriting :"))
# y=int(input(" 2-tomonini kiriting :"))
# a,b = 4 * x * y, (x + y) / 2
# if x > y:
#     print(f"{a:.1f}", f"{b:.1f}")
# else:
#     print(f"{b:.1f}", f"{a:.1f}")



# ball=int(input("Ballingizni kiriting: "))
# if ball < 56:
#    print("siz imtihondan o'ta olmadingiz")
# elif ball >= 56 and ball < 70 :
#    print("Siz imtihondan 3 baho bilan o'tdingiz")
# elif ball >=70 and ball < 86 :
#    print("Siz imtihondan 4 baho bilan o'tdingiz")
# elif ball >= 86 and ball <= 100 :
#    print("Siz imtihondan 5 baho bilan o'tdingiz")
# else:
#    print("Iltimos, 0 dan 100 gacha ball kiziting !")   
# import math
# x=float(input(" 1-tomonini kiriting :"))
# y=float(input(" 2-tomonini kiriting :"))
# if x < 0 and y < 0:
#     print(math.fabs(x), math.fabs(y))
# elif x > 0 and y > 0:
#     print(x,y)
# else:
#     print(x + 0.5, y + 0.5)


# 12.77, 15.88, -75, 18, 0, 89, 25
# max - eng katta => 85
# min - eng kichik => -75
# print(max(12.77, 15.88, -75, 18, 0, 89, 25))
# print(min(12.77, 15.88, -75, 18, 0, 89, 25,))


# x = float(input(" 1-tomonini kiriting :"))
# y = float(input(" 2-tomonini kiriting :"))
# print(max(x,y),min(x,y))

# x = float(input(" 1-tomonini kiriting :"))
# y = float(input(" 2-tomonini kiriting :"))
# z = float(input(" 3-tomonini kiriting :"))
# print(max(x,y,z),min(x,y,z))


# x = float(input(" 1-sonni kiriting :"))
# y = float(input(" 2-sonni kiriting :"))
# z = float(input(" 3-sonni kiriting :"))
# print(max(x + y + z, x, y, z),min(x + y / 2, x, y, z) ** 2 )

# a = float(input(" 1-sonni kiriting: "))
# b = float(input(" 2-sonni kiriting: "))
# c = float(input(" 3-sonni kiriting: "))
# d = float(input(" 4-sonni kiriting: "))
# max_value = max(a, b, c, d)
# min_value = min(a, b, c, d)
# if a <= b <= c <= d:
#     a = b = c = d = max_value
# else:
#     a = b = c = d = min_value
# print(a, b, c, d)

x = float(input(" 1-sonni kiriting :"))
y = float(input(" 2-sonni kiriting :"))
z = float(input(" 3-sonni kiriting :"))
if x < 1 and y < 1 and z < 1:
    d = min(x,y,z)
    if x == d:
        print((y + z) / 2,y,z)
    elif y == d:
        print( (x + z) / 2,x,z)
    else:
        print((x + y) / 2,x,y)
else:
    print(x,y,z)
# 0.43 1.11 0.75  0.62 0.58 0.8








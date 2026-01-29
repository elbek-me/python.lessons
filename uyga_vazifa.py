
# a=1
# b=5
# c=6
# d= (b ** 2) - 4 * a * c
# x1=((-b)-(d ** 0.5)) / (2 *a)
# x2=((-b)+(d ** 0.5)) / (2 *a)
# print(x1, x2)
# a=1
# b=7
# c=10
# d= (b ** 2) - 4 * a * c
# print(d)
# x1=((-b)-(d ** 0.5)) / (2 *a)
# x2=((-b)+(d ** 0.5)) / (2 *a)
# print(x1,x2)

# a = int(input("1 :"))
# x = float(input("2 :"))
# q1 = x * math.sin(x/2 + x/3 + x/4)
# q2 = (math.log10(x*x - 2) +math.pow(3, a)) / (math.cos(x + 3) * math.sin(x + 3) + 8)
# bb1 = q1 + q2
# print(f"{bb1:.2f}")


# a = int(input("1 :"))
# x = float(input("2 :"))
# y = float(input("3 :"))
# b = math.sqrt( math.exp(x * y)  - x * math.sin(a * x)  - (x*x + 2) / (abs(x) + 5))
# c = math.sqrt(math.log(x*x + 2) + 5)
# w2 = b + c
# print(f"{w2:.2f}")


# import math
# x = float(input("sonni kiriting: "))
# a=2**math.tan(x+2)-math.cos(x+math.pow(2,x))
# b=1+math.pow(math.cos(x+2),2)
# c=math.sin(math.pow(x,2))
# d=math.pow(x,2)+3
# aa=math.sqrt(a/b)+c/d
# print(aa)

# import math

# a = int(input("1 -son: "))
# x = float(input("2 -son: "))
# y = float(input("3 -son:  "))
# q1 = y*y + math.exp(x)
# q2 = math.exp(x) + a/(x*x + 2) + (math.cos(x)**2) / math.sin(x*x)
# q3 = math.cos(x)**3
# TT = math.sqrt(q1 + math.sqrt(q2) + q3)
# print(f"{TT:.2f}")



# # 20
import math
x = float(input("1-sonni kiriting: "))
y = float(input("2-sonni kiriting: "))
c = (x ** 2 + 1)
a = c / (x ** 2 + (x * y + y ** 2) / ((y ** 2) + (y + x * y) / (math.fabs(x * y) + 5)))
b = 1 / (1 + math.cos(x) + 1 / math.sin(math.fabs(x)))
javob = a + b
print(f'{javob:.2f}')  
# # 7.09 3.92	4.09 8.67



# # 22
import math 
x = int(input("1-sonni kiriting: "))
y = float(input("2-sonni kiriting: "))
z = float(input("3-sonni kiriting: "))
javob = 2 ** (-x) *math.sqrt(x + math.pow(math.fabs (y) + 2, 1 / 4)) *math.pow((math.pow(math.e, x - 1)) / math.sin(z + 2) + 2, 1 / 3)
print(f'{javob:.2f}')
# # #  1 1.84 0.53  2 1.18 1.03 

# 30
import math
x1 = float(input("1-sonni kiriting: "))
x2 = float(input("2-sonni kiriting: "))
c  = float(input("3-sonni kiriting: "))
d  = float(input("4-sonni kiriting: "))
a = abs(math.sin(abs(c * x2 ** 3 + d * x1 ** 3 - c * d)) ** 2 / math.pow(c * x1 ** 2 + d * x2 ** 2 + 7, 1 / 2))
b = math.tan(x1 * x2 ** 2 + d ** 3)
javob = a + b
print(f'{javob:.2f}')  
#  4.01 0.33 0 1  7.99 0.72 2 3	

	
x = int(input("1-sonini kiritig: "))
y = int(input("2-sonini kiritig: "))
if x < y:
    birinchi_x = (x + y) / 2
    ikkinch_y = 2 * x * y
    x, y = birinchi_x, ikkinch_y
    print(int(x),int(y))
elif y < x:
    ikkinch_y = (x + y) / 2
    birinchi_x = 2 * x * y
    x, y = birinchi_x,ikkinch_y
    print(int(x),int(y))
else:
    print(int(x),int(y))
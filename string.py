# String - matn
# Data types(M'alumot turlari) :1. string(matn) 2.number(son) 3.Boolem(Mantiqiy)
region='Xorazm'
city='Shovot'
street='AL-Xorazimiy'
emoji='✅'
fristname='elbek'
lastname='atajanov'
# Matinlarni qoshish
print(region,city,street,emoji,)
address= 'Men ' +  region + ' viloyati ' +  city + ' tumadi ' + street + ' kochasida yashayman '
print(address)
text='Mening ismim ' + fristname
full_name='Mening toliq ism familyam ' + fristname + " "  + lastname
print(full_name)
print(text)


# f-string
name=f"Mening to'liq ism familyam {fristname} {lastname}"
full_address=f"Men {region} viloyati {city} tumanida yashayman"
print(name)
print(full_address)
print('Hello World!')
print('Hello \tWorld!')
print('Hello \nWorld!')

viloyat="xorazm"
tuman = "shovot"
mahalla = "oq kol"
kocha = "zar bulq"
print( viloyat + " viloyati "  +  tuman + " tumani " +   mahalla + " mahallasi "   +  kocha + " ko'chasi "    )

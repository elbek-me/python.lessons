while True:
    yosh = int(input("Yoshingiz nechada : "))
    if yosh <= 7:
        narh = 2000
    elif yosh <= 18:
        narh = 3000
    elif yosh <= 65:
        narh = 10000
    else:
        narh = 0
    if narh == 0:
        print("Sizga bepul ekan")
    else:
        print(f"Sizga chipta narhi {narh} so'm") 
    javob = input("Yana urinib ko'rasizmi: stop/quit/exit : ")
    if javob == "stop" or javob == "quit" or javob == "exit":
        print("Dastur to'xtadi")
        break


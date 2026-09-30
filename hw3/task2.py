year = int(input("Рік: "))
month = int(input("Місяць: "))
day = int(input("День: "))

if not 0 < month <= 12 or not 0 < day <= 31: 
    print("Таких дат не існує")

else: print(f"{day:02d}.{month:02d}.{year % 100:02d}")


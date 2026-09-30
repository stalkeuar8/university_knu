hours = int(input("Години: "))
minutes = int(input("Хвилини: "))

if not 0 <= hours <= 24 or not 0 <= minutes < 60:
    print("Неправильний ввід цифр, таких хвилин та годин не існує")
    
else:
    print(f"{hours:02d}:{minutes:02d}")
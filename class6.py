def f_safety(x, y):
    try:
        return x / (y - 1) ** 19

    except ZeroDivisionError:
        return None

    except OverflowError:
        return 0

def enter_x():
    x = float(input("Введіть дійсне значення х (додатнє): "))

    if x <= 0:
        raise ValueError

    return x

def enter_y():
    y = float(input("Введіть дійсне значення y (додатнє, більше за 1): "))

    if y <= 0 or y == 1:
        raise ValueError

    return y

try:
    x = enter_x()
    y = enter_y()

    a = f_safety(x, y)

    print(f"Результат: {a}")

except ValueError:
    print(f"Ввели некоректні значення")

except Exception as e:
    print(e)

except BaseException:
    print("\nКлавіатура")
    
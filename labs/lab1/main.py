
import math

def _check_x_value(x: float) -> bool:
    """
    Receives a float value 'x',
    Сhecks whether 'x' is within the expression's domain.
    It returns True if the value is valid, and False if the value is invalid.
    """

    is_acceptable = (9 <= x <= 11 and x != 10)
    return is_acceptable


def f(x: float) -> float:
    """
    Takes a float value 'x' as an argument, 
    evaluates the expression using that value of 'x'.
    It returns the result of evaluating the expression as a float.
    """
    
    result = (
        math.sin(math.pi / 62) ** 2
        + 25 * math.e / (52 * math.pi)
        - 12 / ((x - 10) * (x + 8))
        + 3 * math.acos(x - 10)
        - (14 + math.sqrt(x + 15)) / (x - 5)
    )
    return result


def main():
    """
    The main program's function, 
    it prints an information about program and its author, reads a number, 
    checks it, and displays the result of the calculation.
    """
    print("Author: Marchenko Artem")
    print("Variant 131. Calculating the value of a mathematical expression.")

    try:
        x = float(input("Enter x value (from 9 to 11, but not 10): "))
        
    except (ValueError, EOFError):
        print("\nwrong input")

    else:
        print("\n***** do calculations ... ", end="")

        if _check_x_value(x):
            result = f(x)

        else:
            result = None

        print("done")
        print(f"for x = {x:.5f}")

        if result is None:
            print("result = undefined")

        else:
            print(f"result = {result:.7f}")

main()
"""Lab 2, variant 131."""

A = 0
B = 1


def _welcome():
    """Shows the author and variant."""
    print("Author: Artem Marchenko, K-13")
    print("Variant 131. Calculates the sum of the series for x.")


def s(x, eps):
    """Calculates the sum of series S."""
    a_n = 1.0
    total = a_n
    n = 0

    while a_n >= eps or a_n <= -eps:
        n += 1
        a_n = (-a_n) * x / (n * (n + 1))
        total += a_n

    return total


def _read_x():
    """Reads x and checks whether x is acceptable."""
    try:
        x = float(input(f"Enter x from [{A}, {B}]: "))
        if not A <= x <= B:
            print(f"\n***** error\nx must be in [{A}, {B}].")
            return None

        return x
    except ValueError:
        print("\n***** error\nEnter a real number for x.")
    except EOFError:
        print("\n***** error\nInput ended before x was entered.")

    return None


def _read_eps():
    """Reads eps and checks whether eps is acceptable."""
    try:
        eps = float(input("Enter positive eps (for example, 1e-6): "))
        if not 0 < eps < float("inf"):
            print("\n***** error\neps must be a finite positive number.")
            return None

        return eps
    except ValueError:
        print("\n***** error\nEnter a real number for eps.")
    except EOFError:
        print("\n***** error\nInput ended before eps was entered.")

    return None


def main():
    """Runs the program and prints the result."""
    try:
        _welcome()
        x = _read_x()
        if x is None:
            return

        eps = _read_eps()
        if eps is None:
            return

        print("\n***** do calculations ...", end=" ")
        result = s(x, eps)
        print("done")
        print(f"for x = {x:.7E}")
        print(f"for eps = {eps:.8E}")
        print(f"result = {result:.8f}")

    except Exception:
        print("\n***** error\nunexpected error occurred")
    except KeyboardInterrupt:
        print("\nprogram aborted")
    except BaseException:
        print("\n***** error\nthe program stopped unexpectedly")


main()
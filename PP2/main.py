"""Lab 2, variant 131."""

A = 0
B = 1


def s(x, eps):
    """Calculates the sum of series S."""
    a_n = 1.0
    total = a_n
    n = 0

    while a_n >= eps or a_n <= -eps:
        n += 1
        a_n *= -x / (n * (n + 1))
        total += a_n

    return total


def _welcome():
    """Prints the information about author, variant and program."""
    print("Author: Artem Marchenko, K-13")
    print("Variant 131. Calculates the sum of the series for x.")


def _print_error(error_reason):
    """Prints the error message with its reason."""
    print(f"\n***** error\n{error_reason}")


def _read_x():
    """Reads x and checks whether x is acceptable."""
    try:
        x = float(input(f"Enter x from [{A}, {B}]: "))
        if not A <= x <= B:
            _print_error(f"x must be in [{A}, {B}].")
            return None

        return x
    except ValueError:
        _print_error("x must be a real number.")
    except EOFError:
        _print_error("Input ended before x was entered.")

    return None


def _read_eps():
    """Reads eps and checks whether eps is acceptable."""
    try:
        eps = float(input("Enter positive eps (for example, 1e-6): "))
        if not 0 < eps < float("inf"):
            _print_error("eps must be a finite positive number.")
            return None

        return eps
    except ValueError:
        _print_error("eps must be a real number.")
    except EOFError:
        _print_error("Input ended before eps was entered.")

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

    except Exception as error:
        _print_error(f"Unexpected error: {error}")
    except KeyboardInterrupt:
        print("\nprogram aborted")


main()
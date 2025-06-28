from sympy import symbols, Eq, solve
from fractions import Fraction
import math

def solve_proportion(a, b, c):
    x = symbols('x')
    proportion = Eq(a / b, x / c)
    solution = solve(proportion, x)
    return solution[0]

def solve_equation():
    x = symbols('x')
    equation = input("Enter the equation (e.g., 2*x + 3 = 7): ")
    left, right = equation.split('=')
    eq = Eq(eval(left), eval(right))
    solution = solve(eq, x)
    return solution

def factor_square_root():
    num = float(input("Enter a number to find its square root: "))
    return math.sqrt(num)

def decimal_to_fraction_percent():
    decimal = float(input("Enter a decimal number: "))
    fraction = Fraction(decimal).limit_denominator()
    percent = decimal * 100
    return fraction, f"{percent}%"

def fraction_to_decimal_percent():
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    decimal = numerator / denominator
    percent = decimal * 100
    return decimal, f"{percent}%"

def percent_to_decimal_fraction():
    percent = float(input("Enter percent (without % sign): "))
    decimal = percent / 100
    fraction = Fraction(decimal).limit_denominator()
    return decimal, fraction

# ----------- MENU -------------
def main():
    while True:
        print("\n=== Multi-Function Calculator ===")
        print("1. Solve Proportion (a/b = x/c)")
        print("2. Solve for x in equation")
        print("3. Square root")
        print("4. Decimal → Fraction & Percent")
        print("5. Fraction → Decimal & Percent")
        print("6. Percent → Decimal & Fraction")
        print("7. Exit")

        choice = input("Enter your choice (1–7): ")

        if choice == '1':
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
            c = float(input("Enter c: "))
            print("x =", solve_proportion(a, b, c))

        elif choice == '2':
            print("x =", solve_equation())

        elif choice == '3':
            print("Square root =", factor_square_root())

        elif choice == '4':
            fraction, percent = decimal_to_fraction_percent()
            print("Fraction:", fraction, "Percent:", percent)

        elif choice == '5':
            decimal, percent = fraction_to_decimal_percent()
            print("Decimal:", decimal, "Percent:", percent)

        elif choice == '6':
            decimal, fraction = percent_to_decimal_fraction()
            print("Decimal:", decimal, "Fraction:", fraction)

        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()



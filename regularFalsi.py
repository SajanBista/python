import math

def f(x):
    return 3*x**2 - 6*x + 2

def regula_falsi(x0, x1, tol):
    f0 = f(x0)
    f1 = f(x1)

    if f0 * f1 > 0:
        print("Initial guesses do not bracket the root.")
        return None

    while True:
        x2 = x0 - (f0 * (x1 - x0)) / (f1 - f0)
        f2 = f(x2)

        print(f"x0 = {x0:.6f}, x1 = {x1:.6f}, x2 = {x2:.6f}, f(x2) = {f2:.6f}")

        if abs(x2 - x0) < tol or abs(x2 - x1) < tol:
            return x2

        if f0 * f2 < 0:
            x1 = x2
            f1 = f2
        else:
            x0 = x2
            f0 = f2

def main():
    x0 = float(input("Enter initial guess x0: "))
    x1 = float(input("Enter initial guess x1: "))
    tol = float(input("Enter tolerable error: "))

    root = regula_falsi(x0, x1, tol)

    if root is not None:
        print(f"Root is: {root:.6f}")
    else:
        print("Root not found.")

if __name__ == "__main__":
    main()
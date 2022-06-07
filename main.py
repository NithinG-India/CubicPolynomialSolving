from sys import exit

print("Please include the signs of the corresponding coefficients:")

A = input("Enter the coefficient of x^3:")
A = int(A) or float(A)
try:
    1 / A != 0
except ZeroDivisionError:
    print("A is 0 , This is not a cubic polynomial")
    exit()
else:
    pass
B = input("Enter the coefficient of x^2:")
C = input("Enter the coefficient of x:")
D = input("Enter the coefficient of x^0 (constant):")

B = int(B) or float(B)
C = int(C) or float(C)
D = int(D) or float(D)

if D == 0:
    y = 0
    z = -B / A - y
    valuesfinal = z ** 2 - 4 * (C / A)
    valuesultrafinal = valuesfinal ** (1 / 2)
    values1 = (z + valuesultrafinal) / 2
    x = values1
    n = values1.real
    p = round(n)
    values3 = -B / A - y - x
    d = values3
    l = values3.real
    r = round(l)
    none = input("Do you want the roots in terms of complex numbers?")
    quese = input("Do you want the roots in terms of real numbers(not rounded off)?")
    if none == "YES" or "Yes" or "yes":
        print("The First Root of your cubic polynomial is :", y)
        print("The Second Root of your cubic polynomial is :", x)
        print("The Third Root of your cubic polynomial is :", d)
    elif quese == "YES" or "Yes" or "yes":
        print("The First Root of your cubic polynomial is :", l)
        print("The Second Root of your cubic polynomial is :", n)
        print("The Third Root of your cubic polynomial is :", y)
    else:
        print("The First Root of your cubic polynomial is :", p)
        print("The Second Root of your cubic polynomial is :", y)
        print("The Third Root of your cubic polynomial is :", r)
else:
    values2 = ((((((-B ** 3) / (27 * (A ** 3)) + (B * C) / (6 * (A ** 2)) - D / (2 * A)) + (
            (((-B ** 3) / (27 * (A ** 3)) + (B * C) / (6 * (A ** 2)) - D / (2 * A)) ** 2) + (
            C / (3 * A) - (B ** 2) / (9 * (A ** 2))) ** 3) ** (1 / 2)) ** (1 / 3))) + ((
            (((-B ** 3) / (27 * (A ** 3)) + (B * C) / (6 * (A ** 2)) - D / (2 * A)) - (
                    (((-B ** 3) / (27 * (A ** 3)) + (B * C) / (6 * (A ** 2)) - D / (2 * A)) ** 2) + (
                    C / (3 * A) - (B ** 2) / (9 * (A ** 2))) ** 3) ** (1 / 2)) ** (1 / 3))) - B / (3 * A))
    v = values2
    t = values2.real
    y = round(t)
    z = -B / A - v
    valuesfinal = z ** 2 - 4 * (-D / (A * v))
    valuesultrafinal = valuesfinal ** (1 / 2)
    values1 = (z + valuesultrafinal) / 2
    x = values1
    n = values1.real
    p = round(n)
    values3 = -B / A - v - x
    d = values3
    l = values3.real
    r = round(l)
    none = input("Do you want the roots in terms of complex numbers?")
    quese = input("Do you want the roots in terms of real numbers(not rounded off)?")
    if none == "YES" or "Yes" or "yes":
        print("The First Root of your cubic polynomial is :", v)
        print("The Second Root of your cubic polynomial is :", x)
        print("The Third Root of your cubic polynomial is :", d)
    elif quese == "YES" or "Yes" or "yes":
        print("The First Root of your cubic polynomial is :", l)
        print("The Second Root of your cubic polynomial is :", n)
        print("The Third Root of your cubic polynomial is :", t)
    else:
        print("The First Root of your cubic polynomial is :", p)
        print("The Second Root of your cubic polynomial is :", y)
        print("The Third Root of your cubic polynomial is :", r)

import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Please enter a number")
    sys.exit(1)
try:
    print(f"{x} / {y} = {x / y}")

except ZeroDivisionError:
    print("Cannot divide by zero")
    sys.exit(1)

"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# when the input is not a number, for example a, b, c ...
# whenthe input for denominator is zero, ZeroDivisionError will occor
numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))
fraction = numerator / denominator
while True:
    if denominator == 0:
        print("Cannot be zero!Enter the denominator again: ")
    else:
        break
print(fraction)
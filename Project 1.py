# Name: Ozcan Celik
# Course ID and Section: W26 COP2002.0T1: PROGRAM LOGIC
# Date Created: March 24, 2026
# Program Title: Number Conversion Program
# Program Description: This program provides a menu for the user to convert between hexadecimal, binary, and decimal number systems.

print("Number Conversion Menu")
print("1. Hexadecimal to Binary")
print("2. Binary to Hexadecimal")
print("3. Decimal to Binary")
print("4. Binary to Decimal")
print("5. Exit")
print()
choice = input("Choose an option (1-5): ")

while choice != "5":

    while choice not in ["1", "2", "3", "4", "5"]:
        choice = input("Invalid choice. Choose an option (1-5): ")

    if choice == "1":
        print()
        hex_value = input("Enter a hexadecimal value: ")
        binary_result = ""

        for digit in hex_value.upper():
            if digit == "0":
                nibble = "0000"
            elif digit == "1":
                nibble = "0001"
            elif digit == "2":
                nibble = "0010"
            elif digit == "3":
                nibble = "0011"
            elif digit == "4":
                nibble = "0100"
            elif digit == "5":
                nibble = "0101"
            elif digit == "6":
                nibble = "0110"
            elif digit == "7":
                nibble = "0111"
            elif digit == "8":
                nibble = "1000"
            elif digit == "9":
                nibble = "1001"
            elif digit == "A":
                nibble = "1010"
            elif digit == "B":
                nibble = "1011"
            elif digit == "C":
                nibble = "1100"
            elif digit == "D":
                nibble = "1101"
            elif digit == "E":
                nibble = "1110"
            elif digit == "F":
                nibble = "1111"

            binary_result = binary_result + nibble + " "

        print("Binary:", binary_result.strip())

    elif choice == "2":
        print()
        binary_value = input("Enter a binary value: ")

        remainder = len(binary_value) % 4
        if remainder != 0:
            binary_value = "0" * (4 - remainder) + binary_value

        hex_result = ""
        index = 0

        while index < len(binary_value):
            nibble = binary_value[index:index + 4]

            if nibble == "0000":
                hex_digit = "0"
            elif nibble == "0001":
                hex_digit = "1"
            elif nibble == "0010":
                hex_digit = "2"
            elif nibble == "0011":
                hex_digit = "3"
            elif nibble == "0100":
                hex_digit = "4"
            elif nibble == "0101":
                hex_digit = "5"
            elif nibble == "0110":
                hex_digit = "6"
            elif nibble == "0111":
                hex_digit = "7"
            elif nibble == "1000":
                hex_digit = "8"
            elif nibble == "1001":
                hex_digit = "9"
            elif nibble == "1010":
                hex_digit = "A"
            elif nibble == "1011":
                hex_digit = "B"
            elif nibble == "1100":
                hex_digit = "C"
            elif nibble == "1101":
                hex_digit = "D"
            elif nibble == "1110":
                hex_digit = "E"
            elif nibble == "1111":
                hex_digit = "F"

            hex_result = hex_result + hex_digit
            index = index + 4

        print("Hexadecimal:", hex_result)

    elif choice == "3":
        print()
        decimal_value = int(input("Enter a decimal value: "))
        binary_result = ""

        if decimal_value == 0:
            binary_result = "0"
        else:
            remaining = decimal_value
            while remaining > 0:
                binary_result = str(remaining % 2) + binary_result
                remaining = remaining // 2

        print("Binary:", binary_result)

    elif choice == "4":
        print()
        binary_value = input("Enter a binary value: ")
        decimal_result = 0
        power = 0
        index = len(binary_value) - 1

        while index >= 0:
            decimal_result = decimal_result + int(binary_value[index]) * (2 ** power)
            power = power + 1
            index = index - 1

        print("Decimal:", decimal_result)

    print()
    print("Number Conversion Menu")
    print("1. Hexadecimal to Binary")
    print("2. Binary to Hexadecimal")
    print("3. Decimal to Binary")
    print("4. Binary to Decimal")
    print("5. Exit")
    print()
    choice = input("Choose an option (1-5): ")

print()
print("Exiting program.")

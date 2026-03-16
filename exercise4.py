"""
Name: Ozcan Celik
Student ID: 62050329
Course: COP2002 (Programming Logic)
Date Created: 2026-02-14
Program Title: 2025 Simple IRS Calculator
Program Description:
This program asks the user for their yearly income and calculates a simplified tax amount
using a flat tax rate based on the 2025 IRS Single filing brackets. If the user enters a
negative number, the program prints an error message. The program runs once (no reprompt).
"""

def main():
    print("2025 Simple IRS Calculator")
    print("--------------------------")
    print()

    income = float(input("Enter your yearly income: "))

    if income < 0:
        print("Annual income must be a positive number.")
        return

    # 2025 Single tax brackets (flat rate by bracket, simplified for this exercise)
    # Upper limits for each bracket:
    # 10%: 0 - 11,925
    # 12%: 11,926 - 48,475
    # 22%: 48,476 - 103,350
    # 24%: 103,351 - 197,300
    # 32%: 197,301 - 250,525
    # 35%: 250,526 - 626,350
    # 37%: 626,351 and up

    bracket_tops = [11925, 48475, 103350, 197300, 250525, 626350]
    tax_rates =    [0.10,  0.12,  0.22,   0.24,   0.32,   0.35,   0.37]

    # Find the correct bracket using a loop (arrays only; no dictionaries)
    rate = tax_rates[-1]  # default to top rate if above all bracket_tops
    index = 0
    while index < len(bracket_tops):
        if income <= bracket_tops[index]:
            rate = tax_rates[index]
            break
        index += 1

    taxes = income * rate
    rate_percent = int(rate * 100)

    print()
    print(f"Annual Income: ${income:,.2f}")
    print(f"Tax Rate: {rate_percent}%")
    print(f"You Pay: ${taxes:,.2f}")


if __name__ == "__main__":
    main()
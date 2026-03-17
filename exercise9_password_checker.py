# Exercise 9 - Password Strength Checker
# COP2002 - Python Programming
# Ozcan Celik

import re

def check_length(password):
    return len(password) >= 8

def has_uppercase(password):
    return bool(re.search(r'[A-Z]', password))

def has_lowercase(password):
    return bool(re.search(r'[a-z]', password))

def has_digit(password):
    return bool(re.search(r'\d', password))

def has_special(password):
    return bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

def evaluate_password(password):
    """Evaluate password and return score and feedback."""
    checks = {
        "At least 8 characters"       : check_length(password),
        "Contains uppercase letter"   : has_uppercase(password),
        "Contains lowercase letter"   : has_lowercase(password),
        "Contains a digit"            : has_digit(password),
        "Contains special character"  : has_special(password),
    }

    score = sum(checks.values())

    if score == 5:
        strength = "STRONG"
    elif score >= 3:
        strength = "MEDIUM"
    else:
        strength = "WEAK"

    return checks, score, strength

def display_result(password, checks, score, strength):
    print("\n" + "=" * 40)
    print(f"  PASSWORD: {'*' * len(password)}")
    print(f"  STRENGTH: {strength} ({score}/5)")
    print("=" * 40)
    for criterion, passed in checks.items():
        status = "✓" if passed else "✗"
        print(f"  {status} {criterion}")
    print("=" * 40)

if __name__ == "__main__":
    print("=== PASSWORD STRENGTH CHECKER ===\n")
    while True:
        password = input("Enter a password to check (or 'quit' to exit): ")
        if password.lower() == "quit":
            break
        checks, score, strength = evaluate_password(password)
        display_result(password, checks, score, strength)
        print()

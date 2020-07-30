"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    print("\t1 or more special characters")
    password = input("Please enter a valid password: ")

    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False
    if 2<=len(password)<=6:
        count_lower = 0
        count_upper = 0
        count_digit = 0
        count_special = 0
        for char in password:
            # TODO: count each kind of character (use str methods like isdigit)
            if char.isdigit():
                count_digit+=1
            if char.islower():
                count_lower+=1
            if char.isupper():
                count_upper+=1

    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero
            if char in SPECIAL_CHARACTERS:
                count_special+=1
    # TODO: if any of the 'normal' counts are zero, return False
    if (count_digit>=1 and count_lower>=1 and count_upper>=1 and count_special>=1):
        print("Valid password.")
        print("Your {}-character password is valid: {}".format(len(password),
                                                               password))
    else:
        print("Invalid password.")
    # if we get here (without returning False), then the password must be valid

main()
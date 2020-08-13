
def main():
    email_to_name = {}
    email = input("Please enter your email: ")
    while email != "":
        name = get_name(email)
        check = input("Is your name {}? (Y/n) ".format(name))
        if check.upper() != "Y" and check != "":
            name = input("Please enter your name: ")
        email_to_name[email] = name
        email = input("Please enter your email: ")

    for k,v in email_to_name.items():
        print("{} ({})".format(v, k))


def get_name(email):
    seperate_emails = email.split('@')[0]
    parts = seperate_emails.split('.')
    name = " ".join(parts).title()
    return name


main()
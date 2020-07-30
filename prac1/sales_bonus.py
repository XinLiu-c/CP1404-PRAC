""" Program to calculate and dispaly a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%."""

def main():
    sales = float(input("Enter sales: $")) # get sales
    bonus1 = sales*0.1
    bonus2 = sales*0.15
    if sales < 1000: # conditions for different amount of bonus
        print("Your bonus is $",bonus1)
    else:
        print("Your bonus is $",bonus2)
main()
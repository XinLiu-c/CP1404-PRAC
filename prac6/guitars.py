
from prac6.guitar import Guitar

def main():
    guitar=[]

    print("My Guitars!")
    while True:
        print("Choose one from the menue:\nA) add guitar\nQ) quit ")
        choice=input("Please choose: ").upper()
        count=1
        if choice == "A":
            while True:
                name = input("Please enter your name: ")
                if name=="":
                    print("Invalid name.")
                else:
                    break

            while True:
                year = input("Please enter the year: ")
                if year.isdigit():
                    year=int(year)
                    break

            while True:
                cost = input("Please enter the cost: ")
                if cost.isdigit():
                    cost=int(cost)
                    break
            # guitar_add=Guitar(name,year,cost)
            guitar.append(Guitar(name,year,cost))
            print("{} ({}): ${} added.".format(name,year,cost))
        elif choice == "Q":
            print("These are my guitars: ")
            for i,guitars in enumerate(guitar,1):
                if guitars.is_vintage():
                    vintage_string='(vintage)'
                else:
                    vintage_string=''
                print("Guitar {}: {} {}".format(i,guitars,vintage_string))
            break
main()
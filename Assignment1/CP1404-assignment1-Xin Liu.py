"""
Replace the contents of this module docstring with your own details
Name: LIU XIN
Date started: 08.12
GitHub URL:
"""

# function that displaying the places from reading a csv file
def get_places():
    list_data = [] # empty list
    filename = "places.csv"
    input_file = open(filename, 'r')
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        list_data.append(parts)
    input_file.close()
    list_data.sort(key=itemgetter(3)) # sort data according to "n" and "v"
    list_data.sort(key=itemgetter(2), reverse=True) # sort data according to the priority number
    count = 1
    for list in list_data:
        if list[3] == "n":
            print("*{}. {:9} in {:12} priority {:2}".format(count, list[0], list[1], list[2]))
            count += 1
        else:
            print(" {}. {:9} in {:12} priority {:2}".format(count, list[0], list[1], list[2]))
            count += 1

    return list_data

from operator import itemgetter
def main():

    print("Travel Tracker 1.0 - by Xin Liu")
    print("3 places loaded from places.csv")
    while True:
        print("Menu:\nL - List places\nA - Add new place\nM - Mark a place as visited\nQ - Quit")
        choice = input("Please choose from the menu: ").upper()
        # conditions for different choices that given by the user
        if choice == "L":
            get_places() # call
            print("3 places. You still want to visit 2 places.")
        elif choice == "A":
            name,country,priority=add_place() # call
            list_data=get_places()
            path = "places.csv"
            with open(path,'a+')as f: # add data to a csv file
                csv_write=csv.writer(f)
                added_data=[]
                added_data.append([name, country, priority, "n"])
            print(list_data)
            print("{} in {} (priority {}) added to Travel Tracker.".format(name, country, priority))
        elif choice == "M":
            list_data = get_places()
            print(list_data)
            count_n=0
            for i in list_data:
                if i[3]=="n":
                    count_n+=1
            print(count_n)
            if count_n==0:
                print("No unvisited places")
                continue
            number=int(input("Enter the number of a place to mark as visited: "))
            if number>len(list_data):
                print("Invalid place number")
            elif count_n < number <=len(list_data):
                print("That place is already visited")
            elif number<=0:
                print("number must be > 0")
            else:
                list_data[number-1][3]="v"
                print("{} in {} visited!".format(list_data[number-1][0],list_data[number-1][1]) )
        elif choice == "Q":
            print("4 places saved to places.csv")
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice.")


# functions that adding a new place into the csv file
def add_place():
    while True: # while loop - validation for name
        name = input("Name: ")
        if name == "":
            print("Input cannot be blank.")
        else:
            break
    while True: # while loop - validation for country
        country = input("Country: ")
        if country == "":
            print("Input cannot be blank.")
        else:
            break
    while True: # while loop - validation for priority
        priority = input("Priority: ")
        if priority.isdigit():
            if int(priority) <= 0:
                print("Number must be >0 ")
            else:
                break
        else:
            print("Invalid input, enter a valid number.")

    return name,country,priority


if __name__ == '__main__':
    main()
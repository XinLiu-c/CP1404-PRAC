def main():
    while True: # while loop to validate the right number of items
        number=int(input("Enter the number of items: "))
        if number<=0: # conditions for number of items
            print("Invalid number of items!")
        else:
            break # break while loop
    print("Number of items: ", number)

    total = 0
    for a in range(number): #get prices for each item
        price = int(input("Enter the price of the item: "))
        print("Price of item: $", price)
        total += price
    if total > 100: #conditions for total price
        dis_price = total * 0.9
        print("Total price for {} items is ${} .".format(number, dis_price))
    else:
        print("Total price for {} items is ${} .".format(number, total))
main()



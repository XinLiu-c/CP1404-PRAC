def main():
    name="Gibson L-5 CES"
    year=1922
    cost=16035
    print("{} {} for about ${}!".format(year,name,cost))

    numbers = [0, 50, 100, 150]
    for i,number in enumerate(numbers):
        print("{0:>5}".format(number))
main()
from prac8.unreliable_car import UnreliableCar

def main():
    g_car = UnreliableCar("Good", 100, 90)
    b_car = UnreliableCar("Bad", 100, 9)

    for i in range (1,5):
        print("Attempting to drive {}km : ".format(i))
        print("{:12} drove {:.2f}km".format(g_car.name,g_car.drive(i)))
        print("{:12} drove {:.2f}km".format(b_car.name, b_car.drive(i)))

    print(g_car)
    print(b_car)
main()
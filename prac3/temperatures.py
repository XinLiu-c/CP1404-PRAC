
def main(): # main fuction
    celsius=float(input("Please enter temperature in celsius: "))
    fahrenheit=celsius_to_fahrenheit(celsius) # call
    print("Tempreture in fahrenheit is ", fahrenheit)


def celsius_to_fahrenheit(celsius): # convert function
    return celsius*1.8+32.0

main()


def main():
    numbers=[3,1,4,1,5,9,2]
    print(numbers[0]) # 3
    print(numbers[-1]) # 2
    print(numbers[3]) # 1
    print(numbers[:-1]) # [3, 1, 4, 1, 5, 9]
    print(numbers[3:4]) # [1]
    print(numbers+[6,5,3]) # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print(5 in numbers) # True
    print(7 in numbers) # False
    print("3" in numbers) # False

    number=["ten",1,4,1,5,9,1]
    print(number[2:]) # Get all the elements from numbers except the first two (slice)
    print(9 in number) # True

main()
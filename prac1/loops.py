"""count down from 1 to 20"""
for i in range(1,21,2):
    print(i,end=" ")
print()



"""count in 10s from 0 to 100"""
for i in range (0,11):
    tens = i*10
    print(tens,end=" ")
print()



"""count down from 20 to 1"""
for i in range(20,0,-1):
    print(i,end=" ")
print()



"""print n stars"""
num=int(input("Enter number of stars: "))
for i in range(num):
    j = "*"
    print(j,end="")


"""print n lines of increasing star"""
num=int(input("Enter number: "))
for i in range(1,num+1):
    print("*"*i)

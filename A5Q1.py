#Write a Python class to implement pow(x,n):

class Power:
    def num():
        x=int(input("Enter the number for which nth power to find:"))
        n=int(input("Enter the power of number:"))
        power=1
        for i in range(1, n+1):
            power=power*x
        print("The nth power of the number is", power)

result=Power
result.num()
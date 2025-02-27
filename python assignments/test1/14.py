def get_input():
    n=int(input("enter number"))
    return n
def facto(n):
    fact=1
    if n<0:
        print(f"it is an error and factorials doesnot have negative numbers")
    for i in range (1,n+1):
        fact = fact*i
    print(f"the factorial of {n} is {fact}")
def main():
    n=get_input()
    facto(n)
    
main()
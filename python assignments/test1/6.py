def prime(n):
    if n <= 1:
        return False
    if n==2:
        print(f"{n} is least prime number")
        return True
    for i in range (2,n):
            if n%i==0:
                return False
            return True
def get_input():
    n=int(input("enter number:"))
    return n
def main():
    n=get_input()
    print(f"the number between 1 and {n}")
    for i in range(1,n+1):
        if prime(i):
            print(i, end="  ")
            

main()
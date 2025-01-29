def primes(n):
    if n <= 1:
        return False
    if n==2:
        print(f"{n} is the least number")
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

def get_input():
    n = int(input("Enter a number: "))
    return n

def main():
    n = get_input()
    print(f"Prime numbers from 1 to {n}:")
    for i in range(1, n + 1):
        if primes(i):
            print(i, end=" ")
        

main()

'''def primes(n):
        if n<=1:
            return False
        for i in range (2,n):
            if n%i==0:
                return False
            return True
def get_input():
    n=int(input("enter number"))
    return n
def main():
        n=get_input()
        if primes(n):
            print(f"it is prime number")
        else:
            print(f"it is not prime")
    
main()'''
        
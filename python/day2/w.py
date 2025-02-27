def primes(n):
    if n <= 1:
        return False
    if n == 2:
        print(f"{n} is the least prime number")
        return True
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

def get_input():
    n = int(input("Enter a number: "))
    return n

def main():
    n = get_input()
    print(f"Prime numbers from 1 to {n}:")
    i = 1
    while i <= n:
        if primes(i):
            print(i, end=" ")
        i += 1

main()

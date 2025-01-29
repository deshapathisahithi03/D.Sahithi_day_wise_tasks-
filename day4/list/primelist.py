def primes(m,n):
    if n <= 1:
        return False
    for i in range(m, n):
        if n % i == 0:
            return False
    return True

def get_input():
    n = int(input("Enter a number: "))
    m=int(input("enter b number: "))
    return (n,m)
def maxi(n,l2,m):
    maxim=l2[0]
    for i in range(n,m):
        if l2[i] > maxim:
            maxim=l2[i]
            return maxim
def mini(n,l2,m):
    minim=l2[0]
    for i in range(n,m):
        if l2[i]  < minim:
            minim=l2[i]
            return minim
def main():
    (n,m) = get_input()
    l2=[]
    print(f"Prime numbers from {n} to {m}:")
    for i in range(n, m + 1):
        if primes(i):
            l2.append(i)
    print("list:",l2)
    print(f"the maximum number is:{maxi(n,l2,m)}")
    print(f"the minimum number is:{mini(n,l2,m)}")
            
        

main()

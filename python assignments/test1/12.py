def get_input():
    n=int(input("enter number:"))
    return n
def patterns(n):
        for i in range(1,n+1):
            for j in range(i):
                        print("*",end= "")
            print()
def main():
    n=get_input()
    patterns(n)

main()
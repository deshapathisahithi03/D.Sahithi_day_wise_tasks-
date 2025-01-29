def get_input():
    n=int(input("enter input"))
    return n
def fib(n):
    f=0
    s=1
    for i in range(2,n) :
            t=f+s
            print(f"the series are:{t}")
            f=s
            s=t
def main():
    n=get_input()
    fib(n)
    
main()
            
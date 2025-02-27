def get_input():
    n=int(input("enter number :"))
    return n
def prints(n):
    for i in range (1,n):
        if i%3==0:
            print(f"Fizz")
        elif i%5==0:
            print(f"Buzz")
        elif i%3 and i%5==0:
            print(f"FizzBuzz")
        else:
            print(i)
def main():
    n=get_input()
    prints(n)
    
    
main()

            
            
def get_input():
    n=int(input("enter number:"))
    p=int(input("enter the range:"))
    return (n,p)

def multiply(n,p):
     print(f"the multiplication table for {n}\n")
     for i in range(1,p+1):
            g=n*i
            print(f"{n} * {i} = {g} ")
        
def main():
    (n,p)=get_input()
    multiply(n,p)
    
main()
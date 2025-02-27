#displaying the output
def display(k):
    print(f"the max number is:{k}")
#assigning inputs
def get_input():
    a=input("enter a:")
    b=input("enter b:")
    c=input("enter c:")
    return(a,b,c)
#finding maximum of three numbers
def max3(a,b,c):
#comparing a,b,c using conditional statements
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else :
        return c
#main function
def main():
    (a,b,c)=get_input()#calling inputs
    k=max3(a,b,c)#calling max3 function
    display(k)#calling display function 
    
main()#calling main function
    
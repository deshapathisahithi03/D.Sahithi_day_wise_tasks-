#displaying the output
def display(k):
    print(f"the max number is:{k}")
#assigning inputs
def get_input():
    a=input("enter a:")
    b=input("enter b:")
    c=input("enter c:")
    return(a,b,c)
def max3(a,b,c):
    #consider a variable which is assume to be max and assign the variable with a
    big=a
    bv="a"
    if b>big:
        big=b
        bv="b"
    if c>big:
        big=c
        bv="c"
    return(big,bv)  
#main function
def main():
    (a,b,c)=get_input()#calling inputs
    big=max3(a,b,c)
    display(big)#calling display function 
    
main()#calling main function
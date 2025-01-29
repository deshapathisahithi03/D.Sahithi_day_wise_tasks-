#displaying the output
def display(avg):
    print(f"the avg value is {avg}")
#considering inputs
def get_input():
    a=input("a:")
    b=input("b:")
    c=input("c:")
    d=input("d:")
    n=input("n:")
    return(a,b,c,d,n)
#sum of four number
def add(a,b,c,d):
    val=int(a)+int(b)+int(c)+int(d)
    return val
#calculating average of four numbers
def avg(val,n):
    average=(int(val))/int(n)
    return average
#main function
def main():
    (a,b,c,d,n)=get_input()
    val=add(a,b,c,d)
    ave=avg(val,n)
    display(ave)
    
main()
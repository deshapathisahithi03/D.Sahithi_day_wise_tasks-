#displaying the output
def display(avg):
    print(f"the avg value is {avg}")
#considering inputs
def get_input():
    a=input("a:")
    b=input("b:")
    c=input("c:")
    d=input("d:")
    return(a,b,c,d)
#sum of four number
def add(a,b,c,d):
    val=int(a)+int(b)+int(c)+int(d)
    return val
#calculating average of four numbers
def avg(val):
    average=(int(val))/4
    return average
#main function
def main():
    (a,b,c,d)=get_input()
    val=add(a,b,c,d)
    ave=avg(val)
    display(ave)
    
main()
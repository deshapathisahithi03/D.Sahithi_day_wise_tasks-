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
#calculating average of four numbers
def avg(a,b,c,d):
    average=(int(a)+int(b)+int(c)+int(d))//4
    return average
#main function
def main():
    (a,b,c,d)=get_input()
    ave=avg(a,b,c,d)
    display(ave)
    
main()
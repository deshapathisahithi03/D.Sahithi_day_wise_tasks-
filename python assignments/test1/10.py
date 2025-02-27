def get_input():
    tob=int(input("enter total amount"))
    nop=int(input("enter number of people"))
    tp=int(input("enter tip"))
    return (tob,nop,tp)
def b(tob,nop,tp):
    p=tp//100
    q=((tob+p)/nop)
    print(f"the amount is {q}")
def main():
    (top,nop,tp)=get_input()
    b(top,nop,tp)

main()
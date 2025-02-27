def get_input():
    weight=float(input("enter weight:"))
    height=float(input("enter height:"))
    return (weight,height)
def bmi(weight,height):
    c=weight/(height ** 2)
    print(f"the bmi is {c:.2f}")
    if c >18.5 and c<24.9:
        print(f"Normal")
    elif c<18.5:
        print(f"UnderWeight")
    elif c>25 and c<29.9:
        print(f"OverWeight")
    else:
        print(f"obese")

def main():
    (weight,height)=get_input()
    bmi(weight,height)
    
main()



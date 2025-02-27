def get_input():
    s=int(input("enter salary"))
    a=int(input("enter age"))
    cs=float(input("enter credit score"))
    return(s,a,cs)
def bank(s,a,cs):
         if cs >= 50 and s < 300000 and a > 30:
            print(f"Loan approved")
         elif 25 < cs < 45 and s < 300000 and a > 30:
            print(f"Loan approved based on conditions")
         elif cs > 50 and s > 300000 and a > 30:
            print(f"Rejection due to high salary")
         elif cs < 50 and s < 300000 and a < 30:
            print(f"Rejection due to age limit")
         else:
             print(f"loan will not approve due to rules are not satisfied")

def main():
        (s,a,cs)=get_input()
        bank(s,a,cs)

main()


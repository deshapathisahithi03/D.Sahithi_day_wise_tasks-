
def get_input():
    c=float(input("enter the number1:"))
    f=float(input("enter the number2:"))
    k=float(input("enter number3:"))
    return(c,f,k)
def celsius(f,k):
    t=((f-32)*5/9)
    q=(k-273.15)
    print(f"the conversion value of fahrenheit to celsius {t}")
    print(f"the conversion value of kelvin to celsius {q} ")
def fare(c,k):
    m=((c*9/5)+32)
    r=((k-32)*9/5)
    print(f"the conversion value of celsius to fahrenheit {m}")
    print(f"the conversion value of kelvin to fahrenheit  {r}")
def kelvin(f,c):
    s=(c+273.15)
    v=(((f-32)*5/9)+273.15)
    print(f"the conversion value of   celsius to kelvin {s}")
    print(f"the conversion value of fahrenheit to kelvin {v}")
    
def main():
    (c,f,k)=get_input()
    celsius(f,k)
    fare(c,k)
    kelvin(f,c)
    
main()
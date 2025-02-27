def is_palindrome(n):
    value_str = str(n)
    return (value_str == value_str[::-1])
def get_input():
    l2=[]
    n=input("enter string")
    return(l2,n)
def main():
    n=get_input()
    while True:
        if n.lower() == 0:
            break
        if is_palindrome(n):
            print(f"'{n}' is a palindrome.")
        else:
            print(f"'{n}' is not a palindrome.")
            
main()

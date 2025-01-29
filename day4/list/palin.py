'''def palindrome(l2):
    if l2==l2[::-1]:
        print(f"it is a palindrome")
    if l2==" ":
        return 
    else:
        print(f"it is not palindrome")
def get_input():
    l2=input("enter string:")
    return l2
def main():
    l2=get_input()
    palindrome(l2)
    
main()'''
def palindrome(l2):
    if l2 == "":  # Check for empty string
        print("Input is empty.")
        return
    
    # Check if the string is only spaces
    if all(char == " " for char in l2):
        print("Input is only spaces.")
        return

    if l2 == l2[::-1]:  # Check for palindrome
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")

def get_input():
    l2 = input("Enter a string: ")
    return l2

def main():
    l2 = get_input()
    palindrome(l2)

main()



        
    
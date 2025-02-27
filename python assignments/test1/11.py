# Function to get user input
def get_input():
    password=input("Enter a password to check its strength: ")
    return password
# Function to check the password strength
def check_strength(password):
    length = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)
    if all([length, has_upper, has_lower, has_digit, has_special]):
        return "strong"
    elif length and (has_upper or has_lower) and (has_digit or has_special):
        return "moderate"
    else:
        return "weak"
# Main function
def main():
    password = get_input()  # Get the password from the user
    strength = check_strength(password)  # Check its strength
    print(f"Password strength: {strength}")
# Run the main function program
main()

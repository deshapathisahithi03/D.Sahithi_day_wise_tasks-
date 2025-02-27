# Function to get user input
def get_input():
    str=input("Enter a string: ")
    return str
# Function to analyze the string
def analyze_string(s):
    vowels = 0
    consonants = 0
    digits = 0
    special_characters = 0
    for char in s:
        if char.lower() in "aeiou":
            vowels += 1
        elif char.isalpha():
            consonants += 1
        elif char.isdigit():
            digits += 1
        elif not char.isspace():
            special_characters += 1

    reversed_string = s[::-1]
    return (vowels, consonants, digits, special_characters, reversed_string)

# Main function to run the program
def main():
    string = get_input()  # Get input from the user
    vowels, consonants, digits, special_characters, reversed_string = analyze_string(string)  # Analyze string

    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")
    print(f"Digits: {digits}")
    print(f"Special Characters: {special_characters}")
    print(f"Reversed String: {reversed_string}")

# Run the program
main()

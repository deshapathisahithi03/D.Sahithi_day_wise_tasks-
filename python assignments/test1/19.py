
def get_numbers():
    num = input("Enter a list of numbers ")
    return list(map(int, num.split()))

def sort_numbers(numbers):
    numbers.sort()
    return numbers

def find_second_largest(numbers):
    if len(numbers) < 2:
        return None
    return numbers[-2]

def main():
    numbers = get_numbers()  
    numbers = sort_numbers(numbers)  
    second = find_second_largest(numbers) 
    if second is None:
        print("There is no second largest number.")
    else:
        print(f"The second largest number is: {second}")

main()

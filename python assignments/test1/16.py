def separate_odd_even(numbers):
    odd = []
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return odd, even

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
odd, even = separate_odd_even(numbers)
print("Odd numbers:", odd)
print("Even numbers:", even)

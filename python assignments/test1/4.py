def calculate(p):
    if p >= 90:
        return 'A'
    elif p >= 75:
        return 'B'
    elif p >= 50:
        return 'C'
    else:
        return 'Fail'
def get_input():
    s1=input("enter name of the student")
    return s1
def main():
    s1=get_input()
    marks = []
    total = 0
    for i in range(1, 6):
        mark = float(input(f"Enter marks for subject {i}: "))
        total += mark
    p = total/5
    g= calculate(p)
    print(f"Student Name: {s1}")
    print(f"Total Marks: {total}")
    print(f"Percentage: {p:}%")
    print(f"Grade: {g}")

main()

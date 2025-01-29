l1 = []
k=int(input("enter number of elements:"))
for i in range(k):
    n = int(input(f"Enter number {i+1}: "))
    l1.append(n)
mini = l1[0]
maxi = l1[0]
for num in l1:
    if num < mini:
        mini = num
    if num > maxi:
        maxi = num
print(f"The minimum value is: {mini}")
print(f"The maximum value is: {maxi}")
    

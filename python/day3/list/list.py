#add a empty list
l1=[]
print("1.list is empty:",l1)
#add list of items
l2=[0,1,2,3]
print("2.list with four items:",l2)
#with nested list
l3=['abc',['def','ghi']]
print("3.a nested list:",l3)
#creating a list from a string
l4=list('spam')
print("4.list created from 'spam:'",l4)
#print between the range
l5=list(range(-4,4))
print("5.list of elements of range:",l5)
#accessing an element by index
l6=[10,20,30,40]
print("6.element at index 2 of l6:",l6[3])
#accessing an element from a nested list by index
l7=['x',[10,20,30],'y']
print("7.element at l7[1][2] (nested list):",l7[1][2])
#slicing a list
l8=[0,1,2,3,4,5]
print("8.slicing l8 from index 2 to 4(l8[2:5]):",l8[2:6])
#getting the length of a list
print("9.length of l8:",len(l8))
#demonstrating nested indexing and slicing together
l9=[10,[100,20,300,400],50]
print("10a.element atl9[1]:",l9[1])
print("10b.element atl9[1][3]:",l9[1][3])
print("10c.slicing sublist l9[1][1:3]:",l9[1][1:3])
#summary of outputs
print("\nSummary of Lists")
print("L1:",l1)
print("L2:",l2)
print("L3:",l3)
print("L4:",l4)
print("L5:",l5)
print("L6:",l6)
print("L7:",l7)
print("L8:",l8)
print("L9:",l9)


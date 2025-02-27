t1=()
print(f"the empty tuple is:{t1}")
t2=(0,)
print(f"the one item tuple:{t2}")
t3=(0,'ni',1.2,3)
print(F"the multiple tuples:{t3}")
t4=("abc",('def','ghi'))
print(f"the nested tuples:{t4}")
t5=tuple('spam')
print(f"the tuple of items in a relatable:{t5}")
'''t5[i]
t5[i][j]
t5[i:j]'''
print(t5[0])
print(t4[1][1])
print(t5[1:3])
print(len(t5))


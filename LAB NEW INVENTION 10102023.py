a=[1,2,3,4,5,6,7,8,9,10]
print("length of list: ",len(a))
mid=len(a)//2
print("mid value: ",mid)
target=int(input("Enter the target: "))
if target<=0:
    print("unknown")
elif mid > target:
    print("it is on the index: ",target-1)
elif target>=11:
    print("unknown")
else:
    print("it is on the index: ",target-1)

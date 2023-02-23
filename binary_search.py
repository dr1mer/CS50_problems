# binary search

def binary_search(array, x):
    start = 0
    end = len(array)-1
    mid=0
    while start<=end:
        mid=(start+end)//2
        if array[mid]<x:
            start=mid+1
        elif array[mid]>x:
            end=mid-1
        else:
            return mid
    return -1
    
arr=[1,2,5,6,10,11,16,20,35]    
x=16
result=binary_search(arr,x)
print("The result is under index",result)
    

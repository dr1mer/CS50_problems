arr = [5,1,4,3,2,10,5,9]
for j in range(len(arr)-1):
        for i in range(1,len(arr)-j):
            if arr[i-1]>arr[i]:
                arr[i-1],arr[i]=arr[i],arr[i-1]
print(arr)

def selection_sort(array, size):
    
    for i in range(size):
        small=i
        
        for j in range(i+1, size):
            if array[j]<array[small]:
                small=j
        array[i],array[small] = array[small], array[i]
        
        
data = [13, -1, 0, 15, 12, 13, 4, 5, 100, 95]
size = len(data)
selection_sort(data,size)
print(data)

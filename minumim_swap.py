def min_swap(arr):
    indexes = list(range(1,len(arr)+1))
    visited = []
    swap=0
    for i in range(len(arr)):
        if arr[i] == indexes[i]:
            visited.append(indexes[i])
        else:
            if indexes[i] not in visited:
                swap+=1
                arr[arr[indexes[i]-1]-1],arr[indexes[i]-1] = arr[indexes[i]-1],arr[arr[indexes[i]-1]-1]
                visited.append(indexes[i])
    return swap
a = [7, 1, 3, 2, 4, 5, 6]
print(min_swap(a))
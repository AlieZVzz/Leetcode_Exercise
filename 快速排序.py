def quickSort(array):
    larger = list()
    smaller = list()
    if len(array) < 2 :
        return array
    else:
        standard = array[0]
        for i in array[1:]:
            if i > standard:
                larger.append(i)
            else:
                smaller.append(i)
        return quickSort(smaller) + [standard] + quickSort(larger)
print(quickSort([2,3,1,5,7,6]))


def partition(arr, low, high):
    i = low -1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j]<=pivot:
            
            i +=1
            # print(i)
            arr[i], arr[j] = arr[j], arr[i]
        
    # print(arr)
    arr[i+1], arr[high] = arr[high],arr[i+1]
 
    return i+1
def quick_sort(arr, low, high):
    if low<high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


# print(quick_sort([6,5,9,4,7],0, 4))

def find_k(arr, k):
    low = 0
    high = len(arr)-1
    k = len(arr)-k
    while low<high:
        target = partition(arr, low, high)
        if k == target:
            return arr[k]
        elif k < target:
            high = target-1
        else:
            low = target+1
    return arr[low]


# print(find_k([6,5,9,4,7],1))
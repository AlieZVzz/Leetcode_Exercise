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
# print(quickSort([2,3,1,5,7,6]))
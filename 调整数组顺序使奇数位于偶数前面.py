def reOrderArray(self, array):
    l, r = 0, len(array)-1
    while l < r:
        while l < r and array[l]&1 == 1:
            l += 1
        while l < r and array[r]&1 == 0:
            r -= 1
        array[l], array[r] = array[r], array[l]
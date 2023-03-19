def duplicate(self, numbers, duplication):
    for i in range(len(numbers)):
        while i != numbers[i]:
            if numbers[i] == numbers[numbers[i]]:
                duplication[0] = numbers[i]
                return True                    
            temp = numbers[i]
            numbers[i] = numbers[temp]
            numbers[temp] = temp
    return False
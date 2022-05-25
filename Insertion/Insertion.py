#Insertion Sort Algorithm
# Best case
# Worst case
# 
array = [5,3,4,1,2]

for i in range(1, len(array)):
    valueToCompare = array[i]
    print('comparing the value' + valueToCompare)
    position = i

    while(0 < position and array[position -1] > valueToCompare):
        array[position] = array[position - 1]
        position = position -1

    array[position] = valueToCompare
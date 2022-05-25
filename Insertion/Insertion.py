#Insertion Sort Algorithm
# Best case
# Worst case
# 
array = [5,3,4,1,2]

print('we skip over position 0 comparison because there is no value to the left of it')

for i in range(1, len(array)):
    valueToCompare = array[i]
    position = i
    print('comparing the value ' + str(valueToCompare) + ' at position ' + str(position))
    

    while(0 < position and array[position -1] > valueToCompare):
        array[position] = array[position - 1]
        print('comparing ' + str(valueToCompare) + ' with ' + str(array[position]))
        position = position -1

    array[position] = valueToCompare
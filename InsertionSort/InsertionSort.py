#Insertion Sort Algorithm
# Referenced https://www.bigocheatsheet.com/ for complexity times
#
#Time complexity (Big O)
#------------------
# Best case:   | O(n)
# Worst case:  | O(n^2)
# Average case:| O(n^2)

def InsertionSort(array): 

    print('we skip over position 0 comparison because there is no value to the left of it')

    for i in range(1, len(array)):
        valueToCompare = array[i]
        position = i
        print('comparing ' + str(valueToCompare) + ' at position ' + str(position))
        

        while(0 < position and array[position -1] > valueToCompare):
            array[position] = array[position - 1]
            print('moved ' + str(valueToCompare) + ' to the left ' + str(array[position]))
            position = position -1

        array[position] = valueToCompare
        
    print('the final result is ' + str(array))


myArray = [5,3,4,1,2]
InsertionSort(myArray)

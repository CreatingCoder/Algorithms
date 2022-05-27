/** Insertion Sort Algorithm
    Referenced https://www.bigocheatsheet.com/ for complexity times
    
    Time complexity (Big O)
    ------------------
    Best case:   | O(n)
    Worst case:  | O(n^2)
    Average case:| O(n^2) 
    **/

function InsertionSort(array) {
  
    
    console.log('we skip over position 0 comparison because there is no value to the left of it');
    for(let i = 0; i < array.length; i++){

        let valueToCompare = array[i];
        position = i;
        console.log('Comparing ' + valueToCompare + ' at position ' + position);

        while(0 < position && array[position - 1] > valueToCompare){
            array[position] = array[position - 1];
            console.log('moved ' + valueToCompare + ' to the left ' + array[position]);
            position = position - 1;
        }
        array[position] = valueToCompare
    } 
    console.log('the final result is ' + array);  
  return array;
}

myArray = [5,3,4,1,2];
InsertionSort(myArray);

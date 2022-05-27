/** Insertion Sort Algorithm
    Referenced https://www.bigocheatsheet.com/ for complexity times
    
    Time complexity (Big O)
    ------------------
    Best case:   | O(n)
    Worst case:  | O(n^2)
    Average case:| O(n^2) 
    **/

class InsertionSort {


   void sort(int array[]){
   
      for(int i = 0; i < array.length; i++){
         int valueToCompare = array[i];
         int position = i;
      
         while(0 < position && array[position -1] > valueToCompare){
            array[position] = array[position - 1];
            System.out.println("Moved " + valueToCompare + " to the left of " + array[position]);
            position = position - 1;
         }
         array[position] = valueToCompare;
      }
      
     //For loop below is only for printing
      System.out.print("The final result is " );
      for(int j = 0; j < array.length; ++j){
         System.out.print(array[j] + " ");
      }
   }


   public static void main(String args[]){
   
      int myArray[] = {5,3,4,1,2};
      InsertionSort object = new InsertionSort(); 
      object.sort(myArray);
   }
}
  
    

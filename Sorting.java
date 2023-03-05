public class Sorting {  
    
	public static void bubbleSort(int[] arr) {  
        int n = arr.length;  
		for(int outer=n-1; outer > 0; outer--){  
			for(int inner=0; inner < outer; inner++){  
				if(arr[inner] > arr[inner+1]){  
					System.out.println("inner is " + inner + " swapping " + arr[inner] + " and " + arr[inner+1]);
					//swap elements  
					int temp = arr[inner];  
					arr[inner] = arr[inner+1];  
					arr[inner+1] = temp;  
				}  
			}  
			System.out.println("outer is " + outer);
			System.out.println("Array is:");
			printArray(arr);
        }  
    }  
	
	public static void selectionSort(int[] a){
		for (int outer = 0; outer < a.length-1; outer++){
			System.out.println("outer is " + outer);
			int min = outer;
			for(int inner = outer+1; inner < a.length; inner++){
				if (a[inner] < a[min]){
					min = inner;
				}
			}
			System.out.println("min is " + min);
			System.out.println("swapping " + a[outer] + " and " + a[min]);
			
			int temp = a[outer];
			a[outer] = a[min];
			a[min] = temp;
		}
		
	}
	
	public static void printArray(int[] arr){
		for(int i=0; i < arr.length; i++){  
            System.out.print(arr[i] + " ");  
        }  
        System.out.println();  
	}
	
    public static void main(String[] args) {  
        int arr[] ={7,5,2,3,1};  
                 
        System.out.println("Array Before Bubble Sort");  
		printArray(arr);
                  
        selectionSort(arr); 
		printArray(arr);
    }  
}  
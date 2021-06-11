
import java.util.Random;

public class RicardoJavaProgram1 {

     public static void main(String[] args) {
        
        int array[] = new int[10];	
	Random rand = new Random();
	
	System.out.println("Unsorted Array:");

	for (int i = 0; i < array.length; i++)
	{
		array[i] = rand.nextInt(100);
		System.out.print(array[i] + " ");
	}
	
	System.out.println("\n");

	/* Sort */
	for(int x = 0; x < array.length - 1; x++)
		for( int y = 0; y < array.length - x - 1; y++)
			if(array[y] > array[y + 1])
			{
				int temp = array[y];
				array[y] = array[y + 1];
				array[y + 1] = temp;
			}

	System.out.println("Sorted Array:");
	for(int e = 0; e < array.length; e++)
		System.out.print(array[e] + " ");
    }
}

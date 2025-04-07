import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class rec11_split {
    public static void main(String[] args) {
        int[] input = {1,2,3,4,5};
        List<int[]> res = split(input, 3);
        int[] smaller_or_eq = res.get(0);
        int[] larger = res.get(1);
        System.out.println(Arrays.toString(smaller_or_eq));
        System.out.println(Arrays.toString(larger));
    }

    public static List<int[]> split(int[] int_arr, int n) {
        List<Integer> smaller_or_eq = new ArrayList<>();
        List<Integer> larger = new ArrayList<>();

        // add num to arraylist
        for (int num: int_arr) {
            if (num <= n) {
                smaller_or_eq.add(num);
            } else {
                larger.add(num);
            }
        }
        int[] smaller_or_eq_arr = new int[smaller_or_eq.size()];
        int[] larger_arr = new int[larger.size()];

        // convert arraylist to arr
        for (int i = 0; i < smaller_or_eq.size(); i++) {
            smaller_or_eq_arr[i] = smaller_or_eq.get(i);
        }

        for (int i = 0; i < larger.size(); i++) {
            larger_arr[i] = larger.get(i);
        }

        // returns 2 arrays as a list
        List<int[]> res = new ArrayList<>();
        res.add(smaller_or_eq_arr);
        res.add(larger_arr);

        return res;
    }
}

// assume that the number in the int arr is within the int range
// to create a sorting algo, we can recursively call this function
// until the size of arr is 1, then merge the 2 array back up
// like the merge algorithm in merge  sort
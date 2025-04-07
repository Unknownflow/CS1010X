//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        nth_sum_of_num_array(-1);
        nth_sum_of_num_array(4);
        nth_sum_of_num_array(0);
        nth_sum_of_num_array(8);

    }

    public static void nth_sum_of_num_array(int n) {
        int num_array[] = {3, 4, 6, 1, 0, 9, 8, 6, 2, 5};
        // Write your code here
        // Do not modify any other code
        int res = 0;
        if (n < 0 || n > 10) {
            System.out.println(-1);
//            return -1;
        } else {
            for (int i = 0; i < n; i++) {
                res = res + num_array[i];
            }
            System.out.println(res);
//            return res;
        }
    }

}
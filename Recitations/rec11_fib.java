public class rec11_fib {
    public static void main(String[] args) {
//        for (int i = 0; i < 10; i++) {
//            System.out.println(fib(i));
//        }
//        System.out.println(fib(46));
        // fib(46) prints 1836311903
        System.out.println(fib(47));
        // fib(47) prints -1323752223
        // fib(47) is 2,971,215,073, however, the int limit in java is 2,147,483,647
        // and when the number when a number larger than the limit is stored, a
        // negative value would be stored instead, a larger data type should
        // be used instead to store the val of large fib

    }

    public static int fib(int n) {
        if (n == 0) {
            return 0;
        }
        int first = 0;
        int second = 1;
        for (int i = 1; i < n; i++) {
            int temp = first + second;
            first = second;
            second = temp;
        }
        return second;
    }
}

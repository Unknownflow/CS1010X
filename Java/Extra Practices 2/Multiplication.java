public class Multiplication {
    public static void main(String[] args) {
        printTable(10);
    }
    public static void printTable(int n) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.printf("%4d", i*j);
            }
            System.out.println();
        }
    }
}

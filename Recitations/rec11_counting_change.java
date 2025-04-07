import java.util.Scanner;

public class rec11_counting_change {
    public static void main(String[] args) {
        int[] cents = {1, 5, 10, 20,50};
        int cents_type = cents.length;

        // input to get amount from user
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter amount: ");
        String input = scanner.nextLine();
        int amount = Integer.parseInt(input);

        int res = counting_change(amount, cents_type, cents);
        System.out.println(res);
    }

    public static int counting_change(int amount, int cents_type, int[] cents) {
        if (amount == 0) {
            return 1;
        } else if (amount < 0) {
            return 0;
        } else if (cents_type == 0) {
            return 0;
        }
        return counting_change(amount - cents[cents_type-1], cents_type, cents) +
                counting_change(amount, cents_type - 1, cents);
    }
}

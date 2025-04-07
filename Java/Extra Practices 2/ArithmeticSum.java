public class ArithmeticSum {
    public static void main(String[] args) {
//        System.out.println(getApproxPi(1));
//        System.out.println(getApproxPi(5));
//        System.out.println(getPi(0.001));
//        System.out.println(getPi(1.0E-4));
        System.out.println(getPi(1.0E-5));

    }
    public int getSum(int n) {
        int res = 0;
        for (int i = 1; i <= n; i++) {
            res += i;
        }
        return res;
    }

    public int getMoreSum(int n) {
        int res = 0;
        for (int i = 1; i <= n*2; i=i+2) {
            res += i;
        }
        return res;
    }

    public int getAltSum(int n) {
        if (n % 2 == 0) {
            return -n;
        } else {
            return n;
        }
    }

    public static double getApproxPi(int n) {
        double res = 0;
        boolean isPositive = true;
        for (int i = 1; i <= n*2-1; i=i+2) {
            if (isPositive) {
                res += (double) 4 / i;
            } else {
                res -= (double) 4 / i;
            }
            isPositive = !isPositive;
        }
        return res;
    }

    public static double getPi(double t) {
        double prev = 4;
        double curr = 4 - ((double) 4 / 3);
        double diff = curr - prev;
        boolean isPositive = true;
        int i = 5;

        while (!(0 <= diff && diff <= t)) {
            prev = curr;
            if (isPositive) {
                curr += (double) 4 / i;
            } else {
                curr -= (double) 4 / i;
            }
            isPositive = !isPositive;
            diff = curr - prev;
            i += 2;
        }

        return curr;
    }
}

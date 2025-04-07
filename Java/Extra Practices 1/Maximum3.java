public class Maximum3 {

    public int getMax(int a, int b, int c) {
        int max;

        // Replace ONLY the ..
        if (a > b)
            if (a > c)
                max = a;
            else
                max = c;
        else
            if (b > c)
                max = b;
            else
                max = c;

        return max;
    }
}

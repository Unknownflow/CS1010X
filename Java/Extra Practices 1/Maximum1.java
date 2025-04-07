public class Maximum1 {
    public int getMax(int a, int b, int c) {
        int max;

        // Replace ONLY the ..
        if ((a >= b) && (a >= c))
            max = a;
        else
            if (b >= c)
                max = b;
            else
                max = c;

        return max;
    }
}


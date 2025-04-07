public class Maximum2 {

    public int getMax(int a, int b, int c) {
        int max = a;

        if (b >= max)
            max = b;
        if (c >= max)
            max = c;

        return max;
    }
}

/**
 * Class that manages the bus routes.
 */
public class BusMap {

    public static void main(String[] args) {
        Pair res = getNextStopAndTimeTaken("A1", "PGP (START)");
        System.out.println(res.stopName);
        System.out.println(res.timeTakenFromPreviousStop);
        Pair res2 = getNextStopAndTimeTaken("B1", "OPP YIH");
        System.out.println(res2.stopName);
        System.out.println(res2.timeTakenFromPreviousStop);
        Pair res4 = getNextStopAndTimeTaken("C", null);
        System.out.println(res4.stopName);
        System.out.println(res4.timeTakenFromPreviousStop);
        Pair res3 = getNextStopAndTimeTaken("D1", "BIZ 2");
        System.out.println(res3);
    }

    /**
     * Returns a `Pair` containing the name of the next bus stop for this bus, as well as the time needed to reach that
     * next bus stop from the current stop.
     * <p>
     * IMPORTANT: If `currentStop == null`, return the first stop along the route. If `currentStop` is the final stop
     * for this bus, return `null`.
     *
     * @param busName     Number of the bus: "A1", "B1", "C" or "D1".
     * @param currentStop The current stop of the bus.
     */
    public static Pair getNextStopAndTimeTaken(String busName, String currentStop) {
        // TODO: Implement this (Task 1b)
        String[] stops = {};
        int[] timings = {};
        switch (busName) {
            case "A1":
                stops = A1_STOPS;
                timings = A1_TIMINGS;
                break;
            case "B1":
                stops = B1_STOPS;
                timings = B1_TIMINGS;
                break;
            case "C":
                stops = C_STOPS;
                timings = C_TIMINGS;
                break;
            case "D1":
                stops = D1_STOPS;
                timings = D1_TIMINGS;
                break;
        }
        String lastStop = stops[stops.length-1];
        if (currentStop == null) {
            return new Pair(stops[0], timings[0]);
        } else if (currentStop == lastStop) {
            return null;
        } else {
            for (int i = 0; i < stops.length; i++) {
                if (stops[i] == currentStop) {
                    return new Pair(stops[i+1], timings[i+1]);
                }
            }
        }
        return null;
    }

    /**
     * Names of the bus stops along the routes for each of the buses: A1, B1, C, D1.
     */
    private static final String[] A1_STOPS = {"PGP (START)", "KR MRT", "LT 27", "UNIVERSITY HALL", "OPP UHC",
            "YIH", "CENTRAL LIBRARY", "LT 13", "AS 5", "COM 2", "BIZ 2", "OPP TCOMS", "PGP (END)"};
    private static final String[] B1_STOPS = {"KR BUS TERMINAL", "IT (OPP CLB)", "OPP YIH", "UNIVERSITY TOWN",
            "YIH", "CENTRAL LIBRARY", "LT 13", "AS 5", "BIZ 2"};
    private static final String[] C_STOPS = {"KR BUS TERMINAL (START)", "JAPANESE PRI SCH", "KENT VALE",
            "MUSEUM", "UNIVERSITY TOWN (FROM KR)", "UHC", "OPP UNIVERSITY HALL", "S 17 (OPP LT 27)", "LT 27",
            "UNIVERSITY HALL", "OPP UHC", "UNIVERSITY TOWN (TO KR)", "RAFFLES HALL", "EA", "KR BUS TERMINAL (END)"};
    private static final String[] D1_STOPS = {"OPP HSSML", "OPP NUSS", "COM 2 (FROM HSSML)", "VENTUS (OPP LT 13)",
            "IT (OPP CLB)", "OPP YIH", "MUSEUM", "UNIVERSITY TOWN", "YIH", "CENTRAL LIBRARY",
            "LT 13", "AS 5", "COM 2 (TO BIZ 2)", "BIZ 2"};

    /**
     * Time taken to reach the i-th stop from the (i - 1)-th stop. The integer at the i-th index refers to that for the
     * i-th stop above.
     */
    private static final int[] A1_TIMINGS = {0, 3, 3, 2, 2, 1, 2, 2, 5, 6, 3, 1, 1};
    private static final int[] B1_TIMINGS = {0, 5, 1, 2, 2, 1, 2, 2, 1};
    private static final int[] C_TIMINGS = {0, 1, 10, 3, 1, 3, 1, 2, 1, 1, 1, 2, 2, 1, 2};
    private static final int[] D1_TIMINGS = {0, 4, 2, 2, 1, 1, 2, 1, 3, 1, 1, 7, 2, 4};

    /**
     * Helper class that associates a stop name and the time taken to reach that stop from the previous stop.
     */
    public static class Pair {
        String stopName;
        int timeTakenFromPreviousStop;

        public Pair(String stopName, int time) {
            this.stopName = stopName;
            timeTakenFromPreviousStop = time;
        }
    }

}

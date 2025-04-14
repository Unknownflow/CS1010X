import java.util.Random;

/**
 * Represents the NUS Bus A1.
 */
public class BusA1 extends AbstractBus {

    public static void main(String[] args) {
        BusA1 busA1 = new BusA1();
        System.out.println(busA1.moveToNextStop());
    }

    public BusA1() {
        BusMap.Pair pair = BusMap.getNextStopAndTimeTaken("A1", null);
        assert pair != null;
        currentStopName = pair.stopName; // assigns to superclass' `stopName`
    }

    /**
     * Moves the bus to next stop and returns the amount of time spent moving. If the bus is already at its final stop,
     * return -1.
     *
     * @return The amount of time spent moving if the bus is not at its final stop; else, -1.
     */
    @Override
    public int moveToNextStop() {
        // TODO: Implement this (Task 2a)
        BusMap.Pair currentStopPair = BusMap.getNextStopAndTimeTaken("A1", currentStopName);
        if (currentStopPair != null) {
            currentStopName = currentStopPair.stopName;
            return currentStopPair.timeTakenFromPreviousStop;
        } else {
            return -1;
        }
    }

    // Bus A1 should breakdown with a probability of 0.1
    @Override
    public boolean didBreakdown(Random random) {
        // TODO: Implement this (Task 4a)
        return random.nextDouble() < 0.1;
    }

    @Override
    public String toString() {
        // You may choose to implement this for Task 3b
        return "Bus A1";
    }

}

import jdk.jfr.Event;

import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Random;
import java.util.Scanner;

/**
 * `BusSimulator` drives event simulation, i.e. both event processing and generation.
 */
public class BusSimulator {

    // Priority queue of events for the simulator to process.
    private final Queue<BusEvent> eventQueue = new PriorityQueue<>();

    // Pseudorandom number generator - DO NOT MODIFY THE SEED VALUE OF 999.
    private final Random random = new Random(999);

    /**
     * Constructs a `BusSimulator` with an event queue populated using the `busEvents` given.
     *
     * @param busEvents Events to populate the event queue with.
     */
    public BusSimulator(List<BusEvent> busEvents) {
        eventQueue.addAll(busEvents);
    }

    /**
     * Prints some simple status information about the simulator.
     */
    public void printStatus() {
        System.out.println("Bus simulator is ready!");
        System.out.println("There are a total of " + eventQueue.size() + " events.");
    }

    /**
     * Runs the simulator until the event queue has been emptied.
     */
    public void run() {
        // TODO: Implement this (Task 3b)

        while (!eventQueue.isEmpty()) {
            BusEvent busEvent = eventQueue.poll();
            System.out.println(busEvent.toString());
            AbstractBus bus = busEvent.bus;
            int timeToNextStop = bus.moveToNextStop();
            if (timeToNextStop != -1) {
                int time = busEvent.time + timeToNextStop;
                BusEvent newBusEvent = new BusEvent(bus, time, EventType.OPERATIONAL);
                eventQueue.offer(newBusEvent);
            }
        }
    }

    /**
     * Runs the simulator with a probability of bus breakdowns until the event queue has been emptied.
     * <p>
     * Uses the `random` initialised on top in `BusSimulator` for pseudorandom number generation.
     */
    public void runWithBreakdowns() {
        // TODO: Implement this (Task 4b)
        while (!eventQueue.isEmpty()) {
            BusEvent busEvent = eventQueue.poll();
            System.out.println(busEvent.toString());
            AbstractBus bus = busEvent.bus;
            int time = busEvent.time;
            EventType eventType = busEvent.eventType;
            switch (eventType) {
                case OPERATIONAL:
                    // add breakdown event if train broke down
                    if (bus.didBreakdown(random)) {
                        BusEvent breakdownEvent = new BusEvent(bus, time+1, EventType.BROKEN_DOWN);
                        eventQueue.offer(breakdownEvent);
                    } else {
                        // add event to reach next stop unless its at the last stop
                        int timeToNextStop = bus.moveToNextStop();
                        if (timeToNextStop != -1) {
                            BusEvent nextBusEvent = new BusEvent(bus, time+timeToNextStop, EventType.OPERATIONAL);
                            eventQueue.offer(nextBusEvent);
                        }
                    }
                    break;
                case BROKEN_DOWN:
                    // add repair event after train broke down
                    BusEvent repairEvent = new BusEvent(bus, time+10, EventType.REPAIRED);
                    eventQueue.offer(repairEvent);
                    break;
                case REPAIRED:
                    // add event to reach next stop unless its at the last stop
                    int timeToNextStop = bus.moveToNextStop();
                    if (timeToNextStop != -1) {
                        BusEvent nextBusEvent = new BusEvent(bus, time+timeToNextStop, EventType.OPERATIONAL);
                        eventQueue.offer(nextBusEvent);
                    }
                    break;
            }

        }
    }

    /**
     * Entry point to this program.
     */
    public static void main(String[] args) {
        List<BusEvent> busEvents = readBusEvents();
        BusSimulator simulator = new BusSimulator(busEvents);
        simulator.printStatus();
//        simulator.run();
        simulator.runWithBreakdowns();
    }

    /**
     * Reads in input from the console and produces a list of `BusEvent`s. This method has been provided for you.
     *
     * @return List of `BusEvent`s.
     */
    public static List<BusEvent> readBusEvents() {
        Scanner sc = new Scanner(System.in);
        int numBuses = sc.nextInt();
        sc.nextLine();
        List<BusEvent> busEvents = new ArrayList<>();

        for (int i = 0; i < numBuses; i++) {
            String[] busLine = sc.nextLine().split(" ");
            AbstractBus bus;

            // NOTE: Do read up on switch statements if you're unsure of what they do!
            switch (busLine[0]) {
            case "A1":
                bus = new BusA1();
                break;
            case "B1":
                bus = new BusB1();
                break;
            case "C":
                bus = new BusC();
                break;
            case "D1":
                bus = new BusD1();
                break;
            default:
                continue;
            }

            BusEvent busEvent = new BusEvent(bus, Integer.parseInt(busLine[1]), EventType.OPERATIONAL);
            busEvents.add(busEvent);
        }

        return busEvents;
    }
}

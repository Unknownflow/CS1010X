# Question 2

# Car

# Implement a function car that reads in data about your car and print out some statistical information. The input data includes:

#     Initial odometer value: the initial value of odometer (double type) before making any trip today. The odometer value on the car displays up to a maximum value of 999.9, after which it starts from 000.0 again. (An odometer is an instrument in a car for measuring the distance travelled.)
#     Distance per trip: A tuple of real numbers represented the distance for each trip.

# You may assume that the odometer value and distance per trip has at most one decimal place.

# After all above information are read, your program is to compute the final odometer value, the total number of trips, the average distance of all trips today, and the maximum difference in distance between two consecutive trips. The program then displays the outputs as shown in the sample runs below. The tuple representation is as follows:
# (final_odometer_value, total_number_of_trips, avg_dist_per_trip, max_diff_between_two_consecutive_trips)

# For example, in the sample run #1 below, the difference in distance between trip 1 and trip 2 is 4.8, while the difference in distance between trip 2 and trip 3 is 10.8. Hence the maximum difference is 10.8.

# Study the sample runs carefully so as to ensure that you have understood the question clearly. You should correct your output of floating point numbers to 1 decimal place.

def car(odometer, distances):

    if len(distances) == 0:

        return (odometer, 0, 0.0, 0.0)

    

    totalTrips = len(distances)

    totalDist = distances[0]

    maxDiff = 0

    prev = distances[0]

    

    for dist in distances[1:]:

        totalDist += dist

        diff = abs(dist - prev)

        if diff > maxDiff:

            maxDiff = diff

        prev = dist

    

    avgDist = round(totalDist / totalTrips, 1)

    odometer += totalDist

    while odometer > 999.99:

        odometer -= 999.99

        

    odometer = round(odometer, 1)

    maxDiff = round(maxDiff, 1)

    

    return (odometer, totalTrips, avgDist, maxDiff)
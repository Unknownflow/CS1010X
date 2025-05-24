def cache(slots):
    cache_arr = [-1 for i in range(8)]
    timestamp = [-1 for i in range(8)]
    time = 0
    total_time = 0

    for slot in slots:
        found = False
        min_time = float("inf")
        min_time_idx = -1
        for i in range(len(cache_arr)):
            if timestamp[i] < min_time:
                min_time = timestamp[i]
                min_time_idx = i
            if cache_arr[i] == slot:
                total_time += 20
                found = True
                timestamp[i] = time
                break

        if not found:
            total_time += 100
            timestamp[min_time_idx] = time
            cache_arr[min_time_idx] = slot
        time += 1

    return total_time


print(cache((19, 21, 3, 10, 7)))
print(cache((100, 300, 200, 300, 100)))
print(cache((3, 51, 24, 12, 3, 7, 51, 8, 90, 10, 5, 24)))
print(cache((24, 5)))

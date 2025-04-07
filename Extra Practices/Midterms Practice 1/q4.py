def count_instances(num, seq):
    if seq == ():
        return 0
    if num == seq[0]:
        return 1 + count_instances(num, seq[1:])
    else:
        return count_instances(num, seq[1:])



def count_instances(num, seq):
    count = 0

    for number in seq:
        if num == number:
            count += 1

    return count

print(count_instances(3, (1,2,3)))
print(count_instances(3, (1,2,3,3,2,3)))
print(count_instances(5, (1,2,3)))

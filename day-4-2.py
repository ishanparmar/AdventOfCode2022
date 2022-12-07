count: int = 0
for line in open("day-4-input", "r"):
    ranges = line.rstrip().split(",")
    if (int(ranges[0].split("-")[1]) >= int(ranges[1].split("-")[0]) and int(ranges[0].split("-")[0]) <= int(ranges[1].split("-")[1])) or \
            (int(ranges[0].split("-")[1]) <= int(ranges[1].split("-")[0]) and int(ranges[0].split("-")[0]) >= int(ranges[1].split("-")[1])):
        count += 1
        print(ranges)
print(count)
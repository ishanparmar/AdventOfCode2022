from itertools import islice
def count3Pairs(lines):
    # To store the frequencies of characters
    freq = [[0] * 122 for _ in range(3)]

    # To store the count of valid pairs
    count = 0

    # Update the frequencies of the characters of strings
    row = 0
    print("looping thru ", lines)
    for l in lines:
        l = l.rstrip()
        print(l)
        for i in range(len(l)):
            freq[row][ord(l[i]) - 1] = freq[row][ord(l[i]) - 1] + 1
        row += 1

    # Find the count of valid pairs
    for i in range(122):
        if freq[0][i] > 0 and freq[1][i] > 0 and freq[2][i] > 0:
            if chr(i).islower():
                count += i - 95
            else:
                count += i - 37
    print(count)
    return count


# main
f = open("day-3-input", "r")
ans = 0
with f as infile:
    while True:
        lines = list(islice(infile, 3))
        if lines:
            ans += count3Pairs(lines)
            continue
        break
print("ans", ans)

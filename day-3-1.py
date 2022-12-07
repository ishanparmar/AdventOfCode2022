def countPairs(s1, n1, s2):
    # To store the frequencies of characters
    # of string s1 and s2
    freq1 = [0] * 122
    freq2 = [0] * 122

    # To store the count of valid pairs
    count = 0

    # Update the frequencies of the characters of string s1
    for i in range(n1):
        freq1[ord(s1[i]) - 1] += 1
        freq2[ord(s2[i]) - 1] += 1

    # Find the count of valid pairs
    for i in range(122):
        if freq1[i] > 0 and freq2[i] > 0:
            if chr(i).islower():
                count += i-95
            else:
                count += i - 37
    return count


f = open("day-3-input", "r")
ans = 0
for l in f:
    l = l.rstrip() #remove the trailing /n
    length = int(len(l)/2)
    s1 = l[slice(0, length, 1)] #first half of string
    s2 = l[slice(length, len(l), 1)] #second half of string
    ans += countPairs(s1, len(s1), s2)
print(ans)





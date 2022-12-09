from collections import Counter
def finddupes(inputstring):
    string = Counter(inputstring)
    for char, count in string.items():
        if (count > 1):
            return False
    return True


f = open("day-6-input", "r")
s = f.read()
count = 0
for i in range(len(s)):
    if finddupes(s[i:i+14]):
        print(count+14)
        break
    else :
        count += 1
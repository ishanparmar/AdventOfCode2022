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
    if finddupes(s[i:i+4]):
        print(count+4)
        break
    else :
        count += 1
file = open("input.txt", "r")

def compareChrs(str1,str2):
    for i in str1:
        for j in str2:
            if i==j:
                return i

def get_score(chr1):
    value = ord(chr1)
    if chr1.isupper():
        return value-64+26
    else:
        return value-96

total=0
for line in file.readlines():
    length = len(line.strip())
    half1 = line[0:int(length/2)]
    half2 = line[int(length/2):length]
    charMess = compareChrs(half1,half2)
    total+=get_score(charMess)
    
print(total)
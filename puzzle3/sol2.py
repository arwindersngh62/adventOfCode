from pathlib import Path
file = open( Path(__file__).parent.absolute()/"input.txt", "r")
count = 0
group = ["","",""]
priority = 0
def get_common(str1,str2,str3):
    output = set(str1).intersection(set(str2))
    output = output.intersection(set(str3))
    return output.pop()
    
def get_score(chr1):
    print(chr1)
    value = ord(chr1)
    if chr1.isupper():
        return value-64+26
    else:
        return value-96

def get_priority(group):
    common = get_common(group[0], group[1], group[2])
    return get_score(common)
if __name__ == "__main__":  
    for line in file.readlines():
        if count>2:
            count=0
            priority+=get_priority(group)
            group = ["","",""]
        group[count] = line[:-1]
        count= count+1
priority+=get_priority(group)
print(priority)
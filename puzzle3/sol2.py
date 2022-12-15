file = open("input.txt", "r")
count = 0
group = ["","",""]
priority = 0
def get_common(str1,str2):
    output = ""
    for i in str1:
        for j in str2:
            if i==j:
                output+=i
    return output
    
def get_score(chr1):
    value = ord(chr1)
    if chr1.isupper():
        return value-64+26
    else:
        return value-96

def get_priority(group):
    commons = get_common(group[0], group[1])
    common = get_common(commons, group[2])
    print(common)
    return get_score(common[0])
    
for line in file.readlines():
    if count>2:
        count=0
        
        priority+=get_priority(group)
        group = ["","",""]
    group[count] = line[:-1]
    count= count+1
print(priority)
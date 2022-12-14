win = ("AY", "BZ", "CX")
lose = ("AZ", "BX", "CY")
mapping = {"X":1,"Y":2,"Z":3}
points = 0
file = open("input.txt","r")
for line in file.readlines():
    value = line.replace(" ","").strip()
    if value in win:
        points+=(6+mapping[value[1]])
        
    elif value in lose:
        points+=(0+mapping[value[1]])
        
    else:
        points+=(3+mapping[value[1]])
        
print(points)


win = {"A":2,"B":3,"C":1}
lose = {"A":3,"B":1,"C":2}
draw= {"A":1,"B":2,"C":3}
points = 0
file = open("input.txt","r")
for line in file.readlines():
    value = line.replace(" ","").strip()
    if value[1]=="X":
        points+=(0+lose[value[0]])
    elif value[1]=="Y":
        points+=(3+draw[value[0]])        
    elif value[1]=="Z":
        points+=(6+win[value[0]])
        
print(points)

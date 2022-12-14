file = open("input.txt","r")
count = 1
count_max = 1
max_sum = 0
total=0
for line in file.readlines():
    if line=="\n":
        if max_sum<total:
            max_sum=total
            max_count=count
        total=0
        count+=1
    else:
        total= total+int(line)

print(max_sum,max_count)
    


    


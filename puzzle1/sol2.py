file = open("input.txt","r")
max_sum = [0,0,0]
total=0
def check_and_replace(value):
    if value>=max_sum[0]:
        max_sum[2] = max_sum[1]
        max_sum[1] = max_sum[0]
        max_sum[0] = value
    elif value>=max_sum[1]:
        max_sum[2] = max_sum[1]
        max_sum[1] = value
    elif value>=max_sum[2]:
        max_sum[2] = value
for line in file.readlines():
    if line=="\n":
        
        check_and_replace(total)
        total=0
    else:
        total= total+int(line)



print(sum(max_sum))

from pathlib import Path


def check_fully_contained(pair):
    first_range = list(map(int, pair[0].split("-")))
    second_range = list(map(int, pair[1].split("-")))
    if first_range[0]==first_range[1] or second_range[0]==second_range[1]:
        return null_set_overlap_check(first_range, second_range)
    return check_range_overlap(range(first_range[0],first_range[1]), range(second_range[0], second_range[1]))
    
    
def check_range_overlap(range1, range2):
    return set(range1).issubset(set(range2)) or set(range2).issubset(set(range1))
    
def null_set_overlap_check(range1, range2):
    if range1[0] == range1[1]:
        return range2[0]<=range1[0]
    else:
        return range1[0]<=range2[0]
        
    

def main():
    file = open( Path(__file__).parent.absolute()/"input.txt", "r")
    contained_count = 0
    for line in file.readlines():
        if line[-1] == "\n":
            line= line[:-1]
        pair = line.split(",")
        contained_count+=int(check_fully_contained(pair))
        print(check_fully_contained(pair), int(check_fully_contained(pair)))
        print(contained_count)
        
        
        
if __name__ == "__main__":
    main()
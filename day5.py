### DAY 5: Hydrothermal Venture ###

fp = '5_input.txt'
with open(fp) as f:
    inputs = f.readlines()
inputs = [x.rstrip().replace(' -> ',',').split(',') for x in inputs]
inputs = [[int(val) for val in x] for x in inputs]

# determine max map dimensions
max_dim = max([max(x) for x in inputs])

# discard non-horizontal lines
trunc_inputs = [x for x in inputs if x[0]==x[2] or x[1]==x[3]]


def init_diag():
    # return [[0 for x in range(x_max+1)] for y in range(y_max+1)]
    return [[0 for x in range(max_dim+1)] for y in range(max_dim+1)]

def update_diag(line,diag):
    new = diag
    if line[0] == line[2]:
        row = line[0]
        col_max = max(line[1], line[3])
        col_min = min(line[1], line[3])
        for col in range(col_min,col_max+1):
            new[row][col] += 1
            
    elif line[1] == line[3]:
        col = line[1]
        row_max = max(line[0], line[2])
        row_min = min(line[0], line[2])
        for row in range(row_min,row_max+1):
            new[row][col] += 1
    else:
        print("error: non-linear vents")
        
    return new

def score(diag):
    return sum([1 for row in diag for col in row if col>1])
    

diag1 = init_diag()
for line in trunc_inputs:
    diag1 = update_diag(line,diag1)

print(score(diag1))

# PART 2 #

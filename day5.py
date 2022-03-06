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

def update_diag2(line,diag):
    
    x1,y1,x2,y2 = line
    new = diag

    row_max = max(x1,x2)
    row_min = min(x1,x2)
    col_max = max(y1,y2)
    col_min = min(y1,y2)
    
    
    if x1 == x2:
        row = x1
        for col in range(col_min,col_max+1):
            new[row][col] += 1
            
    elif y1 == y2:
        col = line[1]
        for row in range(row_min,row_max+1):
            new[row][col] += 1
                
    elif abs(x1-x2) == abs(y1-y2):
        dx = 1 if x2 > x1 else -1
        dy = 1 if y2 > y1 else -1

        row = x1
        col = y1
        while row!=x2 + 1*dx:
            new[row][col] += 1
            row += 1*dx
            col += 1*dy

        
    else:
        print("error: non-linear, non-diagonal vents")
        
    return new



trunc_inputs_pt2 = [x for x in inputs if x[0]==x[2] or x[1]==x[3] 
                    or abs(x[0]-x[2])==abs(x[1]-x[3])]

diag2 = init_diag()
for line in trunc_inputs_pt2:
    diag2 = update_diag2(line,diag2)

print(score(diag2))


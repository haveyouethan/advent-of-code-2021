### DAY 4: Giant Squid ###
fp = '4_input.txt'
with open(fp) as f:
  draw = f.readline().rstrip().split(',')
  boards = f.readlines()

boards = [x.rstrip() for x in boards if x != '\n']

# Transform each board into one object under lst_boards, 
# accessible by [row][col]
boards = [row.split() for row in boards]
lst_boards = []
lst_boards = list(zip(boards[::5],
                      boards[1::5],
                      boards[2::5],
                      boards[3::5],
                      boards[4::5]))

# convert zip tuple to lists
lst_boards = [list(board) for board in lst_boards] 

#flatten 2d array into 1d
lst_boards = [[int(val) for row in board for val in row] for board in lst_boards]
draw = [int(x) for x in draw]

# create and init matrix for each board to mark as number drawn
score_boards = [[0]*25 for i in range(len(lst_boards))]

stop = False
for number_drawn in draw:
    # for each value drawn, update scoreboard
    for b,board in enumerate(lst_boards):
        if number_drawn in board:
            idx = board.index(number_drawn)
            score_boards[b][idx] = 1

    # check scoreboards
    for s,s_board in enumerate(score_boards):
        rows = [sum(s_board[5*i:5*i+5]) for i in range(5)]
        cols = [sum(s_board[i::5]) for i in range(5)]
        if (5 in rows) or (5 in cols):
            stop = True
            break
                
    if stop == True:
         unmarked = [lst_boards[s][i] for i,v in enumerate(s_board) if v == 0]
         answer_pt1 = sum(unmarked)*int(number_drawn)
         break

print(f'part1: {answer_pt1}')

# PART 2#

# create and init matrix for each board to mark as number drawn
score_boards = [[0]*25 for i in range(len(lst_boards))]

stop = False
blacklist = []

for number_drawn in draw:
    # for each value drawn, update scoreboard
    for b,board in enumerate(lst_boards):
        if b in blacklist:
            continue
        if number_drawn in board:
            idx = board.index(number_drawn)
            score_boards[b][idx] = 1

    # check scoreboards
    for s,s_board in enumerate(score_boards):
        rows = [sum(s_board[5*i:5*i+5]) for i in range(5)]
        cols = [sum(s_board[i::5]) for i in range(5)]
        if (5 in rows) or (5 in cols):
            blacklist.append(s)

last_board = score_boards[blacklist[-1]]
unmarked = [lst_boards[s][i] for i,v in enumerate(last_board) if v == 0]
answer_pt2 = sum(unmarked)*int(number_drawn)
print(f'part2: {answer_pt2}')


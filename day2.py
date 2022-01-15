### DAY 2: Dive! ###
fp = '2_input.txt'
with open(fp) as f:
  data = f.readlines()

instructions = [line.rstrip().split(' ') for line in data]

class Sub:
  def __init__(self):
    self.horizontal = 0
    self.depth = 0
  
  def forward(self, forward_value):
    self.horizontal += forward_value

  def down(self, down_value):
    self.depth += down_value

  def up(self, up_value):
    self.depth -= up_value

  def answer(self):
    return(self.horizontal * self.depth)

sub = Sub()
for line in instructions:
  order = line[0]
  value = int(line[1])
  # print(order,value)
  if order == 'forward':
    sub.forward(value)
  elif order == 'down':
    sub.down(value)
  elif order == 'up':
    sub.up(value)

sub.answer()

### PART TWO ###
class Sub2:
  def __init__(self):
    self.horizontal = 0
    self.depth = 0
    self.aim = 0
  
  def forward(self, forward_value):
    self.horizontal += forward_value
    self.depth += self.aim*forward_value

  def down(self, down_value):
    self.aim += down_value

  def up(self, up_value):
    self.aim -= up_value

  def answer(self):
    return(self.horizontal * self.depth)
  
  sub2 = Sub2()

for line in instructions:
  order = line[0]
  value = int(line[1])
  # print(order,value)
  if order == 'forward':
    sub2.forward(value)
  elif order == 'down':
    sub2.down(value)
  elif order == 'up':
    sub2.up(value)

sub2.answer()


### DAY 5: Lanternfish ###

fp = '6_input.txt'
with open(fp) as f:
    inputs = f.readlines()

inputs = inputs[0].rstrip().split(',')
inputs = [int(x) for x in inputs]

class Lanternfish:
    def __init__(self, inputs):
        self.day = 0
        self.fishes = inputs
        
    def count_fishes(self):
        return len(self.fishes)
    
    def next_day(self):
        self.day += 1
        self.fishes = self.next_fishes()
    
    def days(self,num_days):
        for day in range(num_days):
            self.next_day()
        
    def next_fishes(self):
        new = [None] * self.count_fishes()
        
        for idx,fish in enumerate(self.fishes):
            if fish == 0:
                new.append(8)
                new[idx] = 6
            else:
                new[idx] = fish - 1
        return new
                
            
    
testcase = [3,4,3,1,2]
tc_fish = Lanternfish(testcase)
tc_fish.days(18)
assert tc_fish.count_fishes()==26 
tc_fish.tc_fish(80-18)
assert fish.count_fishes()==5934 
print('test cases passed')


fish = Lanternfish(inputs)
fish.days(80)
print(fish.count_fishes())


# PART TWO #

class Fishstock:
    """count by census buckets of fish age, 
    instead of by individual fishes"""
    def __init__(self, inputs):
        self.day = -1
        
        tracker = [0]*9
        for fish in inputs:
            tracker[fish] += 1
        self.fishes = tracker

    def count_fishes(self):
        return sum(self.fishes)
    
    def next_day(self):
        self.day += 1
        self.fishes = self.next_fishes()
    
    def days(self,num_days):
        for day in range(num_days):
            self.next_day()
        
    def next_fishes(self):
        new = self.fishes[1:] + self.fishes[:1]
        new[6] += self.fishes[0]
        return new
        
tc_fish = Fishstock(testcase)
tc_fish.days(18)
assert tc_fish.count_fishes()==26 
tc_fish.days(80-18)
assert tc_fish.count_fishes()==5934 
print('test cases (part 2) passed')


fish = Fishstock(inputs)
fish.days(80)
print(fish.count_fishes())

fish.days(256-80)
print(fish.count_fishes())

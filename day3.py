### Day 3: Binary Diagnostic ###
fp = '3_input.txt'
with open(fp) as f:
  data = f.readlines()
report = [line.rstrip() for line in data]

bits = len(report[0])  # 12 bits

lst_gamma = []
for bit in range(bits):
  sum_ones = sum([int(i[bit]) for i in report])
  lst_gamma.append(int(sum_ones > (len(report)/2)))

lst_epsilon = [1-i for i in lst_gamma]

lst_gamma = [str(i) for i in lst_gamma]
bin_gamma = ''.join(lst_gamma)
dec_gamma = int(bin_gamma,2)

lst_epsilon = [str(i) for i in lst_epsilon]
bin_epsilon = ''.join(lst_epsilon)
dec_epsilon = int(bin_epsilon,2)

print(dec_gamma * dec_epsilon)


### PART TWO ###
def oxy(bit):
  # print(bit)
  if bit == 0:
    lst_in = report
  else:
    lst_in = oxy(bit-1)
  if len(lst_in)==1:
    return(lst_in)
  sum_ones = sum([int(line[bit]) for line in lst_in])
  common_value = int(sum_ones >= (len(lst_in)/2))
  return [line for line in lst_in if int(line[bit])==common_value]

def co2(bit):
  # print(bit)
  if bit == 0:
    lst_in = report
  else:
    lst_in = co2(bit-1)
  if len(lst_in)==1:
    return(lst_in)
  sum_ones = sum([int(line[bit]) for line in lst_in])
  common_value = int(sum_ones >= (len(lst_in)/2))
  return [line for line in lst_in if int(line[bit])==(1-common_value)]   
  
dec_oxy = int(oxy(bits-1)[0],2)
dec_co2 = int(co2(bits-1)[0],2)

print(dec_oxy*dec_co2)

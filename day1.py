### DAY 1: Sonar Sweep ###
import pandas as pd
fp = '1_input.txt'
df = pd.read_csv(fp,header=None)

df_results = df > df.shift(1)
df_results.sum()

### PART TWO ###
df_3m = df + df.shift(1) + df.shift(2)
df_results2 = df_3m > df_3m.shift(1)
df_results2.sum()

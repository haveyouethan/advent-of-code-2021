import pandas as pd
fp = '1_input.txt'
df = pd.read_csv(fp,header=None)

df_results = df > df.shift(1)
df_results.sum()

### PART TWO ###
df_results2 = df_3m > df_3m.shift(1)
df_results2.sum()

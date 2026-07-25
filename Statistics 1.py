import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style='whitegrid')

df = sns.load_dataset('tips')

# ? print(df.tail())  df.head() print first 5 elements df.tail() prints last 5 elements

# ? print(df.info())  used to print info

col = df['total_bill']

mean_val = np.mean(col)
median_val = np.median(col)
mode_val = col.mode()[0]

print(mean_val)
print(median_val)
print(mode_val)

jj = plt.subplots(figsize=(15,6))

sns.histplot(col,kde=True,color='b') # right skew distribution
plt.axvline(median_val,color='green',linestyle='-',label=f'Median {median_val:.2f}')
plt.axvline(mean_val,color='red',linestyle='-',label=f'Mean {mean_val:.2f}')
plt.legend()
plt.show()
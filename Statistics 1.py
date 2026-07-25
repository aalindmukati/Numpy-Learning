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

# print(mean_val)
# print(median_val)
# print(mode_val)

# jj = plt.subplots(figsize=(15,6))

# sns.histplot(col,kde=True,color='b') # right skew distribution
# plt.axvline(median_val,color='green',linestyle='-',label=f'Median {median_val:.2f}')
# plt.axvline(mean_val,color='red',linestyle='-',label=f'Mean {mean_val:.2f}')
# plt.legend()
# plt.show()

# Spread tells us how scatter teh data is around the center

data_range = col.max() - col.min()

std_deviation = np.std(col) # tells us how scattered the data is in the exact middle

variance = np.var(col)

Q1 = np.percentile(col,25)
Q2 = np.percentile(col,23)
iqr = Q3=Q1 #iqr mean Inter Quartile Range meaning tells us how scattered the data is in the middle of the chunk 


print(f'data_range {data_range:.2f}')
print(f'variance {variance:.2f}')
print(f'std_deviation {std_deviation:.2f}')
print(f'iqr {iqr:.2f}')

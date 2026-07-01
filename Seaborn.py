import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

tips = sns.load_dataset("tips")
sns.set_style('darkgrid')
sns.set_palette('viridis')

print(tips.shape)

print(tips.head())

figax1 = plt.subplots(figsize=(15,4))
sns.histplot(tips['total_bill'])
plt.show()
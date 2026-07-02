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

#--------------Histogram----------------
# sns.histplot(tips['total_bill'],kde=True)
# plt.title('Bill distribution')
#---------------------------------------

#--------------Box-Plot----------------
# sns.boxplot(x='day',y='total_bill',data=tips,palette='pastel',hue='day')
#---------------------------------------

#--------------Count-Plot----------------
sns.countplot(x='day',data=tips,palette='pastel',hue='sex')
plt.xlabel('Day',fontsize=12)
plt.ylabel('Counting',fontsize=12)
plt.show()
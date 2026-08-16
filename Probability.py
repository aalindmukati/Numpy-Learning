import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

np.random.seed(42)

n = 1000
# outcomes = np.random.choice(['H','T'],size = n) # ! so it creates an array with n elements in it and in that it can be either h or t
# print(outcomes[:150])
# heads = np.sum(outcomes='H')
# tails = np.sum(outcomes='T')

# print('Head:',heads)
# print('Tails:',tails)

dice = np.random.randint(1,7,size=n)
p_dice = np.mean(dice == 4)
print("Probability of 4 = ",p_dice)

vals, counts = np.unique(dice,return_counts=True) #! YOU CAN PASS ANY ARRAY THROUGH IT AND WHAT THIS SAYS IS "FIND THE UNIQUE VALUES AND HOW MANY TIMES THEY HAVE APPEARED"
print(vals)
print(counts)
sns.histplot(dice,discrete=True,kde=True)
plt.show()

